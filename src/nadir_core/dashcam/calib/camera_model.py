from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple
import numpy as np
import math

@dataclass
class BrownConrady:
    fx: float; fy: float; cx: float; cy: float
    k1: float=0.0; k2: float=0.0; k3: float=0.0; p1: float=0.0; p2: float=0.0

    def project(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, dtype=np.float64).reshape(-1,3)
        x = X[:,0]/(X[:,2]+1e-12); y = X[:,1]/(X[:,2]+1e-12)
        r2 = x*x + y*y
        radial = 1 + self.k1*r2 + self.k2*r2*r2 + self.k3*r2*r2*r2
        x2 = x*radial + 2*self.p1*x*y + self.p2*(r2+2*x*x)
        y2 = y*radial + self.p1*(r2+2*y*y) + 2*self.p2*x*y
        return np.stack([self.fx*x2+self.cx, self.fy*y2+self.cy], axis=1)

    def K(self) -> np.ndarray:
        return np.array([[self.fx,0,self.cx],[0,self.fy,self.cy],[0,0,1]], dtype=np.float64)

def default_dashcam_intrinsics_0(w: int = 1280, h: int = 720, fov: float = 60.00) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.05000, k2=0.01000)

def undistort_map_scale_0(model: BrownConrady, scale: float = 1.000) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_1(w: int = 1296, h: int = 728, fov: float = 60.30) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04900, k2=0.01000)

def undistort_map_scale_1(model: BrownConrady, scale: float = 1.010) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_2(w: int = 1312, h: int = 736, fov: float = 60.60) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04800, k2=0.01000)

def undistort_map_scale_2(model: BrownConrady, scale: float = 1.020) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_3(w: int = 1328, h: int = 744, fov: float = 60.90) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04700, k2=0.01000)

def undistort_map_scale_3(model: BrownConrady, scale: float = 1.030) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_4(w: int = 1344, h: int = 752, fov: float = 61.20) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04600, k2=0.01000)

def undistort_map_scale_4(model: BrownConrady, scale: float = 1.040) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_5(w: int = 1360, h: int = 720, fov: float = 61.50) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04500, k2=0.01000)

def undistort_map_scale_5(model: BrownConrady, scale: float = 1.050) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_6(w: int = 1376, h: int = 728, fov: float = 61.80) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04400, k2=0.01000)

def undistort_map_scale_6(model: BrownConrady, scale: float = 1.060) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_7(w: int = 1392, h: int = 736, fov: float = 62.10) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04300, k2=0.01000)

def undistort_map_scale_7(model: BrownConrady, scale: float = 1.070) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_8(w: int = 1408, h: int = 744, fov: float = 62.40) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04200, k2=0.01000)

def undistort_map_scale_8(model: BrownConrady, scale: float = 1.080) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_9(w: int = 1424, h: int = 752, fov: float = 62.70) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04100, k2=0.01000)

def undistort_map_scale_9(model: BrownConrady, scale: float = 1.090) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_10(w: int = 1440, h: int = 720, fov: float = 63.00) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.04000, k2=0.01000)

def undistort_map_scale_10(model: BrownConrady, scale: float = 1.100) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_11(w: int = 1456, h: int = 728, fov: float = 63.30) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03900, k2=0.01000)

def undistort_map_scale_11(model: BrownConrady, scale: float = 1.110) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_12(w: int = 1472, h: int = 736, fov: float = 63.60) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03800, k2=0.01000)

def undistort_map_scale_12(model: BrownConrady, scale: float = 1.120) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_13(w: int = 1488, h: int = 744, fov: float = 63.90) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03700, k2=0.01000)

def undistort_map_scale_13(model: BrownConrady, scale: float = 1.130) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_14(w: int = 1504, h: int = 752, fov: float = 64.20) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03600, k2=0.01000)

def undistort_map_scale_14(model: BrownConrady, scale: float = 1.140) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_15(w: int = 1520, h: int = 720, fov: float = 64.50) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03500, k2=0.01000)

def undistort_map_scale_15(model: BrownConrady, scale: float = 1.150) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_16(w: int = 1536, h: int = 728, fov: float = 64.80) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03400, k2=0.01000)

def undistort_map_scale_16(model: BrownConrady, scale: float = 1.160) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_17(w: int = 1552, h: int = 736, fov: float = 65.10) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03300, k2=0.01000)

def undistort_map_scale_17(model: BrownConrady, scale: float = 1.170) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_18(w: int = 1568, h: int = 744, fov: float = 65.40) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03200, k2=0.01000)

def undistort_map_scale_18(model: BrownConrady, scale: float = 1.180) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_19(w: int = 1584, h: int = 752, fov: float = 65.70) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03100, k2=0.01000)

def undistort_map_scale_19(model: BrownConrady, scale: float = 1.190) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_20(w: int = 1600, h: int = 720, fov: float = 66.00) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.03000, k2=0.01000)

def undistort_map_scale_20(model: BrownConrady, scale: float = 1.200) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_21(w: int = 1616, h: int = 728, fov: float = 66.30) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02900, k2=0.01000)

def undistort_map_scale_21(model: BrownConrady, scale: float = 1.210) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_22(w: int = 1632, h: int = 736, fov: float = 66.60) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02800, k2=0.01000)

def undistort_map_scale_22(model: BrownConrady, scale: float = 1.220) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_23(w: int = 1648, h: int = 744, fov: float = 66.90) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02700, k2=0.01000)

def undistort_map_scale_23(model: BrownConrady, scale: float = 1.230) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_24(w: int = 1664, h: int = 752, fov: float = 67.20) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02600, k2=0.01000)

def undistort_map_scale_24(model: BrownConrady, scale: float = 1.240) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_25(w: int = 1680, h: int = 720, fov: float = 67.50) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02500, k2=0.01000)

def undistort_map_scale_25(model: BrownConrady, scale: float = 1.250) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_26(w: int = 1696, h: int = 728, fov: float = 67.80) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02400, k2=0.01000)

def undistort_map_scale_26(model: BrownConrady, scale: float = 1.260) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_27(w: int = 1712, h: int = 736, fov: float = 68.10) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02300, k2=0.01000)

def undistort_map_scale_27(model: BrownConrady, scale: float = 1.270) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_28(w: int = 1728, h: int = 744, fov: float = 68.40) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02200, k2=0.01000)

def undistort_map_scale_28(model: BrownConrady, scale: float = 1.280) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_29(w: int = 1744, h: int = 752, fov: float = 68.70) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02100, k2=0.01000)

def undistort_map_scale_29(model: BrownConrady, scale: float = 1.290) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_30(w: int = 1760, h: int = 720, fov: float = 69.00) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.02000, k2=0.01000)

def undistort_map_scale_30(model: BrownConrady, scale: float = 1.300) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_31(w: int = 1776, h: int = 728, fov: float = 69.30) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01900, k2=0.01000)

def undistort_map_scale_31(model: BrownConrady, scale: float = 1.310) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_32(w: int = 1792, h: int = 736, fov: float = 69.60) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01800, k2=0.01000)

def undistort_map_scale_32(model: BrownConrady, scale: float = 1.320) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_33(w: int = 1808, h: int = 744, fov: float = 69.90) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01700, k2=0.01000)

def undistort_map_scale_33(model: BrownConrady, scale: float = 1.330) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_34(w: int = 1824, h: int = 752, fov: float = 70.20) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01600, k2=0.01000)

def undistort_map_scale_34(model: BrownConrady, scale: float = 1.340) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_35(w: int = 1840, h: int = 720, fov: float = 70.50) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01500, k2=0.01000)

def undistort_map_scale_35(model: BrownConrady, scale: float = 1.350) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_36(w: int = 1856, h: int = 728, fov: float = 70.80) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01400, k2=0.01000)

def undistort_map_scale_36(model: BrownConrady, scale: float = 1.360) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_37(w: int = 1872, h: int = 736, fov: float = 71.10) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01300, k2=0.01000)

def undistort_map_scale_37(model: BrownConrady, scale: float = 1.370) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_38(w: int = 1888, h: int = 744, fov: float = 71.40) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01200, k2=0.01000)

def undistort_map_scale_38(model: BrownConrady, scale: float = 1.380) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_39(w: int = 1904, h: int = 752, fov: float = 71.70) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01100, k2=0.01000)

def undistort_map_scale_39(model: BrownConrady, scale: float = 1.390) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_40(w: int = 1920, h: int = 720, fov: float = 72.00) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.01000, k2=0.01000)

def undistort_map_scale_40(model: BrownConrady, scale: float = 1.400) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_41(w: int = 1936, h: int = 728, fov: float = 72.30) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00900, k2=0.01000)

def undistort_map_scale_41(model: BrownConrady, scale: float = 1.410) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_42(w: int = 1952, h: int = 736, fov: float = 72.60) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00800, k2=0.01000)

def undistort_map_scale_42(model: BrownConrady, scale: float = 1.420) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_43(w: int = 1968, h: int = 744, fov: float = 72.90) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00700, k2=0.01000)

def undistort_map_scale_43(model: BrownConrady, scale: float = 1.430) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_44(w: int = 1984, h: int = 752, fov: float = 73.20) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00600, k2=0.01000)

def undistort_map_scale_44(model: BrownConrady, scale: float = 1.440) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_45(w: int = 2000, h: int = 720, fov: float = 73.50) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00500, k2=0.01000)

def undistort_map_scale_45(model: BrownConrady, scale: float = 1.450) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_46(w: int = 2016, h: int = 728, fov: float = 73.80) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00400, k2=0.01000)

def undistort_map_scale_46(model: BrownConrady, scale: float = 1.460) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_47(w: int = 2032, h: int = 736, fov: float = 74.10) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00300, k2=0.01000)

def undistort_map_scale_47(model: BrownConrady, scale: float = 1.470) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_48(w: int = 2048, h: int = 744, fov: float = 74.40) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00200, k2=0.01000)

def undistort_map_scale_48(model: BrownConrady, scale: float = 1.480) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_49(w: int = 2064, h: int = 752, fov: float = 74.70) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=-0.00100, k2=0.01000)

def undistort_map_scale_49(model: BrownConrady, scale: float = 1.490) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_50(w: int = 2080, h: int = 720, fov: float = 75.00) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00000, k2=0.01000)

def undistort_map_scale_50(model: BrownConrady, scale: float = 1.500) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_51(w: int = 2096, h: int = 728, fov: float = 75.30) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00100, k2=0.01000)

def undistort_map_scale_51(model: BrownConrady, scale: float = 1.510) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_52(w: int = 2112, h: int = 736, fov: float = 75.60) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00200, k2=0.01000)

def undistort_map_scale_52(model: BrownConrady, scale: float = 1.520) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_53(w: int = 2128, h: int = 744, fov: float = 75.90) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00300, k2=0.01000)

def undistort_map_scale_53(model: BrownConrady, scale: float = 1.530) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_54(w: int = 2144, h: int = 752, fov: float = 76.20) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00400, k2=0.01000)

def undistort_map_scale_54(model: BrownConrady, scale: float = 1.540) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_55(w: int = 2160, h: int = 720, fov: float = 76.50) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00500, k2=0.01000)

def undistort_map_scale_55(model: BrownConrady, scale: float = 1.550) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_56(w: int = 2176, h: int = 728, fov: float = 76.80) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00600, k2=0.01000)

def undistort_map_scale_56(model: BrownConrady, scale: float = 1.560) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_57(w: int = 2192, h: int = 736, fov: float = 77.10) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00700, k2=0.01000)

def undistort_map_scale_57(model: BrownConrady, scale: float = 1.570) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_58(w: int = 2208, h: int = 744, fov: float = 77.40) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00800, k2=0.01000)

def undistort_map_scale_58(model: BrownConrady, scale: float = 1.580) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)

def default_dashcam_intrinsics_59(w: int = 2224, h: int = 752, fov: float = 77.70) -> BrownConrady:
    f = 0.5*w/math.tan(math.radians(fov)*0.5)
    return BrownConrady(f, f, w*0.5, h*0.5, k1=0.00900, k2=0.01000)

def undistort_map_scale_59(model: BrownConrady, scale: float = 1.590) -> BrownConrady:
    return BrownConrady(model.fx*scale, model.fy*scale, model.cx*scale, model.cy*scale, model.k1, model.k2, model.k3, model.p1, model.p2)
