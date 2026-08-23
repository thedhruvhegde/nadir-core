from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class DashcamConfig:
    vehicle_id: str = "dashcam-vehicle"
