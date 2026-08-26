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
    y = int(np.argmax(band)) if band.max() > 0 else h // 2
    # roll from gradient orientation near horizon band
    ys = slice(max(0, y - 4), min(h, y + 5))
    gx, gy, _ = sobel_mag(gray)
    patch_gx = gx[ys, :]
    patch_gy = gy[ys, :]
    angles = np.arctan2(patch_gy, patch_gx + 1e-6)
    # horizontal edges ~ 0 or pi; roll tilts them
    roll = float(np.rad2deg(np.median(angles)))
    # map to small roll around 0
    while roll > 90:
        roll -= 180
    while roll < -90:
        roll += 180
    strength = float(band.max() / (row_energy.mean() + 1e-6))
    return HorizonResult(y_norm=y / float(h), roll_deg=0.15 * roll, strength=min(strength / 5.0, 1.0))
