from __future__ import annotations

import math
from typing import List, Optional

from nadir_core.dashcam.types import MountEstimate
from nadir_core.scoring import PulseScoringOptions, SensorReadings, score_pulse
from nadir_core.scoring.types import ResidualScoreResult


def _rot_yaw_pitch(yaw_deg: float, pitch_deg: float = 0.0) -> List[float]:
    y = math.radians(yaw_deg)
    p = math.radians(pitch_deg)
    cy, sy = math.cos(y), math.sin(y)
    cp, sp = math.cos(p), math.sin(p)
    # R = Ry * Rp (camera extrinsics residual proxy)
    return [
        cy * cp,
