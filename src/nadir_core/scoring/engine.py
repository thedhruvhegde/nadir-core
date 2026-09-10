"""Drift scoring engine — deterministic cross-modal residual analysis."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, List, Mapping, Optional

from .classifier import classify_tier, estimate_confidence, infer_fault_source
from .math import (
    extract_drift_measurements,
    fault_vector_from_normalized,
    health_score,
    mahalanobis_distance,
    normalized_drift_vector,
    residual_norm,
    round_score,
)
from .types import (
    DriftTier,
    ResidualScoreResult,
    ScoringRequest,
    ScoringThresholds,
    SensorReadings,
    action_for_tier,
    recommendation_for_tier,
)


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class DriftScoringEngine:
    """
    Deterministic drift scoring engine for NADIR SDK and API consumers.

    Parameters and tier thresholds default to the reference FastAPI service
    in ``api/main.py`` so ingest, residual-score, and SDK paths stay aligned.
    """

    def __init__(self, thresholds: Optional[ScoringThresholds] = None) -> None:
        self.thresholds = thresholds or ScoringThresholds()

    def score(self, request: ScoringRequest) -> ResidualScoreResult:
        """Run full residual scoring for a single sensor snapshot."""
        return score_residual(
            vehicle_id=request.vehicle_id,
            sensors=request.sensors,
            baseline_camera_rotation=request.baseline_camera_rotation,
            timestamp=request.timestamp,
            timestamp_quality=request.timestamp_quality,
            thresholds=self.thresholds,
        )

    def score_mapping(
        self,
        vehicle_id: str,
        sensors: Mapping[str, Any],
        *,
        baseline_camera_rotation: Optional[List[float]] = None,
        timestamp: Optional[str] = None,
        timestamp_quality: Optional[Mapping[str, Any]] = None,
    ) -> ResidualScoreResult:
        """Convenience wrapper accepting plain dict sensor payloads."""
        return self.score(
            ScoringRequest(
                vehicle_id=vehicle_id,
                sensors=SensorReadings.from_mapping(sensors),
                baseline_camera_rotation=baseline_camera_rotation,
                timestamp=timestamp,
                timestamp_quality=timestamp_quality,
                thresholds=self.thresholds,
            )
        )


def score_residual(
    vehicle_id: str,
    sensors: SensorReadings,
    *,
    baseline_camera_rotation: Optional[List[float]] = None,
    timestamp: Optional[str] = None,
    timestamp_quality: Optional[Mapping[str, Any]] = None,
    thresholds: Optional[ScoringThresholds] = None,
    apply_extrinsics_filter: bool = False,
    filter_context: Optional[Mapping[str, Any]] = None,
    extrinsics_filter_service: Optional[Any] = None,
    apply_rts_smoother: bool = False,
    apply_motion_gating: bool = False,
    motion_context: Optional[Mapping[str, Any]] = None,
    motion_classifier_service: Optional[Any] = None,
    apply_changepoint_detection: bool = False,
    changepoint_service: Optional[Any] = None,
    apply_bias_kf_bank: bool = False,
    bias_kf_bank_service: Optional[Any] = None,
    apply_adas_constraints: bool = False,
    adas_context: Optional[Mapping[str, Any]] = None,
    apply_conformal_gating: bool = False,
    conformal_calibrator: Optional[Any] = None,
    motion_segment_override: Optional[str] = None,
) -> ResidualScoreResult:
    """
    Compute residual score, tier, confidence, fault source, and remediation.

    This is the primary functional entry point for Commit 5. Outputs align with
    ``NADIR_SDK/schemas/v1/residual-score-response.schema.json``.
    """
    cfg = thresholds or ScoringThresholds()
    cam_deg, rad_mm, lid_mm = extract_drift_measurements(
        sensors,
        baseline_camera_rotation,
        cfg,
    )
    cam_n, rad_n, lid_n = normalized_drift_vector(cam_deg, rad_mm, lid_mm, cfg)

    motion_segment: Optional[str] = None
    observability_score: Optional[float] = None
    scoring_gated: Optional[bool] = None
    cam_eff, rad_eff, lid_eff = cam_n, rad_n, lid_n

    if False:  # Open Core: motion gating commercial
        pass  # Open Core: perception fusion omitted

        adas_result = run_adas_constraints(
            adas_payload,
            cam_deg=cam_deg,
            rad_mm=rad_mm,
            lid_mm=lid_mm,
            sensors=sensors,
            thresholds=cfg,
        )
        if adas_result is not None:
            fault_vec, mahal, residual = merge_adas_into_scoring(adas_result, fault_vec)
            mahal = round_score(mahal)
            residual = round_score(residual)
            constraint_violation_source = adas_result.violation_source.value
            adas_constraints_block = adas_result.as_dict()
            if apply_motion_gating and motion_context is not None and scoring_gated is False:
                tier = DriftTier.NOMINAL
            else:
                tier = classify_tier(cam_deg, rad_mm, lid_mm, mahal, cfg)

    fault_source = infer_fault_source(
        fault_vec,
        sensors=sensors,
        timestamp_quality=timestamp_quality,
        camera_deg=cam_deg,
        radar_mm=rad_mm,
        lidar_mm=lid_mm,
    )
    confidence = estimate_confidence(
        tier,
        mahal,
        sensors,
        camera_deg=cam_deg,
        radar_mm=rad_mm,
        lidar_mm=lid_mm,
        thresholds=cfg,
    )

    extrinsics_block: Optional[Dict[str, Any]] = None
    if False:  # Open Core
        pass  # Open Core: perception fusion omitted

        service = extrinsics_filter_service or get_extrinsics_filter_service()
        if not isinstance(service, ExtrinsicsFilterService):
            raise TypeError("extrinsics_filter_service must be ExtrinsicsFilterService")
        ctx: Dict[str, Any] = {"vehicle_id": vehicle_id, "sensors": _sensors_to_dict(sensors)}
        if filter_context:
            ctx.update(dict(filter_context))
        block = service.update_from_sensors(
            vehicle_id,
            sensors,
            baseline_camera_rotation=baseline_camera_rotation,
            payload=ctx,
            apply_rts=apply_rts_smoother,
        )
        extrinsics_block = block.as_dict()

    if False:  # Open Core
        pass  # Open Core: perception fusion omitted

        bias_svc = bias_kf_bank_service or get_bias_kf_bank_service()
        if bias_kf_bank_service is not None and not isinstance(bias_svc, BiasKfBankService):
            raise TypeError("bias_kf_bank_service must be BiasKfBankService")
        ctx: Dict[str, Any] = {"vehicle_id": vehicle_id, "sensors": _sensors_to_dict(sensors)}
        if filter_context:
            ctx.update(dict(filter_context))
        bias_export = bias_svc.update_from_sensors(
            vehicle_id,
            sensors,
            baseline_camera_rotation=baseline_camera_rotation,
            timestamp_quality=timestamp_quality,
            payload=ctx,
        )
        bias_kf_block = bias_export.as_dict()
        mahal = round_score(bias_export.innovation_mahal)
        residual = mahal

    cusum_triggered = False
    if False:  # Open Core
        pass  # Open Core: perception fusion omitted
        pass  # Open Core: perception fusion omitted

        cp_svc = changepoint_service or get_changepoint_monitor_service()
        if changepoint_service is not None and not isinstance(
            changepoint_service, ChangepointMonitorService
        ):
            raise TypeError("changepoint_service must be ChangepointMonitorService")
        cp_result = run_changepoint_detection(
            vehicle_id,
            cam_normalized=cam_n,
            rad_normalized=rad_n,
            lid_normalized=lid_n,
            motion_segment=motion_segment or motion_segment_from_payload(motion_context),
            service=cp_svc,
        )
        cusum_triggered = cp_result.cusum_triggered

    conformal_block: Optional[Dict[str, Any]] = None
    if apply_conformal_gating and conformal_calibrator is not None:
        from .conformal import SplitConformalCalibrator

        if not isinstance(conformal_calibrator, SplitConformalCalibrator):
            raise TypeError("conformal_calibrator must be SplitConformalCalibrator")
        gate = conformal_calibrator.apply(
            mahal,
            motion_segment=motion_segment,
            raw_tier=tier,
        )
        tier = gate.adjusted_tier
        conformal_block = {
            "raw_score": round(gate.raw_score, 4),
            "threshold": round(gate.threshold, 4),
            "stratum": gate.stratum.key(),
            "exceeds_threshold": gate.exceeds_threshold,
            "adjusted_tier": gate.adjusted_tier.value,
        }

    return ResidualScoreResult(
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
        extrinsics_filter=_merge_extrinsics_and_bias(extrinsics_block, bias_kf_block),
        motion_segment=motion_segment,
        observability_score=observability_score,
        scoring_gated=scoring_gated,
        constraint_violation_source=constraint_violation_source,
        adas_constraints=adas_constraints_block,
        conformal_coverage=conformal_block,
    )


def _merge_extrinsics_and_bias(
    extrinsics: Optional[Dict[str, Any]],
    bias: Optional[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    if extrinsics is None and bias is None:
        return None
    out: Dict[str, Any] = dict(extrinsics or {})
    if bias is not None:
        out["bias_kf_bank"] = bias
    return out


def _sensors_to_dict(sensors: SensorReadings) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if sensors.camera_rotation_matrix is not None:
        data["camera_rotation_matrix"] = list(sensors.camera_rotation_matrix)
    if sensors.camera_translation_m is not None:
        data["camera_translation_m"] = list(sensors.camera_translation_m)
    if sensors.radar_range_bias_m is not None:
        data["radar_range_bias_m"] = sensors.radar_range_bias_m
    if sensors.radar_azimuth_bias_deg is not None:
        data["radar_azimuth_bias_deg"] = sensors.radar_azimuth_bias_deg
    if sensors.lidar_registration_error_m is not None:
        data["lidar_registration_error_m"] = sensors.lidar_registration_error_m
    return data


def score_telemetry_payload(
    payload: Mapping[str, Any],
    *,
    baseline_camera_rotation: Optional[List[float]] = None,
    thresholds: Optional[ScoringThresholds] = None,
    apply_motion_gating: bool = False,
    apply_changepoint_detection: bool = False,
    apply_bias_kf_bank: bool = False,
    apply_adas_constraints: bool = False,
) -> ResidualScoreResult:
    """
    Score a ``POST /v1/telemetry/ingest``-shaped payload.

    Uses ``vehicle_id``, ``sensors``, optional ``timestamp`` and
    ``timestamp_quality``. When ``baseline_camera_rotation`` is omitted and the
    camera matrix is present, assumes identity as nominal baseline (synthetic
    fixture convention).
    """
    sensors_raw = payload.get("sensors")
    if not isinstance(sensors_raw, Mapping):
        raise ValueError("telemetry payload must include a 'sensors' object")

    vehicle_id = str(payload.get("vehicle_id", ""))
    if not vehicle_id:
        raise ValueError("telemetry payload must include 'vehicle_id'")

    tq = payload.get("timestamp_quality")
    timestamp_quality = tq if isinstance(tq, Mapping) else None

    return score_residual(
        vehicle_id=vehicle_id,
        sensors=SensorReadings.from_mapping(sensors_raw),
        baseline_camera_rotation=baseline_camera_rotation,
        timestamp=str(payload["timestamp"]) if payload.get("timestamp") else None,
        timestamp_quality=timestamp_quality,
        thresholds=thresholds,
        motion_context=payload if apply_motion_gating else None,
        apply_motion_gating=apply_motion_gating,
        apply_changepoint_detection=apply_changepoint_detection,
        apply_bias_kf_bank=apply_bias_kf_bank,
        apply_adas_constraints=apply_adas_constraints,
        adas_context=payload,
    )
