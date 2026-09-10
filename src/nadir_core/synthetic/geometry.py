"""Rotation and sensor geometry helpers for synthetic telemetry."""

from __future__ import annotations

import math
from typing import List, Sequence, Tuple

import numpy as np

_IDENTITY_FLAT: Tuple[float, ...] = (
    1.0, 0.0, 0.0,
    0.0, 1.0, 0.0,
    0.0, 0.0, 1.0,
)


def identity_rotation() -> List[float]:
    """Row-major 3×3 identity rotation matrix."""
    return list(_IDENTITY_FLAT)


def euler_to_rotation_matrix(
    *,
    roll_deg: float = 0.0,
    pitch_deg: float = 0.0,
    yaw_deg: float = 0.0,
) -> List[float]:
    """
    Build a row-major rotation matrix from roll/pitch/yaw (degrees).

    Composition: R = Rz(yaw) @ Ry(pitch) @ Rx(roll).
    """
    roll, pitch, yaw = (math.radians(v) for v in (roll_deg, pitch_deg, yaw_deg))

    cx, sx = math.cos(roll), math.sin(roll)
    cy, sy = math.cos(pitch), math.sin(pitch)
    cz, sz = math.cos(yaw), math.sin(yaw)

    rx = np.array([[1.0, 0.0, 0.0], [0.0, cx, -sx], [0.0, sx, cx]])
    ry = np.array([[cy, 0.0, sy], [0.0, 1.0, 0.0], [-sy, 0.0, cy]])
    rz = np.array([[cz, -sz, 0.0], [sz, cz, 0.0], [0.0, 0.0, 1.0]])
    matrix = rz @ ry @ rx
    return [float(x) for x in matrix.reshape(-1).tolist()]


def smoothstep(progress: float) -> float:
    """Hermite ease-in-out on [0, 1] (clamped)."""
    t = min(1.0, max(0.0, progress))
    return t * t * (3.0 - 2.0 * t)


def add_noise(value: float, rng: np.random.Generator, sigma: float) -> float:
    return float(value + rng.normal(0.0, sigma))
