"""Edge CUSUM tracker for Pulse tier lane (P7).

Per-vehicle one-sided CUSUM on Mahalanobis distance streams. Used when
``enable_edge_cusum_boost`` is set on ``PulseScoringOptions``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from threading import Lock
from typing import Dict, List, Optional

import numpy as np

from .types import DriftTier, ScoringThresholds


@dataclass(frozen=True)
class EdgeCusumConfig:
    k: float = 0.5
    h: float = 4.5
    warmup_samples: int = 20
    boost_mahal_fraction: float = 0.92


@dataclass(frozen=True)
class CusumUpdate:
    z: float
    s_pos: float
    statistic: float
    triggered: bool
    warmed_up: bool


@dataclass
class OneSidedCUSUM:
    config: EdgeCusumConfig = field(default_factory=EdgeCusumConfig)
    _samples: List[float] = field(default_factory=list)
    _mean: Optional[float] = None
    _std: Optional[float] = None
    _s_pos: float = 0.0

    def update(self, value: float) -> CusumUpdate:
        cfg = self.config
        if self._mean is None:
            self._samples.append(float(value))
            if len(self._samples) < cfg.warmup_samples:
                return CusumUpdate(0.0, 0.0, 0.0, False, False)
            self._mean = float(np.mean(self._samples))
            self._std = max(float(np.std(self._samples)), 1e-6)

        assert self._mean is not None and self._std is not None
        z = (float(value) - self._mean) / self._std
        self._s_pos = max(0.0, self._s_pos + z - cfg.k)
        triggered = self._s_pos > cfg.h
        return CusumUpdate(
            z=z,
            s_pos=self._s_pos,
            statistic=self._s_pos,
            triggered=triggered,
            warmed_up=True,
        )


@dataclass(frozen=True)
class EdgeCusumResult:
    triggered: bool
    statistic: float
    z: float
    warmed_up: bool
    tier_boosted: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "triggered": self.triggered,
            "statistic": round(self.statistic, 4),
            "z": round(self.z, 4),
            "warmed_up": self.warmed_up,
            "tier_boosted": self.tier_boosted,
        }


_lock = Lock()
_trackers: Dict[str, OneSidedCUSUM] = {}


def get_edge_cusum(
    vehicle_id: str,
    *,
    config: Optional[EdgeCusumConfig] = None,
) -> OneSidedCUSUM:
    with _lock:
        tracker = _trackers.get(vehicle_id)
        if tracker is None:
            tracker = OneSidedCUSUM(config=config or EdgeCusumConfig())
            _trackers[vehicle_id] = tracker
        return tracker


def reset_edge_cusum_trackers() -> None:
    with _lock:
        _trackers.clear()


def update_edge_cusum(
    vehicle_id: str,
    mahal: float,
    *,
    config: Optional[EdgeCusumConfig] = None,
) -> CusumUpdate:
    tracker = get_edge_cusum(vehicle_id, config=config)
    return tracker.update(float(mahal))


def apply_edge_cusum_tier_boost(
    tier: DriftTier,
    *,
    mahal: float,
    cusum_triggered: bool,
    thresholds: ScoringThresholds,
    config: Optional[EdgeCusumConfig] = None,
) -> tuple[DriftTier, bool]:
    """Promote NOMINAL → CAUTION when edge CUSUM fires near caution Mahalanobis."""
    if not cusum_triggered or tier is not DriftTier.NOMINAL:
        return tier, False
    cfg = config or EdgeCusumConfig()
    if mahal > thresholds.mahal_caution * cfg.boost_mahal_fraction:
        return DriftTier.CAUTION, True
    return tier, False


def evaluate_edge_cusum_boost(
    vehicle_id: str,
    tier: DriftTier,
    mahal: float,
    thresholds: ScoringThresholds,
    *,
    config: Optional[EdgeCusumConfig] = None,
) -> tuple[DriftTier, EdgeCusumResult]:
    update = update_edge_cusum(vehicle_id, mahal, config=config)
    boosted_tier, boosted = apply_edge_cusum_tier_boost(
        tier,
        mahal=mahal,
        cusum_triggered=update.triggered,
        thresholds=thresholds,
        config=config,
    )
    result = EdgeCusumResult(
        triggered=update.triggered,
        statistic=update.statistic,
        z=update.z,
        warmed_up=update.warmed_up,
        tier_boosted=boosted,
    )
    return boosted_tier, result
