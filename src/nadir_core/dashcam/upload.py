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
        "tier": sample.tier.value if hasattr(sample.tier, "value") else str(sample.tier),
        "mahal": sample.mahal,
        "health_score": sample.health_score,
        "estimate": sample.estimate.as_dict(),
        "explanation": sample.explanation,
    }


def upload_sample(
    api_url: str,
    vehicle_id: str,
    sample: HealthSample,
    *,
    token: Optional[str] = None,
    timeout_s: float = 10.0,
    session: Optional[object] = None,
) -> Dict[str, Any]:
    if requests is None:
