from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np

from nadir_core.dashcam.vision.preprocess import sobel_mag, to_gray


@dataclass(frozen=True)
class HorizonResult:
    y_norm: float
    roll_deg: float
    strength: float


def estimate_horizon(image: np.ndarray) -> HorizonResult:
    gray = to_gray(image)
    h, w = gray.shape
    _, _, mag = sobel_mag(gray)
    # row energy of horizontal edges
    row_energy = mag.mean(axis=1)
    # prefer middle band
    band = np.zeros_like(row_energy)
    lo, hi = int(0.25 * h), int(0.75 * h)
    band[lo:hi] = row_energy[lo:hi]
