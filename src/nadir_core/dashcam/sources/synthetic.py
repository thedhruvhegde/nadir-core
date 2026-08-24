from __future__ import annotations

import time
from typing import Iterator, Optional

import numpy as np

from nadir_core.dashcam.sources.base import BaseSource
from nadir_core.dashcam.types import FramePacket, SourceKind


def make_road_frame(
    h: int = 360,
    w: int = 640,
    *,
    horizon_y: float = 0.45,
    roll_deg: float = 0.0,
    yaw_shift_px: float = 0.0,
    seed: int = 0,
) -> np.ndarray:
