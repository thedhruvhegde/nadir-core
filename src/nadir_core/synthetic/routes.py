"""Simulated route progression for synthetic telemetry."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class RouteTemplate:
    """Starting route context for a synthetic drive."""

    route_id: str
    segment_id: str
    latitude_deg: float
    longitude_deg: float
    heading_deg: float
    odometer_km: float
    road_class: str
    speed_limit_mps: float


DEFAULT_HIGHWAY_ROUTE = RouteTemplate(
    route_id="CA-101-north-commute",
    segment_id="seg-palo-alto-08",
    latitude_deg=37.4419,
    longitude_deg=-122.1430,
    heading_deg=352.0,
    odometer_km=18420.3,
    road_class="controlled-access highway",
    speed_limit_mps=29.0,
)


def advance_route(
    template: RouteTemplate,
    *,
    frame_index: int,
    dt_s: float,
    speed_mps: float,
) -> Dict[str, object]:
    """
    Advance lat/lon/heading/odometer along a gentle highway arc.

    Uses a constant-speed approximation suitable for 10 Hz telemetry frames.
    """
    distance_m = speed_mps * dt_s * max(frame_index, 0)
    distance_km = distance_m / 1000.0
    heading_rad = math.radians(template.heading_deg)

    # Approximate local ENU displacement (adequate for demo synthetic data).
    dlat = (distance_m * math.cos(heading_rad)) / 111_320.0
    dlon = (distance_m * math.sin(heading_rad)) / (
        111_320.0 * math.cos(math.radians(template.latitude_deg))
    )

    heading = (template.heading_deg + frame_index * 0.02) % 360.0
    segment_num = 8 + (frame_index // 200)

    return {
        "route_id": template.route_id,
        "segment_id": f"{template.segment_id}-{segment_num:02d}",
        "odometer_km": round(template.odometer_km + distance_km, 4),
        "latitude_deg": round(template.latitude_deg + dlat, 6),
        "longitude_deg": round(template.longitude_deg + dlon, 6),
        "heading_deg": round(heading, 2),
        "road_class": template.road_class,
        "speed_limit_mps": template.speed_limit_mps,
    }
