from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict, List, Optional

from nadir_core.dashcam.types import MountEstimate
from nadir_core.scoring.types import DriftTier, ResidualScoreResult


@dataclass
class HealthSample:
    timestamp_s: float
    estimate: MountEstimate
    tier: DriftTier
    mahal: float
    health_score: float
    explanation: str

    def as_dict(self) -> Dict:
        return {
            "timestamp_s": self.timestamp_s,
            "estimate": self.estimate.as_dict(),
            "tier": self.tier.value if hasattr(self.tier, "value") else str(self.tier),
            "mahal": self.mahal,
            "health_score": self.health_score,
            "explanation": self.explanation,
        }


@dataclass
class HealthSeries:
    window: int = 200
    samples: Deque[HealthSample] = field(default_factory=lambda: deque(maxlen=200))
    _cusum_pos: float = 0.0
    _cusum_neg: float = 0.0
    _slope_alert: bool = False

    def __post_init__(self) -> None:
        self.samples = deque(maxlen=self.window)

    def add(self, sample: HealthSample) -> None:
        self.samples.append(sample)
        # CUSUM on |yaw|
        x = abs(sample.estimate.yaw_deg)
        target = 0.25
        drift = 0.15
        self._cusum_pos = max(0.0, self._cusum_pos + (x - target - drift))
        self._cusum_neg = max(0.0, self._cusum_neg + (-x - target - drift))
        if len(self.samples) >= 12:
            ys = [s.estimate.yaw_deg for s in list(self.samples)[-12:]]
            slope = (ys[-1] - ys[0]) / 11.0
            self._slope_alert = abs(slope) > 0.08

    @property
    def cusum_triggered(self) -> bool:
        return self._cusum_pos > 2.5 or self._cusum_neg > 2.5

    @property
    def gradual_slope_alert(self) -> bool:
        return self._slope_alert

    def latest(self) -> Optional[HealthSample]:
        return self.samples[-1] if self.samples else None

    def summary(self) -> Dict:
        if not self.samples:
            return {"n": 0}
        tiers = [s.tier.value if hasattr(s.tier, "value") else str(s.tier) for s in self.samples]
        critical = sum(1 for t in tiers if t == "CRITICAL")
        caution = sum(1 for t in tiers if t == "CAUTION")
        last = self.samples[-1]
        return {
            "n": len(self.samples),
            "last_tier": tiers[-1],
            "caution_count": caution,
            "critical_count": critical,
            "cusum_triggered": self.cusum_triggered,
            "gradual_slope_alert": self.gradual_slope_alert,
            "last_yaw_deg": last.estimate.yaw_deg,
            "last_health_score": last.health_score,
        }
