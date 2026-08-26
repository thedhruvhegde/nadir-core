from __future__ import annotations

from collections import deque
from typing import Deque, List, Optional, Tuple

import numpy as np

from nadir_core.dashcam.types import FramePacket, MountEstimate
from nadir_core.dashcam.vision.flow import FlowTracker
from nadir_core.dashcam.vision.horizon import estimate_horizon
from nadir_core.dashcam.vision.preprocess import resize_max
from nadir_core.dashcam.vision.vanishing import estimate_vanishing_yaw


class MountTracker:
    def __init__(self, window: int = 24, max_width: int = 960) -> None:
        self.window = window
        self.max_width = max_width
        self.flow = FlowTracker()
        self._yaw: Deque[float] = deque(maxlen=window)
        self._pitch: Deque[float] = deque(maxlen=window)
        self._roll: Deque[float] = deque(maxlen=window)
        self._baseline_yaw: Optional[float] = None
        self._baseline_pitch: Optional[float] = None
        self._baseline_roll: Optional[float] = None

