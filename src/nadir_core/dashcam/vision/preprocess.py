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
