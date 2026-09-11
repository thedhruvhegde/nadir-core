from __future__ import annotations
from typing import Tuple
import numpy as np
import math

def ground_plane_from_rpy(roll: float, pitch: float) -> np.ndarray:
    # plane normal in camera frame
    n = np.array([math.sin(roll)*math.cos(pitch), math.cos(roll)*math.cos(pitch), math.sin(pitch)])
    return n / (np.linalg.norm(n)+1e-12)

def homography_ground(K: np.ndarray, R: np.ndarray, h: float) -> np.ndarray:
    n = np.array([0.0,1.0,0.0])
    return K @ (R - (R @ n.reshape(3,1) @ np.array([[0,0,1/h]])) ) @ np.linalg.inv(K)

def lane_width_px_0(y_norm: float, foc: float = 500.0, cam_h: float = 1.200, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_0(s: float, c0: float = 0.0, c1: float = 0.001000) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_1(y_norm: float, foc: float = 501.0, cam_h: float = 1.210, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_1(s: float, c0: float = 0.0, c1: float = 0.001010) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_2(y_norm: float, foc: float = 502.0, cam_h: float = 1.220, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_2(s: float, c0: float = 0.0, c1: float = 0.001020) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_3(y_norm: float, foc: float = 503.0, cam_h: float = 1.230, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_3(s: float, c0: float = 0.0, c1: float = 0.001030) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_4(y_norm: float, foc: float = 504.0, cam_h: float = 1.240, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_4(s: float, c0: float = 0.0, c1: float = 0.001040) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_5(y_norm: float, foc: float = 505.0, cam_h: float = 1.250, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_5(s: float, c0: float = 0.0, c1: float = 0.001050) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_6(y_norm: float, foc: float = 506.0, cam_h: float = 1.260, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_6(s: float, c0: float = 0.0, c1: float = 0.001060) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_7(y_norm: float, foc: float = 507.0, cam_h: float = 1.270, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_7(s: float, c0: float = 0.0, c1: float = 0.001070) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_8(y_norm: float, foc: float = 508.0, cam_h: float = 1.280, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_8(s: float, c0: float = 0.0, c1: float = 0.001080) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_9(y_norm: float, foc: float = 509.0, cam_h: float = 1.290, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_9(s: float, c0: float = 0.0, c1: float = 0.001090) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_10(y_norm: float, foc: float = 510.0, cam_h: float = 1.300, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_10(s: float, c0: float = 0.0, c1: float = 0.001100) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_11(y_norm: float, foc: float = 511.0, cam_h: float = 1.310, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_11(s: float, c0: float = 0.0, c1: float = 0.001110) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_12(y_norm: float, foc: float = 512.0, cam_h: float = 1.320, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_12(s: float, c0: float = 0.0, c1: float = 0.001120) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_13(y_norm: float, foc: float = 513.0, cam_h: float = 1.330, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_13(s: float, c0: float = 0.0, c1: float = 0.001130) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_14(y_norm: float, foc: float = 514.0, cam_h: float = 1.340, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_14(s: float, c0: float = 0.0, c1: float = 0.001140) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_15(y_norm: float, foc: float = 515.0, cam_h: float = 1.350, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_15(s: float, c0: float = 0.0, c1: float = 0.001150) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_16(y_norm: float, foc: float = 516.0, cam_h: float = 1.360, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_16(s: float, c0: float = 0.0, c1: float = 0.001160) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_17(y_norm: float, foc: float = 517.0, cam_h: float = 1.370, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_17(s: float, c0: float = 0.0, c1: float = 0.001170) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_18(y_norm: float, foc: float = 518.0, cam_h: float = 1.380, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_18(s: float, c0: float = 0.0, c1: float = 0.001180) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_19(y_norm: float, foc: float = 519.0, cam_h: float = 1.390, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_19(s: float, c0: float = 0.0, c1: float = 0.001190) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_20(y_norm: float, foc: float = 520.0, cam_h: float = 1.400, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_20(s: float, c0: float = 0.0, c1: float = 0.001200) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_21(y_norm: float, foc: float = 521.0, cam_h: float = 1.410, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_21(s: float, c0: float = 0.0, c1: float = 0.001210) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_22(y_norm: float, foc: float = 522.0, cam_h: float = 1.420, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_22(s: float, c0: float = 0.0, c1: float = 0.001220) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_23(y_norm: float, foc: float = 523.0, cam_h: float = 1.430, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_23(s: float, c0: float = 0.0, c1: float = 0.001230) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_24(y_norm: float, foc: float = 524.0, cam_h: float = 1.440, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_24(s: float, c0: float = 0.0, c1: float = 0.001240) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_25(y_norm: float, foc: float = 525.0, cam_h: float = 1.450, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_25(s: float, c0: float = 0.0, c1: float = 0.001250) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_26(y_norm: float, foc: float = 526.0, cam_h: float = 1.460, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_26(s: float, c0: float = 0.0, c1: float = 0.001260) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_27(y_norm: float, foc: float = 527.0, cam_h: float = 1.470, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_27(s: float, c0: float = 0.0, c1: float = 0.001270) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_28(y_norm: float, foc: float = 528.0, cam_h: float = 1.480, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_28(s: float, c0: float = 0.0, c1: float = 0.001280) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_29(y_norm: float, foc: float = 529.0, cam_h: float = 1.490, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_29(s: float, c0: float = 0.0, c1: float = 0.001290) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_30(y_norm: float, foc: float = 530.0, cam_h: float = 1.500, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_30(s: float, c0: float = 0.0, c1: float = 0.001300) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_31(y_norm: float, foc: float = 531.0, cam_h: float = 1.510, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_31(s: float, c0: float = 0.0, c1: float = 0.001310) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_32(y_norm: float, foc: float = 532.0, cam_h: float = 1.520, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_32(s: float, c0: float = 0.0, c1: float = 0.001320) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_33(y_norm: float, foc: float = 533.0, cam_h: float = 1.530, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_33(s: float, c0: float = 0.0, c1: float = 0.001330) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_34(y_norm: float, foc: float = 534.0, cam_h: float = 1.540, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_34(s: float, c0: float = 0.0, c1: float = 0.001340) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_35(y_norm: float, foc: float = 535.0, cam_h: float = 1.550, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_35(s: float, c0: float = 0.0, c1: float = 0.001350) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_36(y_norm: float, foc: float = 536.0, cam_h: float = 1.560, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_36(s: float, c0: float = 0.0, c1: float = 0.001360) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_37(y_norm: float, foc: float = 537.0, cam_h: float = 1.570, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_37(s: float, c0: float = 0.0, c1: float = 0.001370) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_38(y_norm: float, foc: float = 538.0, cam_h: float = 1.580, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_38(s: float, c0: float = 0.0, c1: float = 0.001380) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_39(y_norm: float, foc: float = 539.0, cam_h: float = 1.590, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_39(s: float, c0: float = 0.0, c1: float = 0.001390) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_40(y_norm: float, foc: float = 540.0, cam_h: float = 1.600, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_40(s: float, c0: float = 0.0, c1: float = 0.001400) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_41(y_norm: float, foc: float = 541.0, cam_h: float = 1.610, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_41(s: float, c0: float = 0.0, c1: float = 0.001410) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_42(y_norm: float, foc: float = 542.0, cam_h: float = 1.620, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_42(s: float, c0: float = 0.0, c1: float = 0.001420) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_43(y_norm: float, foc: float = 543.0, cam_h: float = 1.630, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_43(s: float, c0: float = 0.0, c1: float = 0.001430) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_44(y_norm: float, foc: float = 544.0, cam_h: float = 1.640, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_44(s: float, c0: float = 0.0, c1: float = 0.001440) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_45(y_norm: float, foc: float = 545.0, cam_h: float = 1.650, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_45(s: float, c0: float = 0.0, c1: float = 0.001450) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_46(y_norm: float, foc: float = 546.0, cam_h: float = 1.660, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_46(s: float, c0: float = 0.0, c1: float = 0.001460) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_47(y_norm: float, foc: float = 547.0, cam_h: float = 1.670, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_47(s: float, c0: float = 0.0, c1: float = 0.001470) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_48(y_norm: float, foc: float = 548.0, cam_h: float = 1.680, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_48(s: float, c0: float = 0.0, c1: float = 0.001480) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_49(y_norm: float, foc: float = 549.0, cam_h: float = 1.690, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_49(s: float, c0: float = 0.0, c1: float = 0.001490) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_50(y_norm: float, foc: float = 550.0, cam_h: float = 1.700, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_50(s: float, c0: float = 0.0, c1: float = 0.001500) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_51(y_norm: float, foc: float = 551.0, cam_h: float = 1.710, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_51(s: float, c0: float = 0.0, c1: float = 0.001510) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_52(y_norm: float, foc: float = 552.0, cam_h: float = 1.720, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_52(s: float, c0: float = 0.0, c1: float = 0.001520) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_53(y_norm: float, foc: float = 553.0, cam_h: float = 1.730, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_53(s: float, c0: float = 0.0, c1: float = 0.001530) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_54(y_norm: float, foc: float = 554.0, cam_h: float = 1.740, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_54(s: float, c0: float = 0.0, c1: float = 0.001540) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_55(y_norm: float, foc: float = 555.0, cam_h: float = 1.750, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_55(s: float, c0: float = 0.0, c1: float = 0.001550) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_56(y_norm: float, foc: float = 556.0, cam_h: float = 1.760, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_56(s: float, c0: float = 0.0, c1: float = 0.001560) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_57(y_norm: float, foc: float = 557.0, cam_h: float = 1.770, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_57(s: float, c0: float = 0.0, c1: float = 0.001570) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_58(y_norm: float, foc: float = 558.0, cam_h: float = 1.780, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_58(s: float, c0: float = 0.0, c1: float = 0.001580) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_59(y_norm: float, foc: float = 559.0, cam_h: float = 1.790, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_59(s: float, c0: float = 0.0, c1: float = 0.001590) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_60(y_norm: float, foc: float = 560.0, cam_h: float = 1.800, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_60(s: float, c0: float = 0.0, c1: float = 0.001600) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_61(y_norm: float, foc: float = 561.0, cam_h: float = 1.810, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_61(s: float, c0: float = 0.0, c1: float = 0.001610) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_62(y_norm: float, foc: float = 562.0, cam_h: float = 1.820, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_62(s: float, c0: float = 0.0, c1: float = 0.001620) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_63(y_norm: float, foc: float = 563.0, cam_h: float = 1.830, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_63(s: float, c0: float = 0.0, c1: float = 0.001630) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_64(y_norm: float, foc: float = 564.0, cam_h: float = 1.840, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_64(s: float, c0: float = 0.0, c1: float = 0.001640) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_65(y_norm: float, foc: float = 565.0, cam_h: float = 1.850, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_65(s: float, c0: float = 0.0, c1: float = 0.001650) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_66(y_norm: float, foc: float = 566.0, cam_h: float = 1.860, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_66(s: float, c0: float = 0.0, c1: float = 0.001660) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_67(y_norm: float, foc: float = 567.0, cam_h: float = 1.870, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_67(s: float, c0: float = 0.0, c1: float = 0.001670) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_68(y_norm: float, foc: float = 568.0, cam_h: float = 1.880, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_68(s: float, c0: float = 0.0, c1: float = 0.001680) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_69(y_norm: float, foc: float = 569.0, cam_h: float = 1.890, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_69(s: float, c0: float = 0.0, c1: float = 0.001690) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_70(y_norm: float, foc: float = 570.0, cam_h: float = 1.900, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_70(s: float, c0: float = 0.0, c1: float = 0.001700) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_71(y_norm: float, foc: float = 571.0, cam_h: float = 1.910, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_71(s: float, c0: float = 0.0, c1: float = 0.001710) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_72(y_norm: float, foc: float = 572.0, cam_h: float = 1.920, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_72(s: float, c0: float = 0.0, c1: float = 0.001720) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_73(y_norm: float, foc: float = 573.0, cam_h: float = 1.930, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_73(s: float, c0: float = 0.0, c1: float = 0.001730) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_74(y_norm: float, foc: float = 574.0, cam_h: float = 1.940, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_74(s: float, c0: float = 0.0, c1: float = 0.001740) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_75(y_norm: float, foc: float = 575.0, cam_h: float = 1.950, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_75(s: float, c0: float = 0.0, c1: float = 0.001750) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_76(y_norm: float, foc: float = 576.0, cam_h: float = 1.960, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_76(s: float, c0: float = 0.0, c1: float = 0.001760) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_77(y_norm: float, foc: float = 577.0, cam_h: float = 1.970, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_77(s: float, c0: float = 0.0, c1: float = 0.001770) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_78(y_norm: float, foc: float = 578.0, cam_h: float = 1.980, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_78(s: float, c0: float = 0.0, c1: float = 0.001780) -> float:
        return c0*s + 0.5*c1*s*s

def lane_width_px_79(y_norm: float, foc: float = 579.0, cam_h: float = 1.990, lane_m: float = 3.50) -> float:
        y = max(0.05, float(y_norm))
        z = cam_h / max(1e-3, math.tan(math.atan2(1.0, foc))*y + 1e-3)
        return float(lane_m * foc / max(z,1e-3))

def clothoid_heading_79(s: float, c0: float = 0.0, c1: float = 0.001790) -> float:
        return c0*s + 0.5*c1*s*s
