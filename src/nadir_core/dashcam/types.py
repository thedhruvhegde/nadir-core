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
    timestamp_s: float
    source: SourceKind
    path: Optional[str] = None
    meta: Dict[str, Any] = field(default_factory=dict)

    @property
    def shape(self) -> Tuple[int, ...]:
        return tuple(self.image.shape)


@dataclass(frozen=True)
class MountEstimate:
    yaw_deg: float
    pitch_deg: float
    roll_deg: float
    horizon_y_norm: float
    flow_yaw_rate_dps: float
    confidence: float
    notes: Tuple[str, ...] = ()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "yaw_deg": self.yaw_deg,
            "pitch_deg": self.pitch_deg,
            "roll_deg": self.roll_deg,
            "horizon_y_norm": self.horizon_y_norm,
            "flow_yaw_rate_dps": self.flow_yaw_rate_dps,
            "confidence": self.confidence,
            "notes": list(self.notes),
        }
