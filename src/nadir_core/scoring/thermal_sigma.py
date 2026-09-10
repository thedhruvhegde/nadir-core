"""Temperature-compensated sigma scaling for NADIR Pulse tier."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional, Tuple

from .types import ScoringThresholds


@dataclass(frozen=True)
class ThermalSigmaConfig:
    """Linear thermal expansion model for camera σ scaling."""

    reference_c: float = 25.0
    alpha_per_c: float = 0.008
    max_scale: float = 1.35
    min_scale: float = 0.85


def thermal_scale_factor(
    ambient_temp_c: Optional[float],
    *,
    config: Optional[ThermalSigmaConfig] = None,
) -> float:
    """Return multiplicative σ scale for camera channel."""
    if ambient_temp_c is None:
        return 1.0
    cfg = config or ThermalSigmaConfig()
    delta = float(ambient_temp_c) - cfg.reference_c
    scale = 1.0 + cfg.alpha_per_c * delta
    return float(min(max(scale, cfg.min_scale), cfg.max_scale))


def apply_thermal_sigma_scaling(
    thresholds: ScoringThresholds,
    ambient_temp_c: Optional[float],
    *,
    config: Optional[ThermalSigmaConfig] = None,
) -> Tuple[ScoringThresholds, Optional[Mapping[str, object]]]:
    """
    Widen camera σ under elevated ambient temperature.

    Radar and lidar σ are unchanged — thermal cycling primarily affects
    camera mount compliance and adhesive creep rates.
    """
    if ambient_temp_c is None:
        return thresholds, None

    cfg = config or ThermalSigmaConfig()
    scale = thermal_scale_factor(ambient_temp_c, config=cfg)
    if abs(scale - 1.0) < 1e-6:
        return thresholds, None

    adapted = ScoringThresholds(
        camera_critical_deg=thresholds.camera_critical_deg,
        radar_critical_mm=thresholds.radar_critical_mm,
        lidar_critical_mm=thresholds.lidar_critical_mm,
        mahal_critical=thresholds.mahal_critical,
        camera_caution_deg=thresholds.camera_caution_deg,
        radar_caution_mm=thresholds.radar_caution_mm,
        lidar_caution_mm=thresholds.lidar_caution_mm,
        mahal_caution=thresholds.mahal_caution,
        camera_sigma_deg=thresholds.camera_sigma_deg * scale,
        radar_sigma_mm=thresholds.radar_sigma_mm,
        lidar_sigma_mm=thresholds.lidar_sigma_mm,
        radar_azimuth_mm_per_deg=thresholds.radar_azimuth_mm_per_deg,
    )
    meta = {
        "ambient_temp_c": round(float(ambient_temp_c), 2),
        "reference_c": cfg.reference_c,
        "alpha_per_c": cfg.alpha_per_c,
        "camera_sigma_scale": round(scale, 6),
        "camera_sigma_deg": round(adapted.camera_sigma_deg, 6),
    }
    return adapted, meta
