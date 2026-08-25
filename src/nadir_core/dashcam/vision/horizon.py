from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np

from nadir_core.dashcam.vision.preprocess import sobel_mag, to_gray

