"""Online Welford sigma adaptation per vehicle stratum for Pulse tier."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from threading import Lock
from typing import Dict, Mapping, Optional, Tuple

from .types import ScoringThresholds


@dataclass(frozen=True)
class AdaptiveSigmaConfig:
    """Controls warm-up, blending, and clamping for online σ estimation."""

    min_samples: int = 30
    max_samples: int = 604_800
    blend_with_default: float = 0.35
    floor_ratio: float = 0.5
    ceiling_ratio: float = 3.0
    min_sigma_camera_deg: float = 0.05
    min_sigma_radar_mm: float = 0.2
    min_sigma_lidar_mm: float = 0.15


@dataclass
class _ModalityWelford:
    count: int = 0
    mean: float = 0.0
    m2: float = 0.0

    def update(self, value: float, *, max_samples: int) -> None:
        if not math.isfinite(value):
            return
        if self.count >= max_samples:
            return
        self.count += 1
        delta = value - self.mean
        self.mean += delta / self.count
        delta2 = value - self.mean
        self.m2 += delta * delta2

    @property
    def variance(self) -> float:
        if self.count < 2:
            return 0.0
        return max(self.m2 / (self.count - 1), 0.0)

    @property
    def std(self) -> float:
        return math.sqrt(self.variance)


@dataclass
class _StratumState:
    camera: _ModalityWelford = field(default_factory=_ModalityWelford)
    radar: _ModalityWelford = field(default_factory=_ModalityWelford)
    lidar: _ModalityWelford = field(default_factory=_ModalityWelford)

    def sample_count(self) -> int:
        return min(self.camera.count, self.radar.count, self.lidar.count)


def resolve_pulse_stratum(
    pulse_context: Optional[Mapping[str, object]] = None,
    *,
    ambient_temp_c: Optional[float] = None,
) -> str:
    """
    Bucket vehicles into adaptation strata.

    Uses explicit ``stratum`` from context, thermal band, or ``global``.
    """
    if pulse_context is not None:
        raw = pulse_context.get("stratum")
        if isinstance(raw, str) and raw.strip():
            return raw.strip().lower()

    temp = ambient_temp_c
    if temp is None and pulse_context is not None:
        raw_temp = pulse_context.get("ambient_temp_c")
        if isinstance(raw_temp, (int, float)):
            temp = float(raw_temp)

    if temp is not None:
        if temp >= 45.0:
            return "thermal_hot"
        if temp <= 0.0:
            return "thermal_cold"
        return "thermal_nominal"
    return "global"


def _clamp_sigma(value: float, default: float, cfg: AdaptiveSigmaConfig) -> float:
    lo = max(default * cfg.floor_ratio, 1e-6)
    hi = default * cfg.ceiling_ratio
    return float(min(max(value, lo), hi))


def _blend(default: float, observed: float, default_weight: float) -> float:
    """Blend observed scale with fleet default; ``default_weight=0.35`` → 65% observed."""
    w = min(max(default_weight, 0.0), 1.0)
    return default * w + observed * (1.0 - w)


@dataclass
class AdaptiveSigmaTracker:
    """Per (vehicle_id, stratum) online σ tracker using Welford's algorithm."""

    config: AdaptiveSigmaConfig = field(default_factory=AdaptiveSigmaConfig)
    _states: Dict[Tuple[str, str], _StratumState] = field(default_factory=dict)
    _lock: Lock = field(default_factory=Lock, repr=False)

    def _state(self, vehicle_id: str, stratum: str) -> _StratumState:
        key = (vehicle_id, stratum)
        if key not in self._states:
            self._states[key] = _StratumState()
        return self._states[key]

    def observe_normalized(
        self,
        vehicle_id: str,
        stratum: str,
        *,
        cam_n: float,
        rad_n: float,
        lid_n: float,
    ) -> int:
        """Record normalized residuals; returns stratum sample count after update."""
        with self._lock:
            state = self._state(vehicle_id, stratum)
            max_n = self.config.max_samples
            state.camera.update(abs(cam_n), max_samples=max_n)
            state.radar.update(abs(rad_n), max_samples=max_n)
            state.lidar.update(abs(lid_n), max_samples=max_n)
            return state.sample_count()

    def effective_thresholds(
        self,
        base: ScoringThresholds,
        vehicle_id: str,
        stratum: str,
    ) -> Tuple[ScoringThresholds, Dict[str, object]]:
        """
        Return adapted thresholds and metadata.

        During cold start (``count < min_samples``), returns base thresholds unchanged
        so tier classification is stable on first frames.
        """
        with self._lock:
            state = self._state(vehicle_id, stratum)
            count = state.sample_count()

            if count < self.config.min_samples:
                return base, {
                    "stratum": stratum,
                    "sample_count": count,
                    "cold_start": True,
                    "camera_sigma_deg": base.camera_sigma_deg,
                    "radar_sigma_mm": base.radar_sigma_mm,
                    "lidar_sigma_mm": base.lidar_sigma_mm,
                }

            cam_std = max(state.camera.std, state.camera.mean * 0.25, self.config.min_sigma_camera_deg)
            rad_std = max(state.radar.std, state.radar.mean * 0.25, self.config.min_sigma_radar_mm)
            lid_std = max(state.lidar.std, state.lidar.mean * 0.25, self.config.min_sigma_lidar_mm)

        blend_w = self.config.blend_with_default
        cam_sigma = _clamp_sigma(
            _blend(base.camera_sigma_deg, cam_std, blend_w),
            base.camera_sigma_deg,
            self.config,
        )
        rad_sigma = _clamp_sigma(
            _blend(base.radar_sigma_mm, rad_std, blend_w),
            base.radar_sigma_mm,
            self.config,
        )
        lid_sigma = _clamp_sigma(
            _blend(base.lidar_sigma_mm, lid_std, blend_w),
            base.lidar_sigma_mm,
            self.config,
        )

        adapted = ScoringThresholds(
            camera_critical_deg=base.camera_critical_deg,
            radar_critical_mm=base.radar_critical_mm,
            lidar_critical_mm=base.lidar_critical_mm,
            mahal_critical=base.mahal_critical,
            camera_caution_deg=base.camera_caution_deg,
            radar_caution_mm=base.radar_caution_mm,
            lidar_caution_mm=base.lidar_caution_mm,
            mahal_caution=base.mahal_caution,
            camera_sigma_deg=cam_sigma,
            radar_sigma_mm=rad_sigma,
            lidar_sigma_mm=lid_sigma,
            radar_azimuth_mm_per_deg=base.radar_azimuth_mm_per_deg,
        )
        meta = {
            "stratum": stratum,
            "sample_count": count,
            "cold_start": False,
            "camera_sigma_deg": round(cam_sigma, 6),
            "radar_sigma_mm": round(rad_sigma, 6),
            "lidar_sigma_mm": round(lid_sigma, 6),
            "observed_std": {
                "camera": round(cam_std, 6),
                "radar": round(rad_std, 6),
                "lidar": round(lid_std, 6),
            },
        }
        return adapted, meta

    def reset_vehicle(self, vehicle_id: str) -> None:
        with self._lock:
            keys = [k for k in self._states if k[0] == vehicle_id]
            for key in keys:
                del self._states[key]


_GLOBAL_ADAPTIVE_TRACKER = AdaptiveSigmaTracker()


def get_adaptive_sigma_tracker() -> AdaptiveSigmaTracker:
    return _GLOBAL_ADAPTIVE_TRACKER


def reset_adaptive_sigma_trackers() -> None:
    """Clear all vehicle state — for deterministic tests."""
    _GLOBAL_ADAPTIVE_TRACKER._states.clear()
