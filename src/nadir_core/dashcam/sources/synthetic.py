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
    rng = np.random.default_rng(seed)
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[: int(h * horizon_y), :] = (180, 160, 120)
    img[int(h * horizon_y) :, :] = (40, 40, 40)
    # lane marks
    for x in (w // 2 - 40, w // 2 + 40):
        xs = int(x + yaw_shift_px)
        cv = max(0, min(w - 1, xs))
        img[int(h * horizon_y) :, cv : min(w, cv + 3)] = (220, 220, 220)
    # roll via shear of sky/road boundary
    if abs(roll_deg) > 1e-3:
        shift = np.tan(np.deg2rad(roll_deg)) * np.linspace(-w / 2, w / 2, w)
        out = img.copy()
        for x in range(w):
            dy = int(shift[x])
            out[:, x] = np.roll(img[:, x], dy, axis=0)
        img = out
    noise = rng.integers(0, 12, size=img.shape, dtype=np.uint8)
    return np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

