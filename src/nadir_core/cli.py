"""CLI entrypoints for NADIR Open Core."""

from __future__ import annotations

import argparse
import json
import math
import sys
from typing import List, Optional

from nadir_core.scoring import PulseScoringOptions, SensorReadings, score_pulse


def _rot_yaw(deg: float) -> List[float]:
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return [c, -s, 0.0, s, c, 0.0, 0.0, 0.0, 1.0]


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Score ADAS residual drift with NADIR Pulse (Open Core)")
    parser.add_argument("--vehicle-id", default="demo-vehicle")
    parser.add_argument("--yaw-deg", type=float, default=0.35, help="Camera yaw residual in degrees")
    parser.add_argument("--json", action="store_true", help="Print full JSON result")
    args = parser.parse_args(argv)

    sensors = SensorReadings(
        camera_rotation_matrix=_rot_yaw(args.yaw_deg),
        radar_range_bias_m=0.0004 * abs(args.yaw_deg),
        radar_azimuth_bias_deg=0.08 * abs(args.yaw_deg),
        lidar_registration_error_m=0.0003 * abs(args.yaw_deg),
    )
    result = score_pulse(
        vehicle_id=args.vehicle_id,
        sensors=sensors,
        options=PulseScoringOptions(enable_latency_profiler=False),
    )
    if args.json:
        print(json.dumps(result.to_dict() if hasattr(result, "to_dict") else {
            "tier": str(result.tier),
            "mahal_distance": getattr(result, "mahal_distance", None),
            "health_score": getattr(result, "health_score", None),
        }, indent=2, default=str))
    else:
        print(f"vehicle={args.vehicle_id} yaw={args.yaw_deg}° → tier={result.tier}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
