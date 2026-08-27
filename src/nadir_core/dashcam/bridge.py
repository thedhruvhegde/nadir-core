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
        -sy,
        cy * sp,
        sy * cp,
        cy,
        sy * sp,
        -sp,
        0.0,
        cp,
    ]


def vision_to_readings(estimate: MountEstimate) -> SensorReadings:
    # roll folded lightly into radar azimuth proxy so Pulse sees cross-signal tension
    return SensorReadings(
        camera_rotation_matrix=_rot_yaw_pitch(estimate.yaw_deg, estimate.pitch_deg),
        radar_azimuth_bias_deg=0.05 * estimate.roll_deg,
        radar_range_bias_m=0.0002 * abs(estimate.yaw_deg),
        lidar_registration_error_m=0.0002 * abs(estimate.pitch_deg),
