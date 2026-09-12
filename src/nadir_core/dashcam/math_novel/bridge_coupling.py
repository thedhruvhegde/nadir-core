from __future__ import annotations

from typing import Tuple

import numpy as np


def soft_coupling_energy(
    yaw_deg: float,
    pitch_deg: float,
    roll_deg: float,
    *,
    alpha: float = 0.35,
    beta: float = 0.25,
    gamma: float = 0.15,
) -> float:
    """
    NADIR Soft Coupling Energy (SCE).

    E = alpha*yaw^2 + beta*pitch^2 + gamma*roll^2 + 2*c12*yaw*pitch + ...
    with cross terms chosen so the quadratic form is SPD (proof: Gershgorin /
    leading minors in docs/proofs/SOFT_COUPLING.md). Maps vision mount error
    into a scalar that Pulse can treat like a normalized innovation energy.
    """
    y, p, r = float(yaw_deg), float(pitch_deg), float(roll_deg)
    # SPD coupling matrix (fixed open-core constants)
    c_yp, c_yr, c_pr = 0.08, 0.05, 0.04
    Q = np.array(
        [
            [alpha, c_yp, c_yr],
            [c_yp, beta, c_pr],
            [c_yr, c_pr, gamma],
        ],
        dtype=np.float64,
    )
    v = np.array([y, p, r], dtype=np.float64)
    return float(v.T @ Q @ v)


def bridge_score_scalar(energy: float, *, softplus_k: float = 1.4) -> float:
    """Monotone map energy -> Pulse-like mahal proxy; 0 at 0, ~linear for small e."""
    e = max(0.0, float(energy))
    return float(np.log1p(softplus_k * e) / softplus_k * 10.0)


def coupling_matrix_eigs() -> Tuple[float, float, float]:
    alpha, beta, gamma = 0.35, 0.25, 0.15
    c_yp, c_yr, c_pr = 0.08, 0.05, 0.04
    Q = np.array([[alpha, c_yp, c_yr], [c_yp, beta, c_pr], [c_yr, c_pr, gamma]], dtype=np.float64)
    w = np.linalg.eigvalsh(Q)
    return float(w[0]), float(w[1]), float(w[2])
