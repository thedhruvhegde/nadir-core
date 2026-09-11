from __future__ import annotations

import math
from typing import Iterable, List, Sequence, Tuple

import numpy as np

EPS = 1e-12


def hat(w: Sequence[float]) -> np.ndarray:
    wx, wy, wz = float(w[0]), float(w[1]), float(w[2])
    return np.array([[0.0, -wz, wy], [wz, 0.0, -wx], [-wy, wx, 0.0]], dtype=np.float64)


def vee(W: np.ndarray) -> np.ndarray:
    return np.array([W[2, 1], W[0, 2], W[1, 0]], dtype=np.float64)


def so3_exp(w: Sequence[float]) -> np.ndarray:
    w = np.asarray(w, dtype=np.float64).reshape(3)
    theta = float(np.linalg.norm(w))
    if theta < EPS:
        return np.eye(3) + hat(w)
    k = w / theta
    K = hat(k)
    s, c = math.sin(theta), math.cos(theta)
    return np.eye(3) + s * K + (1.0 - c) * (K @ K)


def so3_log(R: np.ndarray) -> np.ndarray:
    R = np.asarray(R, dtype=np.float64).reshape(3, 3)
    cos_theta = (np.trace(R) - 1.0) * 0.5
    cos_theta = float(np.clip(cos_theta, -1.0, 1.0))
    theta = math.acos(cos_theta)
    if theta < EPS:
        return vee(0.5 * (R - R.T))
    if abs(theta - math.pi) < 1e-6:
        # near-pi branch
        A = 0.5 * (R + np.eye(3))
        idx = int(np.argmax(np.diag(A)))
        v = np.sqrt(np.maximum(np.diag(A), 0.0))
        if A[idx, idx] < EPS:
            return np.array([theta, 0.0, 0.0])
        # sign recovery
        for i in range(3):
            for j in range(i + 1, 3):
                if A[i, j] < 0:
                    if abs(v[i]) > abs(v[j]):
                        v[j] = -v[j]
                    else:
                        v[i] = -v[i]
        return theta * v / (np.linalg.norm(v) + EPS)
    return (theta / (2.0 * math.sin(theta))) * vee(R - R.T)


def left_jacobian(w: Sequence[float]) -> np.ndarray:
    w = np.asarray(w, dtype=np.float64).reshape(3)
    theta = float(np.linalg.norm(w))
    if theta < EPS:
        return np.eye(3) + 0.5 * hat(w)
    K = hat(w / theta)
    s, c = math.sin(theta), math.cos(theta)
    a = (1.0 - c) / theta
    b = (theta - s) / theta
    return np.eye(3) + a * K + b * (K @ K)


def left_jacobian_inv(w: Sequence[float]) -> np.ndarray:
    w = np.asarray(w, dtype=np.float64).reshape(3)
    theta = float(np.linalg.norm(w))
    if theta < EPS:
        return np.eye(3) - 0.5 * hat(w)
    half = 0.5 * theta
    cot = 1.0 / math.tan(half) if abs(math.sin(half)) > EPS else 0.0
    K = hat(w / theta)
    a = half * cot
    return np.eye(3) - 0.5 * hat(w) / 1.0 + (1.0 - a) * (K @ K)


def geodesic_distance(R1: np.ndarray, R2: np.ndarray) -> float:
    return float(np.linalg.norm(so3_log(R1.T @ R2)))


def rot_x(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], dtype=np.float64)


def rot_y(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]], dtype=np.float64)


def rot_z(a: float) -> np.ndarray:
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], dtype=np.float64)


def rpy_to_rot(roll: float, pitch: float, yaw: float) -> np.ndarray:
    return rot_z(yaw) @ rot_y(pitch) @ rot_x(roll)


def rot_to_rpy(R: np.ndarray) -> Tuple[float, float, float]:
    R = np.asarray(R, dtype=np.float64).reshape(3, 3)
    pitch = math.asin(float(np.clip(-R[2, 0], -1.0, 1.0)))
    if abs(math.cos(pitch)) < 1e-8:
        roll = 0.0
        yaw = math.atan2(-R[0, 1], R[1, 1])
    else:
        roll = math.atan2(R[2, 1], R[2, 2])
        yaw = math.atan2(R[1, 0], R[0, 0])
    return roll, pitch, yaw


def slerp(R0: np.ndarray, R1: np.ndarray, t: float) -> np.ndarray:
    t = float(np.clip(t, 0.0, 1.0))
    w = so3_log(R0.T @ R1)
    return R0 @ so3_exp(t * w)


def average_rotations(Rs: Iterable[np.ndarray], iters: int = 20) -> np.ndarray:
    Rs = [np.asarray(R, dtype=np.float64) for R in Rs]
    if not Rs:
        return np.eye(3)
    R = Rs[0].copy()
    for _ in range(iters):
        acc = np.zeros(3)
        for Ri in Rs:
            acc += so3_log(R.T @ Ri)
        acc /= len(Rs)
        if np.linalg.norm(acc) < 1e-10:
            break
        R = R @ so3_exp(acc)
    return R


def adjoint_SE3(T: np.ndarray) -> np.ndarray:
    R = T[:3, :3]
    t = T[:3, 3]
    Ad = np.zeros((6, 6), dtype=np.float64)
    Ad[:3, :3] = R
    Ad[3:, 3:] = R
    Ad[3:, :3] = hat(t) @ R
    return Ad


def se3_exp(xi: Sequence[float]) -> np.ndarray:
    xi = np.asarray(xi, dtype=np.float64).reshape(6)
    w, v = xi[:3], xi[3:]
    R = so3_exp(w)
    J = left_jacobian(w)
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = J @ v
    return T


def se3_log(T: np.ndarray) -> np.ndarray:
    T = np.asarray(T, dtype=np.float64).reshape(4, 4)
    w = so3_log(T[:3, :3])
    Jinv = left_jacobian_inv(w)
    v = Jinv @ T[:3, 3]
    return np.concatenate([w, v])


def make_pose(R: np.ndarray, t: Sequence[float]) -> np.ndarray:
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = np.asarray(t, dtype=np.float64)
    return T
