from __future__ import annotations

from typing import Tuple

import numpy as np


def to_gray(image: np.ndarray) -> np.ndarray:
    if image.ndim == 2:
