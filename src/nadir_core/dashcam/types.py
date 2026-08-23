from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional, Tuple

import numpy as np


class SourceKind(str, Enum):
    FOLDER = "folder"
    VIOFO = "viofo"
    BLACKVUE = "blackvue"
    RTSP = "rtsp"
    SYNTHETIC = "synthetic"


@dataclass
class FramePacket:
    image: np.ndarray
