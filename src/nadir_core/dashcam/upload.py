from __future__ import annotations

from typing import Any, Dict, Optional

from nadir_core.dashcam.health import HealthSample

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # type: ignore


def build_upload_payload(vehicle_id: str, sample: HealthSample) -> Dict[str, Any]:
    return {
        "vehicle_id": vehicle_id,
        "source": "dashcam_open_core",
        "claim_boundary": "vision_mount_health_only",
        "timestamp_s": sample.timestamp_s,
