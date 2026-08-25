from __future__ import annotations

from typing import List

from nadir_core.dashcam.types import MountEstimate
from nadir_core.scoring.types import DriftTier


def explain_mount(estimate: MountEstimate, tier: DriftTier) -> str:
    parts: List[str] = []
    parts.append(f"tier={tier.value}")
    parts.append(f"yaw={estimate.yaw_deg:.2f}° pitch={estimate.pitch_deg:.2f}° roll={estimate.roll_deg:.2f}°")
    if estimate.notes:
        parts.append("signals: " + "; ".join(estimate.notes))
    else:
        parts.append("signals: stable geometry vs local baseline")
    parts.append(
        "vision mount health only — not a multi-sensor ADAS calibration certificate"
    )
    return " | ".join(parts)
