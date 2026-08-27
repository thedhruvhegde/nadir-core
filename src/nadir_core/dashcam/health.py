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
