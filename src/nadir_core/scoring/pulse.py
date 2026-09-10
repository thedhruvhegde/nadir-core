"""NADIR Pulse tier — v2 Mahalanobis scoring with composable math layers."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any, Dict, Mapping, Optional, Sequence, Union

from nadir_core.observability.pulse_timing import (
    PulseLatencyExceededError,
    PulseLatencyProfiler,
    check_pulse_latency_budget,
)
from .engine import score_residual
from .pulse_engine import run_pulse_engine
from .pulse_options import PulseScoringOptions, default_pulse_options
from .types import (
    ResidualScoreResult,
    ScoringRequest,
    ScoringThresholds,
    SensorReadings,
)

PULSE_PIPELINE_VERSION = "pulse"
PULSE_SCHEMA_VERSION = "1.1"
PULSE_LATENCY_BUDGET_MS = 200.0


def _uses_v2_engine(options: Optional[PulseScoringOptions]) -> bool:
    if options is None:
        return default_pulse_options().enable_adaptive_sigma
    return any(
        (
            options.enable_adaptive_sigma,
            options.enable_robust_mahalanobis,
            options.enable_cross_modal_gate,
            options.enable_block_covariance,
            options.enable_thermal_sigma,
            options.enable_vibration_notch,
            options.enable_edge_cusum_boost,
            options.enable_gradual_slope_boost,
            options.enable_fault_attribution_v2,
            options.enable_conformal_lite,
            options.enable_latency_profiler,
        )
    )


@dataclass(frozen=True)
class PulseScoringLane:
    """
    Canonical NADIR Pulse scoring lane.

    Mahalanobis fusion + tier gates; optional v2 layers via ``PulseScoringOptions``.
    """

    thresholds: ScoringThresholds = ScoringThresholds()
    options: PulseScoringOptions = default_pulse_options()
    pipeline_version: str = PULSE_PIPELINE_VERSION
    latency_budget_ms: float = PULSE_LATENCY_BUDGET_MS

    def score(self, request: ScoringRequest, *, max_ms: Optional[float] = None) -> ResidualScoreResult:
        """Score a full ``ScoringRequest`` on the Pulse lane."""
        return score_pulse(
            request.vehicle_id,
            request.sensors,
            baseline_camera_rotation=request.baseline_camera_rotation,
            timestamp=request.timestamp,
            timestamp_quality=request.timestamp_quality,
            thresholds=request.thresholds or self.thresholds,
            options=self.options,
            max_ms=max_ms,
        )

    def score_mapping(
        self,
        vehicle_id: str,
        sensors: Mapping[str, Any],
        *,
        baseline_camera_rotation: Optional[Sequence[float]] = None,
        timestamp: Optional[str] = None,
        timestamp_quality: Optional[Mapping[str, Any]] = None,
        pulse_context: Optional[Mapping[str, object]] = None,
        max_ms: Optional[float] = None,
    ) -> ResidualScoreResult:
        """Score a plain ``sensors`` mapping."""
        return score_pulse(
            vehicle_id,
            SensorReadings.from_mapping(sensors),
            baseline_camera_rotation=baseline_camera_rotation,
            timestamp=timestamp,
            timestamp_quality=timestamp_quality,
            thresholds=self.thresholds,
            options=self.options,
            pulse_context=pulse_context,
            max_ms=max_ms,
        )

    def score_telemetry_payload(
        self,
        payload: Mapping[str, Any],
        *,
        baseline_camera_rotation: Optional[Sequence[float]] = None,
        timestamp: Optional[str] = None,
        max_ms: Optional[float] = None,
    ) -> ResidualScoreResult:
        """Score a ``POST /v1/telemetry/ingest``-shaped payload."""
        sensors_raw = payload.get("sensors")
        if not isinstance(sensors_raw, Mapping):
            raise ValueError("telemetry payload must include a 'sensors' object")

        vehicle_id = str(payload.get("vehicle_id", ""))
        if not vehicle_id:
            raise ValueError("telemetry payload must include 'vehicle_id'")

        tq = payload.get("timestamp_quality")
        timestamp_quality = tq if isinstance(tq, Mapping) else None
        ts = timestamp or (str(payload["timestamp"]) if payload.get("timestamp") else None)

        return score_pulse(
            vehicle_id,
            SensorReadings.from_mapping(sensors_raw),
            baseline_camera_rotation=baseline_camera_rotation,
            timestamp=ts,
            timestamp_quality=timestamp_quality,
            thresholds=self.thresholds,
            options=self.options,
            pulse_context=payload,
            max_ms=max_ms,
        )

    def to_api_dict(self, result: ResidualScoreResult) -> Dict[str, Any]:
        """Serialize a Pulse result to the slim API response shape."""
        return pulse_result_to_api_dict(result)


def score_pulse(
    vehicle_id: str,
    sensors: Union[SensorReadings, Mapping[str, Any]],
    *,
    baseline_camera_rotation: Optional[Sequence[float]] = None,
    timestamp: Optional[str] = None,
    timestamp_quality: Optional[Mapping[str, Any]] = None,
    thresholds: Optional[ScoringThresholds] = None,
    options: Optional[PulseScoringOptions] = None,
    pulse_context: Optional[Mapping[str, object]] = None,
    max_ms: Optional[float] = None,
) -> ResidualScoreResult:
    """
    Run Pulse-tier scoring.

    When v2 options are enabled (adaptive sigma on by default), uses ``pulse_engine``.
    Otherwise falls back to v1 ``score_residual`` with all optional flags disabled.
    """
    effective_options = options if options is not None else default_pulse_options()
    budget_ms = max_ms if max_ms is not None else PULSE_LATENCY_BUDGET_MS
    profiler: PulseLatencyProfiler | None = None
    if effective_options.enable_latency_profiler:
        profiler = PulseLatencyProfiler(budget_ms=budget_ms)

    if _uses_v2_engine(effective_options):
        result, enrichment = run_pulse_engine(
            vehicle_id,
            sensors,
            baseline_camera_rotation=baseline_camera_rotation,
            timestamp=timestamp,
            timestamp_quality=timestamp_quality,
            thresholds=thresholds,
            options=effective_options,
            pulse_context=pulse_context,
            profiler=profiler,
        )
        latency_body = check_pulse_latency_budget(profiler, raise_on_exceed=max_ms is not None)
        enrichment_dict = enrichment.to_api_dict()
        if latency_body is not None:
            enrichment_dict["latency_ms"] = latency_body
        result = replace(result, pulse_enrichment=enrichment_dict)
    else:
        if isinstance(sensors, Mapping):
            sensor_model = SensorReadings.from_mapping(sensors)
        else:
            sensor_model = sensors
        cfg = thresholds or ScoringThresholds()
        result = score_residual(
            vehicle_id=vehicle_id,
            sensors=sensor_model,
            baseline_camera_rotation=baseline_camera_rotation,
            timestamp=timestamp,
            timestamp_quality=timestamp_quality,
            thresholds=cfg,
            apply_extrinsics_filter=False,
            apply_rts_smoother=False,
            apply_motion_gating=False,
            apply_changepoint_detection=False,
            apply_bias_kf_bank=False,
            apply_adas_constraints=False,
            apply_conformal_gating=False,
        )
        if profiler is not None:
            profiler.mark("legacy_score_residual")

    check_pulse_latency_budget(profiler, raise_on_exceed=max_ms is not None)
    return result


def pulse_result_to_api_dict(result: ResidualScoreResult) -> Dict[str, Any]:
    """
    Slim Pulse response — no forecast, conformal, ADAS, or filter blocks.

    Adds ``pipeline_version: pulse``, ``health_score``, and optional ``pulse_enrichment``.
    """
    body: Dict[str, Any] = {
        "schema_version": PULSE_SCHEMA_VERSION,
        "vehicle_id": result.vehicle_id,
        "residual_score": result.residual_score,
        "mahal_distance": result.mahal_distance,
        "tier": result.tier.value,
        "camera_drift_deg": result.camera_drift_deg,
        "radar_drift_mm": result.radar_drift_mm,
        "lidar_drift_mm": result.lidar_drift_mm,
        "recommendation": result.recommendation,
        "recommended_action": result.recommended_action.value,
        "confidence": result.confidence,
        "probable_fault_source": result.probable_fault_source.value,
        "fault_vector": dict(result.fault_vector),
        "health_score": result.health_score,
        "timestamp": result.timestamp,
        "cusum_triggered": result.cusum_triggered,
        "pipeline_version": PULSE_PIPELINE_VERSION,
        "algorithm_tier": "pulse",
    }
    if result.pulse_enrichment is not None:
        body["pulse_enrichment"] = dict(result.pulse_enrichment)
        latency = result.pulse_enrichment.get("latency_ms")
        if isinstance(latency, dict):
            body["latency_ms"] = dict(latency)
    if result.scoring_gated is not None:
        body["scoring_gated"] = result.scoring_gated
    return body


def score_pulse_api_dict(
    vehicle_id: str,
    sensors: Union[SensorReadings, Mapping[str, Any]],
    *,
    baseline_camera_rotation: Optional[Sequence[float]] = None,
    timestamp: Optional[str] = None,
    timestamp_quality: Optional[Mapping[str, Any]] = None,
    thresholds: Optional[ScoringThresholds] = None,
    options: Optional[PulseScoringOptions] = None,
    pulse_context: Optional[Mapping[str, object]] = None,
    max_ms: Optional[float] = None,
) -> Dict[str, Any]:
    """Convenience wrapper returning the Pulse API dict directly."""
    result = score_pulse(
        vehicle_id,
        sensors,
        baseline_camera_rotation=baseline_camera_rotation,
        timestamp=timestamp,
        timestamp_quality=timestamp_quality,
        thresholds=thresholds,
        options=options,
        pulse_context=pulse_context,
        max_ms=max_ms,
    )
    return pulse_result_to_api_dict(result)
