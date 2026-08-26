from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from nadir_core.dashcam.vision.preprocess import sobel_mag, to_gray


@dataclass(frozen=True)
class VanishingResult:
    yaw_deg: float
    x_norm: float
    confidence: float


def estimate_vanishing_yaw(image: np.ndarray) -> VanishingResult:
    """Lane-ish vertical structure centroid as yaw proxy."""
    gray = to_gray(image)
    h, w = gray.shape
    gx, gy, mag = sobel_mag(gray)
    # emphasize near-vertical edges in lower half
    mask = np.abs(gx) > (np.abs(gy) + 1.0)
    mask[: h // 2, :] = False
    weights = mag * mask
    if weights.sum() < 1e-3:
        return VanishingResult(yaw_deg=0.0, x_norm=0.5, confidence=0.1)
    xs = np.arange(w, dtype=np.float32)
    col = weights.sum(axis=0)
    x = float(np.sum(xs * col) / (col.sum() + 1e-6))
    x_norm = x / float(w)
    # map deviation from center to yaw degrees (soft FOV ~70deg)
    yaw = (x_norm - 0.5) * 70.0
    conf = float(min(1.0, weights.sum() / (h * w * 5.0)))
    return VanishingResult(yaw_deg=yaw, x_norm=x_norm, confidence=conf)
