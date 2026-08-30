from __future__ import annotations

import numpy as np

from nadir_core.dashcam.sources.synthetic import make_road_frame
from nadir_core.dashcam.vision.horizon import estimate_horizon
from nadir_core.dashcam.vision.vanishing import estimate_vanishing_yaw


def test_horizon_finds_band():
    img = make_road_frame(horizon_y=0.4, roll_deg=0.0, seed=1)
    hz = estimate_horizon(img)
    assert 0.25 < hz.y_norm < 0.6


def test_vanishing_shifts_with_yaw_px():
    a = make_road_frame(yaw_shift_px=0.0, seed=2)
    b = make_road_frame(yaw_shift_px=30.0, seed=2)
    ya = estimate_vanishing_yaw(a).yaw_deg
    yb = estimate_vanishing_yaw(b).yaw_deg
    assert yb > ya


def test_clamp01():
    from nadir_core.dashcam.vision.preprocess import clamp01

    assert clamp01(-1) == 0.0
    assert clamp01(2) == 1.0
    assert clamp01(0.3) == 0.3
