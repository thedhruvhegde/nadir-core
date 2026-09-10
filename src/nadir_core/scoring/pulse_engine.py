"""Pulse v2 scoring orchestrator — composable math layers P1–P10."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping, Optional, Sequence, Tuple, Union

from nadir_core.observability.pulse_timing import PulseLatencyProfiler

from .pulse_edge_cusum import evaluate_edge_cusum_boost
from .pulse_gradual_slope import evaluate_gradual_slope_boost

from .adaptive_sigma import (
    AdaptiveSigmaTracker,
    get_adaptive_sigma_tracker,
    resolve_pulse_stratum,
)
try:
    from .block_covariance import extract_block_covariance_from_bias_kf
except ImportError:
    extract_block_covariance_from_bias_kf = None  # type: ignore
from .classifier import classify_tier, estimate_confidence, infer_fault_source
from .conformal_pulse import get_pulse_conformal_lite
from .math import (
    extract_drift_measurements,
    fault_vector_from_normalized,
    health_score,
    mahalanobis_distance,
    normalized_drift_vector,
    residual_norm,
    round_score,
)
from .pulse_cross_modal_gate import evaluate_cross_modal_gate, gate_result_to_dict
from .pulse_fault_attribution import (
    attribution_confidence_from_posterior,
    bayesian_fault_posterior,
    posterior_entropy,
)
from .pulse_options import PulseEnrichment, PulseScoringOptions
from .robust_mahalanobis import RobustMahalanobisConfig, score_mahalanobis_pair
from .thermal_sigma import ThermalSigmaConfig, apply_thermal_sigma_scaling
from .types import (
    DriftTier,
    ResidualScoreResult,
    ScoringThresholds,
    SensorReadings,
    action_for_tier,
    recommendation_for_tier,
)
from .vibration_filter import apply_vibration_notch_filter


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _extract_ambient_temp(pulse_context: Optional[Mapping[str, object]]) -> Optional[float]:
    if pulse_context is None:
        return None
    raw = pulse_context.get("ambient_temp_c")
    if isinstance(raw, (int, float)):
        return float(raw)
    metadata = pulse_context.get("metadata")
    if isinstance(metadata, Mapping):
        nested = metadata.get("ambient_temp_c")
        if isinstance(nested, (int, float)):
            return float(nested)
    return None


def _merge_enrichment(base: PulseEnrichment, **kwargs: object) -> PulseEnrichment:
    data = {
        "pipeline_version": base.pipeline_version,
        "adaptive_sigma": base.adaptive_sigma,
        "robust_mahalanobis": base.robust_mahalanobis,
        "cross_modal_gate": base.cross_modal_gate,
        "block_covariance": base.block_covariance,
        "thermal_sigma": base.thermal_sigma,
        "vibration_filter": base.vibration_filter,
        "edge_cusum": base.edge_cusum,
        "fault_attribution_v2": base.fault_attribution_v2,
        "conformal_lite": base.conformal_lite,
        "scoring_gated": base.scoring_gated,
        "gate_reason": base.gate_reason,
    }
    data.update(kwargs)
    return PulseEnrichment(**data)


def _mark(profiler: Optional[PulseLatencyProfiler], name: str) -> None:
    if profiler is not None:
        profiler.mark(name)


def run_pulse_engine(
    vehicle_id: str,
    sensors: Union[SensorReadings, Mapping[str, Any]],
    *,
    baseline_camera_rotation: Optional[Sequence[float]] = None,
    timestamp: Optional[str] = None,
    timestamp_quality: Optional[Mapping[str, Any]] = None,
    thresholds: Optional[ScoringThresholds] = None,
    options: Optional[PulseScoringOptions] = None,
    pulse_context: Optional[Mapping[str, object]] = None,
    sigma_tracker: Optional[AdaptiveSigmaTracker] = None,
    profiler: Optional[PulseLatencyProfiler] = None,
) -> Tuple[ResidualScoreResult, PulseEnrichment]:
    """Execute Pulse v2 pipeline with optional math layers."""
    if isinstance(sensors, Mapping):
        sensor_model = SensorReadings.from_mapping(sensors)
    else:
        sensor_model = sensors
    _mark(profiler, "payload_normalize")

    opts = options or PulseScoringOptions()
    cfg = thresholds or ScoringThresholds()
    tracker = sigma_tracker or get_adaptive_sigma_tracker()
    enrichment = PulseEnrichment()

    ambient_temp = _extract_ambient_temp(pulse_context)
    stratum = resolve_pulse_stratum(pulse_context, ambient_temp_c=ambient_temp)

    if opts.enable_adaptive_sigma:
        cfg, adaptive_meta = tracker.effective_thresholds(cfg, vehicle_id, stratum)
        enrichment = _merge_enrichment(enrichment, adaptive_sigma=adaptive_meta)
    _mark(profiler, "adaptive_sigma")

    if opts.enable_thermal_sigma:
        thermal_cfg = ThermalSigmaConfig(
            reference_c=opts.thermal_reference_c,
            alpha_per_c=opts.thermal_alpha_per_c,
        )
        cfg, thermal_meta = apply_thermal_sigma_scaling(cfg, ambient_temp, config=thermal_cfg)
        if thermal_meta is not None:
            enrichment = _merge_enrichment(enrichment, thermal_sigma=dict(thermal_meta))
    _mark(profiler, "thermal_sigma")

    cam_deg, rad_mm, lid_mm = extract_drift_measurements(
        sensor_model,
        baseline_camera_rotation,
        cfg,
    )
    cam_n, rad_n, lid_n = normalized_drift_vector(cam_deg, rad_mm, lid_mm, cfg)

    if opts.enable_vibration_notch:
        vib = apply_vibration_notch_filter(cam_n, rad_n, lid_n, pulse_context)
        cam_n, rad_n, lid_n = vib.cam_n, vib.rad_n, vib.lid_n
        enrichment = _merge_enrichment(enrichment, vibration_filter=vib.to_dict())
    _mark(profiler, "vibration_notch")

    scoring_gated = False
    gate_reason: Optional[str] = None
    fusion_allowed = True
    if opts.enable_cross_modal_gate:
        gate = evaluate_cross_modal_gate(
            sensor_model,
            cam_n=cam_n,
            rad_n=rad_n,
            lid_n=lid_n,
            confidence=opts.cross_modal_confidence,
        )
        enrichment = _merge_enrichment(
            enrichment,
            cross_modal_gate=gate_result_to_dict(gate),
        )
        fusion_allowed = gate.fusion_allowed
        if not gate.fusion_allowed:
            gate_reason = gate.reason
    _mark(profiler, "cross_modal_gate")

    if opts.enable_block_covariance and fusion_allowed and extract_block_covariance_from_bias_kf is not None:
        block = extract_block_covariance_from_bias_kf(
            vehicle_id,
            sensor_model,
            baseline_camera_rotation=baseline_camera_rotation,
            timestamp_quality=timestamp_quality,
            pulse_context=pulse_context,
            thresholds=cfg,
        )
        mahal = block.mahal_distance
        enrichment = _merge_enrichment(
            enrichment,
            block_covariance={
                "source": block.source,
                "covariance_block": list(block.covariance_block),
                "observed_modalities": list(block.observed_indices),
                "mahal_distance": block.mahal_distance,
            },
        )
    elif opts.enable_robust_mahalanobis and fusion_allowed:
        robust_cfg = RobustMahalanobisConfig(huber_delta=opts.robust_huber_delta)
        mahal, l2_mahal = score_mahalanobis_pair(
            cam_n, rad_n, lid_n, use_robust=True, config=robust_cfg
        )
        from .robust_mahalanobis import _disagreement_ratio

        enrichment = _merge_enrichment(
            enrichment,
            robust_mahalanobis={
                "enabled": True,
                "huber_delta": opts.robust_huber_delta,
                "l2_mahal_distance": l2_mahal,
                "robust_mahal_distance": mahal,
                "disagreement_ratio": round(_disagreement_ratio(cam_n, rad_n, lid_n), 4),
            },
        )
    else:
        if fusion_allowed:
            mahal = round_score(mahalanobis_distance((cam_n, rad_n, lid_n)))
        else:
            mahal = 0.0
    _mark(profiler, "mahalanobis_fusion")

    residual = round_score(residual_norm((cam_n, rad_n, lid_n)))

    tier = classify_tier(cam_deg, rad_mm, lid_mm, mahal, cfg)
    cusum_triggered = False

    if opts.enable_edge_cusum_boost:
        tier, cusum_result = evaluate_edge_cusum_boost(
            vehicle_id,
            tier,
            mahal,
            cfg,
        )
        cusum_triggered = cusum_result.triggered
        enrichment = _merge_enrichment(enrichment, edge_cusum=cusum_result.to_dict())
    _mark(profiler, "edge_cusum")

    if opts.enable_gradual_slope_boost:
        tier, slope_result = evaluate_gradual_slope_boost(
            vehicle_id,
            tier,
            mahal,
            cfg,
        )
        enrichment = _merge_enrichment(enrichment, gradual_slope=slope_result.to_dict())
    _mark(profiler, "gradual_slope")

    fault_vec = fault_vector_from_normalized(cam_n, rad_n, lid_n)
    fault_source = infer_fault_source(
        fault_vec,
        sensors=sensor_model,
        timestamp_quality=timestamp_quality,
        camera_deg=cam_deg,
        radar_mm=rad_mm,
        lidar_mm=lid_mm,
    )

    if opts.enable_fault_attribution_v2:
        posterior = bayesian_fault_posterior(
            fault_vec,
            sensors=sensor_model,
            probable_fault_source=fault_source,
        )
        enrichment = _merge_enrichment(
            enrichment,
            fault_attribution_v2={
                "posterior": posterior,
                "entropy": posterior_entropy(posterior),
                "confidence": attribution_confidence_from_posterior(posterior),
            },
        )
    _mark(profiler, "fault_attribution")

    if opts.enable_conformal_lite:
        lite = get_pulse_conformal_lite()
        dominant = lite.dominant_modality_from_vector(fault_vec)
        gate_body = lite.apply(
            mahal,
            raw_tier=tier,
            dominant_modality=dominant,
            motion_segment=stratum.split(":")[0] if ":" in stratum else None,
        )
        enrichment = _merge_enrichment(enrichment, conformal_lite=gate_body)
        tier = DriftTier(str(gate_body["adjusted_tier"]))
    _mark(profiler, "conformal_lite")

    confidence = estimate_confidence(
        tier,
        mahal,
        sensor_model,
        camera_deg=cam_deg,
        radar_mm=rad_mm,
        lidar_mm=lid_mm,
        thresholds=cfg,
    )

    if opts.enable_adaptive_sigma:
        sample_count = tracker.observe_normalized(
            vehicle_id,
            stratum,
            cam_n=cam_n,
            rad_n=rad_n,
            lid_n=lid_n,
        )
        if enrichment.adaptive_sigma is not None:
            adaptive_meta = dict(enrichment.adaptive_sigma)
            adaptive_meta["post_update_sample_count"] = sample_count
            enrichment = _merge_enrichment(enrichment, adaptive_sigma=adaptive_meta)
    _mark(profiler, "adaptive_observe")

    enrichment = _merge_enrichment(
        enrichment,
        scoring_gated=scoring_gated,
        gate_reason=gate_reason,
    )

    result = ResidualScoreResult(
        vehicle_id=vehicle_id,
        residual_score=residual,
        mahal_distance=mahal,
        tier=tier,
        camera_drift_deg=round_score(cam_deg),
        radar_drift_mm=round_score(rad_mm),
        lidar_drift_mm=round_score(lid_mm),
        recommendation=recommendation_for_tier(tier),
        recommended_action=action_for_tier(tier),
        confidence=confidence,
        probable_fault_source=fault_source,
        fault_vector=fault_vec,
        health_score=health_score(cam_deg, rad_mm, lid_mm),
        timestamp=timestamp or _utc_now_iso(),
        cusum_triggered=cusum_triggered,
        scoring_gated=scoring_gated or None,
    )
    return result, enrichment
