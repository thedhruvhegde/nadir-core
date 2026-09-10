"""Cross-modal validity gating for NADIR Pulse tier."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple

from nadir_core.scoring.types import SensorReadings


@dataclass(frozen=True)
class CrossModalGateResult:
    """Outcome of pre-fusion cross-modal validity check."""

    accepted: bool
    valid_modalities: Tuple[str, ...]
    invalid_modalities: Tuple[str, ...]
    reason: str
    fusion_allowed: bool = True


def _modality_present(sensors: SensorReadings, name: str) -> bool:
    if name == "camera":
        return sensors.camera_rotation_matrix is not None
    if name == "radar":
        return sensors.radar_range_bias_m is not None or sensors.radar_azimuth_bias_deg is not None
    if name == "lidar":
        return sensors.lidar_registration_error_m is not None
    return False


def count_valid_modalities(sensors: SensorReadings) -> int:
    return sum(
        1
        for name in ("camera", "radar", "lidar")
        if _modality_present(sensors, name)
    )


def evaluate_cross_modal_gate(
    sensors: SensorReadings,
    *,
    cam_n: float,
    rad_n: float,
    lid_n: float,
    min_modalities: int = 2,
    confidence: float = 0.997,
) -> CrossModalGateResult:
    """
    Gate **Mahalanobis fusion** when insufficient modalities are observable.

    Scalar per-modality tier thresholds still apply when ``fusion_allowed`` is
    false — only coupled Mahalanobis escalation is suppressed.
    """
    _ = (cam_n, rad_n, lid_n, confidence)
    valid: list[str] = []
    invalid: list[str] = []

    for name in ("camera", "radar", "lidar"):
        if _modality_present(sensors, name):
            valid.append(name)
        else:
            invalid.append(name)

    if len(valid) < min_modalities:
        return CrossModalGateResult(
            accepted=False,
            valid_modalities=tuple(valid),
            invalid_modalities=tuple(invalid),
            reason=f"insufficient_modalities:{len(valid)}<{min_modalities}",
            fusion_allowed=False,
        )

    return CrossModalGateResult(
        accepted=True,
        valid_modalities=tuple(valid),
        invalid_modalities=tuple(invalid),
        reason="ok",
        fusion_allowed=True,
    )


def gate_result_to_dict(result: CrossModalGateResult) -> Mapping[str, object]:
    return {
        "accepted": result.accepted,
        "fusion_allowed": result.fusion_allowed,
        "valid_modalities": list(result.valid_modalities),
        "invalid_modalities": list(result.invalid_modalities),
        "reason": result.reason,
    }
