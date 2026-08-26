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
