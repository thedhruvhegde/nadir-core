from __future__ import annotations
from typing import Optional, Tuple
import numpy as np

def normalize_points(pts: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    pts = np.asarray(pts, dtype=np.float64).reshape(-1, 2)
    c = pts.mean(axis=0)
    d = np.linalg.norm(pts - c, axis=1).mean() + 1e-12
    s = math.sqrt(2.0) / d
    T = np.array([[s, 0, -s*c[0]], [0, s, -s*c[1]], [0, 0, 1]], dtype=np.float64)
    ph = np.c_[pts, np.ones(len(pts))]
    return (T @ ph.T).T[:, :2], T

import math

def dlt_homography(src: np.ndarray, dst: np.ndarray) -> np.ndarray:
    src_n, T1 = normalize_points(src)
    dst_n, T2 = normalize_points(dst)
    A = []
    for (x, y), (u, v) in zip(src_n, dst_n):
        A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
        A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])
    A = np.asarray(A, dtype=np.float64)
    _, _, vh = np.linalg.svd(A)
    Hn = vh[-1].reshape(3, 3)
    H = np.linalg.inv(T2) @ Hn @ T1
    return H / (H[2, 2] + 1e-12)

def ransac_homography(src: np.ndarray, dst: np.ndarray, iters: int = 200, thresh: float = 3.0, rng=None):
    rng = np.random.default_rng(rng)
    src = np.asarray(src, dtype=np.float64).reshape(-1, 2)
    dst = np.asarray(dst, dtype=np.float64).reshape(-1, 2)
    n = len(src)
    best_H, best_inl = None, []
    if n < 4:
        return None, []
    for _ in range(iters):
        idx = rng.choice(n, 4, replace=False)
        H = dlt_homography(src[idx], dst[idx])
        inl = []
        for i in range(n):
            p = np.array([src[i,0], src[i,1], 1.0])
            q = H @ p
            if abs(q[2]) < 1e-10: continue
            q = q[:2]/q[2]
            if np.linalg.norm(q - dst[i]) < thresh:
                inl.append(i)
        if len(inl) > len(best_inl):
            best_inl = inl
            best_H = H
    if best_H is not None and len(best_inl) >= 4:
        best_H = dlt_homography(src[best_inl], dst[best_inl])
    return best_H, best_inl

def homography_yaw_pitch(H: np.ndarray, K: np.ndarray) -> Tuple[float, float]:
    # decompose approx using infinite homography intuition
    Kinv = np.linalg.inv(K)
    Rapprox = Kinv @ H @ K
    # orthonormalize
    u, _, vh = np.linalg.svd(Rapprox)
    R = u @ vh
    if np.linalg.det(R) < 0:
        R = -R
    yaw = math.atan2(R[1,0], R[0,0])
    pitch = math.asin(float(np.clip(-R[2,0], -1, 1)))
    return float(np.degrees(yaw)), float(np.degrees(pitch))

def camera_K_0(w: int, h: int, fov_deg: float = 50.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_1(w: int, h: int, fov_deg: float = 51.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_2(w: int, h: int, fov_deg: float = 52.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_3(w: int, h: int, fov_deg: float = 53.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_4(w: int, h: int, fov_deg: float = 54.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_5(w: int, h: int, fov_deg: float = 55.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_6(w: int, h: int, fov_deg: float = 56.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_7(w: int, h: int, fov_deg: float = 57.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_8(w: int, h: int, fov_deg: float = 58.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_9(w: int, h: int, fov_deg: float = 59.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_10(w: int, h: int, fov_deg: float = 60.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_11(w: int, h: int, fov_deg: float = 61.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_12(w: int, h: int, fov_deg: float = 62.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_13(w: int, h: int, fov_deg: float = 63.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_14(w: int, h: int, fov_deg: float = 64.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_15(w: int, h: int, fov_deg: float = 65.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_16(w: int, h: int, fov_deg: float = 66.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_17(w: int, h: int, fov_deg: float = 67.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_18(w: int, h: int, fov_deg: float = 68.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)

def camera_K_19(w: int, h: int, fov_deg: float = 69.0) -> np.ndarray:
    f = 0.5 * w / math.tan(math.radians(fov_deg) * 0.5)
    return np.array([[f, 0, w*0.5],[0, f, h*0.5],[0,0,1]], dtype=np.float64)
