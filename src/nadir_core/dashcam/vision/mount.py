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

    def reset(self) -> None:
        self.flow.reset()
        self._yaw.clear()
        self._pitch.clear()
        self._roll.clear()
        self._baseline_yaw = None
        self._baseline_pitch = None
        self._baseline_roll = None

    def _huber(self, values: Deque[float]) -> float:
        if not values:
            return 0.0
        arr = np.asarray(values, dtype=np.float64)
        med = np.median(arr)
        resid = arr - med
        scale = np.median(np.abs(resid)) + 1e-6
        w = 1.0 / (1.0 + (resid / (1.345 * scale)) ** 2)
        return float(np.sum(w * arr) / (np.sum(w) + 1e-9))

    def update(self, packet: FramePacket) -> MountEstimate:
        img = resize_max(packet.image, self.max_width)
        hz = estimate_horizon(img)
        vp = estimate_vanishing_yaw(img)
        fl = self.flow.update(img, packet.timestamp_s)

        # pitch from horizon vs nominal 0.45
        pitch = (hz.y_norm - 0.45) * 40.0
        yaw = vp.yaw_deg
        roll = hz.roll_deg

        self._yaw.append(yaw)
        self._pitch.append(pitch)
        self._roll.append(roll)

        yaw_s = self._huber(self._yaw)
        pitch_s = self._huber(self._pitch)
        roll_s = self._huber(self._roll)

        if self._baseline_yaw is None and len(self._yaw) >= min(8, self.window):
