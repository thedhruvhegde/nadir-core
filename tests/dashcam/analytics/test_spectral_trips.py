
import numpy as np
from nadir_core.dashcam.analytics.spectral import welch_psd, vibration_features_0
from nadir_core.dashcam.analytics.trips import segment_trips

def test_welch():
    t = np.linspace(0, 8, 128)
    x = np.sin(2*np.pi*1.5*t)
    f, p = welch_psd(x, fs=16.0)
    assert f.size == p.size

def test_segments():
    speed = np.array([0,0,2,2,2,2,0,0,3,3,3,3,3,0])
    yaw = np.linspace(0, 0.2, len(speed))
    roll = np.zeros_like(speed)
    segs = segment_trips(speed, yaw, roll, min_len=3)
    assert len(segs) >= 1
