"""Minimal Pulse scoring demo for NADIR Open Core."""

from __future__ import annotations

import math

from nadir_core import SensorReadings, score_pulse
from nadir_core.scoring import PulseScoringOptions


def rot_yaw(deg: float) -> list[float]:
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return [c, -s, 0.0, s, c, 0.0, 0.0, 0.0, 1.0]


def main() -> None:
    for yaw in (0.05, 0.25, 0.45, 0.9):
        result = score_pulse(
            vehicle_id="open-core-demo",
            sensors=SensorReadings(
                camera_rotation_matrix=rot_yaw(yaw),
                radar_range_bias_m=0.0005 * abs(yaw),
                radar_azimuth_bias_deg=0.1 * abs(yaw),
            ),
            options=PulseScoringOptions(enable_latency_profiler=False),
        )
        print(f"yaw={yaw:4.2f}°  tier={result.tier}  mahal={result.mahal_distance:.3f}")


if __name__ == "__main__":
    main()
