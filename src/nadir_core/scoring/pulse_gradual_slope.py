"""Gradual residual-slope detector for Pulse (validation campaign lift).

Page-Hinkley style one-sided detector on the first difference of Mahalanobis
distance. Tuned for micro-gradual ramps where pointwise thresholds stay
NOMINAL too long. Feature-flagged via ``PulseScoringOptions.enable_gradual_slope_boost``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from threading import Lock
from typing import Dict, Optional

from .types import DriftTier, ScoringThresholds


@dataclass(frozen=True)
class GradualSlopeConfig:
    delta: float = 0.008
    threshold: float = 0.18
    warmup_samples: int = 5
    boost_mahal_fraction: float = 0.35
    min_mahal_absolute: float = 0.85
    min_slope: float = 0.002


@dataclass(frozen=True)
class GradualSlopeUpdate:
    slope: float
    statistic: float
    triggered: bool
    warmed_up: bool


@dataclass
class GradualSlopeTracker:
    config: GradualSlopeConfig = field(default_factory=GradualSlopeConfig)
    _prev: Optional[float] = None
    _count: int = 0
    _mean_slope: float = 0.0
    _ph: float = 0.0
    _min_ph: float = 0.0

    def update(self, mahal: float) -> GradualSlopeUpdate:
        cfg = self.config
        value = float(mahal)
        self._count += 1
        if self._prev is None:
            self._prev = value
            return GradualSlopeUpdate(0.0, 0.0, False, False)
        slope = value - self._prev
        self._prev = value
        if self._count < cfg.warmup_samples:
            return GradualSlopeUpdate(slope, 0.0, False, False)

        # Page-Hinkley on positive residual slope (drift building up).
        self._mean_slope += (slope - self._mean_slope) / max(1, self._count - 1)
        self._ph = self._ph + (slope - self._mean_slope - cfg.delta)
        self._min_ph = min(self._min_ph, self._ph)
        statistic = self._ph - self._min_ph
        triggered = statistic > cfg.threshold and slope >= cfg.min_slope
        return GradualSlopeUpdate(
            slope=slope,
            statistic=statistic,
            triggered=triggered,
            warmed_up=True,
        )


@dataclass(frozen=True)
class GradualSlopeResult:
    triggered: bool
    statistic: float
    slope: float
    warmed_up: bool
    tier_boosted: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "triggered": self.triggered,
            "statistic": round(self.statistic, 4),
            "slope": round(self.slope, 6),
            "warmed_up": self.warmed_up,
            "tier_boosted": self.tier_boosted,
        }


_lock = Lock()
_trackers: Dict[str, GradualSlopeTracker] = {}


def get_gradual_slope_tracker(
    vehicle_id: str,
    *,
    config: Optional[GradualSlopeConfig] = None,
) -> GradualSlopeTracker:
    with _lock:
        tracker = _trackers.get(vehicle_id)
        if tracker is None:
            tracker = GradualSlopeTracker(config=config or GradualSlopeConfig())
            _trackers[vehicle_id] = tracker
        return tracker


def reset_gradual_slope_trackers() -> None:
    with _lock:
        _trackers.clear()


def apply_gradual_slope_tier_boost(
    tier: DriftTier,
    *,
    mahal: float,
    triggered: bool,
    thresholds: ScoringThresholds,
    config: Optional[GradualSlopeConfig] = None,
) -> tuple[DriftTier, bool]:
    if not triggered or tier is not DriftTier.NOMINAL:
        return tier, False
    cfg = config or GradualSlopeConfig()
    frac_floor = thresholds.mahal_caution * cfg.boost_mahal_fraction
    if mahal >= max(cfg.min_mahal_absolute, frac_floor):
        return DriftTier.CAUTION, True
    return tier, False


def evaluate_gradual_slope_boost(
    vehicle_id: str,
    tier: DriftTier,
    mahal: float,
    thresholds: ScoringThresholds,
    *,
    config: Optional[GradualSlopeConfig] = None,
) -> tuple[DriftTier, GradualSlopeResult]:
    tracker = get_gradual_slope_tracker(vehicle_id, config=config)
    update = tracker.update(mahal)
    boosted_tier, boosted = apply_gradual_slope_tier_boost(
        tier,
        mahal=mahal,
        triggered=update.triggered,
        thresholds=thresholds,
        config=config,
    )
    result = GradualSlopeResult(
        triggered=update.triggered,
        statistic=update.statistic,
        slope=update.slope,
        warmed_up=update.warmed_up,
        tier_boosted=boosted,
    )
    return boosted_tier, result
