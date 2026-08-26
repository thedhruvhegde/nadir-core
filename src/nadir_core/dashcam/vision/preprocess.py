from __future__ import annotations

from typing import Tuple

import numpy as np


def to_gray(image: np.ndarray) -> np.ndarray:
    if image.ndim == 2:
        return image.astype(np.float32)
    # BT.601
    r = image[..., 2].astype(np.float32)
    g = image[..., 1].astype(np.float32)
    b = image[..., 0].astype(np.float32)
    return 0.299 * r + 0.587 * g + 0.114 * b


def resize_max(image: np.ndarray, max_width: int = 960) -> np.ndarray:
    h, w = image.shape[:2]
    if w <= max_width:
        return image
    scale = max_width / float(w)
    new_w = max_width
    new_h = max(1, int(round(h * scale)))
    yy = (np.linspace(0, h - 1, new_h)).astype(np.int32)
    xx = (np.linspace(0, w - 1, new_w)).astype(np.int32)
    return image[np.ix_(yy, xx)]


def sobel_mag(gray: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    gx = np.zeros_like(gray)
    gy = np.zeros_like(gray)
    gx[:, 1:-1] = gray[:, 2:] - gray[:, :-2]
    gy[1:-1, :] = gray[2:, :] - gray[:-2, :]
    mag = np.hypot(gx, gy)
    return gx, gy, mag
