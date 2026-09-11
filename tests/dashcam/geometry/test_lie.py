
import numpy as np
from nadir_core.dashcam.geometry.lie_so3 import so3_exp, so3_log, rpy_to_rot, rot_to_rpy, geodesic_distance

def test_exp_log_roundtrip():
    w = np.array([0.1, -0.2, 0.05])
    R = so3_exp(w)
    w2 = so3_log(R)
    assert np.linalg.norm(w-w2) < 1e-8

def test_rpy():
    R = rpy_to_rot(0.05, -0.02, 0.1)
    r,p,y = rot_to_rpy(R)
    assert abs(r-0.05)<1e-8 and abs(y-0.1)<1e-8

def test_geodesic_zero():
    R = so3_exp([0.01,0.02,0.03])
    assert geodesic_distance(R,R) < 1e-10
