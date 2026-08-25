from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from nadir_core.dashcam.vision.preprocess import to_gray


@dataclass(frozen=True)
class FlowResult:
    yaw_rate_dps: float
    mean_dx: float
    confidence: float


class FlowTracker:
    def __init__(self, grid: int = 12) -> None:
        self.grid = grid
        self._prev: Optional[np.ndarray] = None
        self._prev_t: Optional[float] = None

    def reset(self) -> None:
        self._prev = None
        self._prev_t = None

    def update(self, image: np.ndarray, timestamp_s: float) -> FlowResult:
        gray = to_gray(image)
        h, w = gray.shape
