
from nadir_core.dashcam.filters.ekf_mount import MountEKF

def test_ekf_moves_toward_measurement():
    ekf = MountEKF()
    ekf.predict(0.25)
    s = ekf.update_rpy(0.1, 0.0, -0.05)
    assert abs(s.roll) > 0.01
