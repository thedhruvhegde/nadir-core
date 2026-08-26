from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from nadir_core.dashcam.vision.preprocess import sobel_mag, to_gray


