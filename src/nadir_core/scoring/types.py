"""Typed models for drift scoring inputs and outputs."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Mapping, Optional, Sequence


class DriftTier(str, Enum):
    """Drift severity tier aligned with the NADIR API and JSON schemas."""

    NOMINAL = "NOMINAL"
    CAUTION = "CAUTION"
    CRITICAL = "CRITICAL"


class RecommendedAction(str, Enum):
    """Structured remediation action codes."""

    NOMINAL_OPERATION = "nominal_operation"
    CALIBRATION_RECOMMENDED = "calibration_recommended"
    CALIBRATION_REQUIRED = "calibration_required"


class FaultSource(str, Enum):
    """Dominant modality contributing to elevated residuals."""

    CAMERA_EXTRINSICS = "camera_extrinsics"
    RADAR_ALIGNMENT = "radar_alignment"
    LIDAR_REGISTRATION = "lidar_registration"
    IMU_BIAS = "imu_bias"
    TIME_SYNC = "time_sync"
    MULTI_MODAL = "multi_modal"
    UNKNOWN = "unknown"


_TIER_RECOMMENDATIONS: Dict[DriftTier, str] = {
    DriftTier.CRITICAL: (
        "Immediate calibration required. Remove vehicle from active service."
    ),
    DriftTier.CAUTION: (
        "Schedule calibration within 72 hours. Increased monitoring active."
    ),
    DriftTier.NOMINAL: (
        "No action required. Continue standard monitoring interval."
    ),
}

_TIER_ACTIONS: Dict[DriftTier, RecommendedAction] = {
    DriftTier.CRITICAL: RecommendedAction.CALIBRATION_REQUIRED,
    DriftTier.CAUTION: RecommendedAction.CALIBRATION_RECOMMENDED,
    DriftTier.NOMINAL: RecommendedAction.NOMINAL_OPERATION,
}


@dataclass(frozen=True)
class ScoringThresholds:
    """Tier classification thresholds (defaults match ``api/main.py``)."""

    camera_critical_deg: float = 1.0
    radar_critical_mm: float = 4.0
    lidar_critical_mm: float = 3.5
    mahal_critical: float = 7.0

    camera_caution_deg: float = 0.3
    radar_caution_mm: float = 1.5
    lidar_caution_mm: float = 1.2
    mahal_caution: float = 3.0

    camera_sigma_deg: float = 0.15
    radar_sigma_mm: float = 0.8
    lidar_sigma_mm: float = 0.5

    radar_azimuth_mm_per_deg: float = 12.0


@dataclass(frozen=True)
class SensorReadings:
    """Multi-modal sensor snapshot for residual scoring."""

    camera_rotation_matrix: Optional[Sequence[float]] = None
    camera_translation_m: Optional[Sequence[float]] = None
    radar_range_bias_m: Optional[float] = None
    radar_azimuth_bias_deg: Optional[float] = None
    lidar_registration_error_m: Optional[float] = None
    lidar_confidence: Optional[float] = None
    imu_accel_mps2: Optional[Sequence[float]] = None
    imu_gyro_radps: Optional[Sequence[float]] = None
    can_vehicle_speed_mps: Optional[float] = None

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "SensorReadings":
        """Build from API/telemetry ``sensors`` object."""
        return cls(
            camera_rotation_matrix=_optional_float_seq(data.get("camera_rotation_matrix")),
            camera_translation_m=_optional_float_seq(data.get("camera_translation_m")),
            radar_range_bias_m=_optional_float(data.get("radar_range_bias_m")),
            radar_azimuth_bias_deg=_optional_float(data.get("radar_azimuth_bias_deg")),
            lidar_registration_error_m=_optional_float(data.get("lidar_registration_error_m")),
            lidar_confidence=_optional_float(data.get("lidar_confidence")),
            imu_accel_mps2=_optional_float_seq(data.get("imu_accel_mps2")),
            imu_gyro_radps=_optional_float_seq(data.get("imu_gyro_radps")),
            can_vehicle_speed_mps=_optional_float(data.get("can_vehicle_speed_mps")),
        )


@dataclass(frozen=True)
class ResidualScoreResult:
    """Deterministic output of the drift scoring engine."""

    vehicle_id: str
    residual_score: float
    mahal_distance: float
    tier: DriftTier
    camera_drift_deg: float
    radar_drift_mm: float
    lidar_drift_mm: float
    recommendation: str
    recommended_action: RecommendedAction
    confidence: float
    probable_fault_source: FaultSource
    fault_vector: Dict[str, float]
    health_score: float
    timestamp: str
    cusum_triggered: bool = False
    extrinsics_filter: Optional[Dict[str, Any]] = None
    motion_segment: Optional[str] = None
    observability_score: Optional[float] = None
    scoring_gated: Optional[bool] = None
    constraint_violation_source: Optional[str] = None
    adas_constraints: Optional[Dict[str, Any]] = None
    conformal_coverage: Optional[Dict[str, Any]] = None
    pulse_enrichment: Optional[Dict[str, Any]] = None
    meridian_enrichment: Optional[Dict[str, Any]] = None
    fleet_sparse_norm: Optional[float] = None
    apex_enrichment: Optional[Dict[str, Any]] = None
    shadow_bound: Optional[Dict[str, Any]] = None

    def to_api_dict(self) -> Dict[str, Any]:
        """Serialize to ``/v1/drift-analysis/residual-score`` response shape."""
        body = {
            "vehicle_id": self.vehicle_id,
            "residual_score": self.residual_score,
            "mahal_distance": self.mahal_distance,
            "tier": self.tier.value,
            "camera_drift_deg": self.camera_drift_deg,
            "radar_drift_mm": self.radar_drift_mm,
            "lidar_drift_mm": self.lidar_drift_mm,
            "recommendation": self.recommendation,
            "recommended_action": self.recommended_action.value,
            "confidence": self.confidence,
            "probable_fault_source": self.probable_fault_source.value,
            "fault_vector": dict(self.fault_vector),
            "timestamp": self.timestamp,
            "cusum_triggered": self.cusum_triggered,
        }
        if self.extrinsics_filter is not None:
            body["extrinsics_filter"] = dict(self.extrinsics_filter)
        if self.motion_segment is not None:
            body["motion_segment"] = self.motion_segment
        if self.observability_score is not None:
            body["observability_score"] = self.observability_score
        if self.scoring_gated is not None:
            body["scoring_gated"] = self.scoring_gated
        if self.constraint_violation_source is not None:
            body["constraint_violation_source"] = self.constraint_violation_source
        if self.adas_constraints is not None:
            body["adas_constraints"] = dict(self.adas_constraints)
        if self.conformal_coverage is not None:
            body["conformal_coverage"] = dict(self.conformal_coverage)
        if self.pulse_enrichment is not None:
            body["pulse_enrichment"] = dict(self.pulse_enrichment)
        if self.meridian_enrichment is not None:
            body["meridian_enrichment"] = dict(self.meridian_enrichment)
        if self.fleet_sparse_norm is not None:
            body["fleet_sparse_norm"] = self.fleet_sparse_norm
        if self.apex_enrichment is not None:
            body["apex_enrichment"] = dict(self.apex_enrichment)
        if self.shadow_bound is not None:
            body["shadow_bound"] = dict(self.shadow_bound)
        return body


@dataclass
class ScoringRequest:
    """Full scoring request including optional baselines and quality hints."""

    vehicle_id: str
    sensors: SensorReadings
    baseline_camera_rotation: Optional[Sequence[float]] = None
    timestamp: Optional[str] = None
    timestamp_quality: Optional[Mapping[str, Any]] = None
    thresholds: ScoringThresholds = field(default_factory=ScoringThresholds)


def recommendation_for_tier(tier: DriftTier) -> str:
    return _TIER_RECOMMENDATIONS[tier]


def action_for_tier(tier: DriftTier) -> RecommendedAction:
    return _TIER_ACTIONS[tier]


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    return float(value)


def _optional_float_seq(value: Any) -> Optional[List[float]]:
    if value is None:
        return None
    return [float(v) for v in value]
