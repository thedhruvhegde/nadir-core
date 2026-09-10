"""Smoke tests for NADIR Open Core scoring."""

from __future__ import annotations

import math

from nadir_core.scoring import DriftTier, PulseScoringOptions, SensorReadings, score_pulse


def _rot(yaw: float) -> list[float]:
    r = math.radians(yaw)
    c, s = math.cos(r), math.sin(r)
    return [c, -s, 0.0, s, c, 0.0, 0.0, 0.0, 1.0]


def test_nominal_small_yaw() -> None:
    result = score_pulse(
        vehicle_id="t1",
        sensors=SensorReadings(camera_rotation_matrix=_rot(0.05)),
        options=PulseScoringOptions(enable_latency_profiler=False),
    )
    assert result.tier is DriftTier.NOMINAL


def test_caution_or_critical_on_large_yaw() -> None:
    result = score_pulse(
        vehicle_id="t2",
        sensors=SensorReadings(camera_rotation_matrix=_rot(0.8)),
        options=PulseScoringOptions(enable_latency_profiler=False),
    )
    assert result.tier in (DriftTier.CAUTION, DriftTier.CRITICAL)
