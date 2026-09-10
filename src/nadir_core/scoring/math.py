"""Pure numerical helpers for cross-modal drift scoring."""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

import numpy as np

from .types import ScoringThresholds, SensorReadings

_IDENTITY_ROW_MAJOR: Tuple[float, ...] = (
    1.0, 0.0, 0.0,
    0.0, 1.0, 0.0,
    0.0, 0.0, 1.0,
)


def rotation_residual_deg(
    current: Sequence[float],
    baseline: Sequence[float],
) -> float:
    """
    Geodesic angle between two SO(3) rotation matrices (row-major 9-vectors).

    Matches ``api.main._rotation_residual_deg``.
    """
    r_cur = np.array(current, dtype=np.float64).reshape(3, 3)
    r_bas = np.array(baseline, dtype=np.float64).reshape(3, 3)
    r_res = r_cur @ r_bas.T
    trace = float(np.clip((np.trace(r_res) - 1.0) / 2.0, -1.0, 1.0))
    return float(np.degrees(np.arccos(trace)))


def radar_drift_mm(
    range_bias_m: Optional[float],
    azimuth_bias_deg: Optional[float],
    *,
    azimuth_scale: float = 12.0,
) -> float:
    """Composite radar drift in millimeters (matches API ingest logic)."""
    rad_mm = abs(range_bias_m or 0.0) * 1000.0
    if azimuth_bias_deg:
        rad_mm += abs(azimuth_bias_deg) * azimuth_scale
    return float(rad_mm)


def lidar_drift_mm(registration_error_m: Optional[float]) -> float:
    return float(abs(registration_error_m or 0.0) * 1000.0)


def normalized_drift_vector(
    camera_deg: float,
    radar_mm: float,
    lidar_mm: float,
    thresholds: ScoringThresholds,
) -> Tuple[float, float, float]:
    """Per-modality normalisation used before Mahalanobis and residual norm."""
    cam_n = camera_deg / thresholds.camera_sigma_deg
    rad_n = radar_mm / thresholds.radar_sigma_mm
    lid_n = lidar_mm / thresholds.lidar_sigma_mm
    return cam_n, rad_n, lid_n


def mahalanobis_distance(
    drift_vec: Sequence[float],
    sigma_diag: Optional[Sequence[float]] = None,
) -> float:
    """Mahalanobis distance with diagonal covariance (identity by default)."""
    vec = np.array(drift_vec, dtype=np.float64)
    sigma = np.ones_like(vec) if sigma_diag is None else np.array(sigma_diag, dtype=np.float64)
    sigma_inv = np.diag(1.0 / (sigma + 1e-9))
    return float(np.sqrt(vec @ sigma_inv @ vec))


def residual_norm(drift_vec: Sequence[float]) -> float:
    """L2 norm of the normalised drift vector."""
    vec = np.array(drift_vec, dtype=np.float64)
    return float(np.linalg.norm(vec))


def health_score(camera_deg: float, radar_mm: float, lidar_mm: float) -> float:
    """Fleet health score penalty model (matches ``api.main._health_score``)."""
    penalty = camera_deg * 18.0 + radar_mm * 4.0 + lidar_mm * 3.0
    return round(max(0.0, min(100.0, 100.0 - penalty)), 2)


def extract_drift_measurements(
    sensors: SensorReadings,
    baseline_camera_rotation: Optional[Sequence[float]],
    thresholds: ScoringThresholds,
) -> Tuple[float, float, float]:
    """Compute raw camera/radar/lidar drift from sensor readings."""
    cam_deg = 0.0
    baseline = baseline_camera_rotation
    if baseline is None and sensors.camera_rotation_matrix is not None:
        baseline = _IDENTITY_ROW_MAJOR

    if sensors.camera_rotation_matrix is not None and baseline is not None:
        if len(sensors.camera_rotation_matrix) == 9 and len(baseline) == 9:
            try:
                cam_deg = rotation_residual_deg(sensors.camera_rotation_matrix, baseline)
            except (ValueError, np.linalg.LinAlgError):
                cam_deg = 0.0

    rad_mm = radar_drift_mm(
        sensors.radar_range_bias_m,
        sensors.radar_azimuth_bias_deg,
        azimuth_scale=thresholds.radar_azimuth_mm_per_deg,
    )
    lid_mm = lidar_drift_mm(sensors.lidar_registration_error_m)
    return cam_deg, rad_mm, lid_mm


def fault_vector_from_normalized(
    cam_n: float,
    rad_n: float,
    lid_n: float,
) -> dict[str, float]:
    """
    Normalised contribution weights summing to 1.0 (deterministic rounding).
    """
    total = cam_n + rad_n + lid_n
    if total <= 1e-12:
        third = round(1.0 / 3.0, 6)
        return {"camera": third, "radar": third, "lidar": third}
    return {
        "camera": round(cam_n / total, 6),
        "radar": round(rad_n / total, 6),
        "lidar": round(lid_n / total, 6),
    }


def round_score(value: float, places: int = 6) -> float:
    """Deterministic rounding for reproducible outputs across platforms."""
    return float(round(value, places))
