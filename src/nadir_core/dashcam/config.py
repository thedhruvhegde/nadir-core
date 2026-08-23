from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class DashcamConfig:
    vehicle_id: str = "dashcam-vehicle"
    sample_hz: float = 4.0
    max_width: int = 960
    store_path: str = "out/dashcam_health.jsonl"
    api_url: Optional[str] = None
    api_token_env: str = "NADIR_API_TOKEN"
    viofo_host: Optional[str] = None
    blackvue_host: Optional[str] = "10.99.77.1"
    rtsp_url: Optional[str] = None
    folder: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_env(cls, **overrides: Any) -> "DashcamConfig":
        cfg = cls(
            vehicle_id=os.environ.get("NADIR_VEHICLE_ID", "dashcam-vehicle"),
            api_url=os.environ.get("NADIR_API_URL") or None,
            store_path=os.environ.get("NADIR_DASHCAM_STORE", "out/dashcam_health.jsonl"),
            viofo_host=os.environ.get("NADIR_VIOFO_HOST"),
            blackvue_host=os.environ.get("NADIR_BLACKVUE_HOST", "10.99.77.1"),
            rtsp_url=os.environ.get("NADIR_RTSP_URL"),
