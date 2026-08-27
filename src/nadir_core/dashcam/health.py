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
