from __future__ import annotations

from collections import deque
from typing import Deque, List, Optional, Tuple

import numpy as np

from nadir_core.dashcam.types import FramePacket, MountEstimate
from nadir_core.dashcam.vision.flow import FlowTracker
from nadir_core.dashcam.vision.horizon import estimate_horizon
from nadir_core.dashcam.vision.preprocess import resize_max
from nadir_core.dashcam.vision.vanishing import estimate_vanishing_yaw
from nadir_core.dashcam.filters.ekf_mount import MountEKF
from nadir_core.dashcam.features.vanishing_ransac import Line2D, ransac_vanishing_point, edge_lines_from_grad_scale_0
from nadir_core.dashcam.vision.preprocess import sobel_mag, to_gray
import math


class MountTracker:
    def __init__(self, window: int = 24, max_width: int = 960) -> None:
        self.window = window
        self.max_width = max_width
        self.flow = FlowTracker()
        self.ekf = MountEKF()
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
            self._baseline_yaw = yaw_s
            self._baseline_pitch = pitch_s
            self._baseline_roll = roll_s

        if self._baseline_yaw is not None:
            yaw_s = yaw_s - self._baseline_yaw
            pitch_s = pitch_s - (self._baseline_pitch or 0.0)
            roll_s = roll_s - (self._baseline_roll or 0.0)

        notes: List[str] = []
        if abs(roll_s) > 1.5:
            notes.append("mount roll elevated")
        if abs(yaw_s) > 1.0:
            notes.append("yaw offset from baseline")
        if abs(pitch_s) > 2.0:
            notes.append("horizon pitch shifted")
        if abs(fl.yaw_rate_dps) > 8.0:
            notes.append("unstable ego yaw rate")

        # optional RANSAC VP refinement on strong edges
        gray = to_gray(img)
        gx, gy, mag = sobel_mag(gray)
        lines = edge_lines_from_grad_scale_0(gx, gy, mag)
        vp_r, inl = ransac_vanishing_point(lines, iters=40, thresh=3.0, rng=0)
        if vp_r is not None and len(inl) >= 4:
            yaw_s = 0.5 * yaw_s + 0.5 * ((vp_r[0] / max(img.shape[1], 1) - 0.5) * 70.0)
            notes = list(notes) + ["ransac vp"]
            notes = tuple(notes)

        dt = 0.25
        self.ekf.predict(dt)
        filt = self.ekf.update_rpy(math.radians(roll_s), math.radians(pitch_s), math.radians(yaw_s))
        yaw_s = math.degrees(filt.yaw)
        pitch_s = math.degrees(filt.pitch)
        roll_s = math.degrees(filt.roll)

        conf = float(
            0.35 * hz.strength
            + 0.35 * vp.confidence
            + 0.30 * fl.confidence
        )
        return MountEstimate(
            yaw_deg=yaw_s,
            pitch_deg=pitch_s,
            roll_deg=roll_s,
            horizon_y_norm=hz.y_norm,
            flow_yaw_rate_dps=fl.yaw_rate_dps,
            confidence=min(1.0, conf),
            notes=tuple(notes),
        )
