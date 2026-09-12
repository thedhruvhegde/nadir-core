from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np

from nadir_core.dashcam.geometry.lie_so3 import rpy_to_rot, so3_log


@dataclass
class IGMRState:
    """Running natural parameters for a Gaussian mount estimate on R^3 (rpy)."""

    mean: np.ndarray
    precision: np.ndarray
    n: int = 0

    @classmethod
    def identity(cls) -> "IGMRState":
        return cls(mean=np.zeros(3), precision=np.eye(3) * 1e-3, n=0)

    def update(self, z: np.ndarray, meas_prec: np.ndarray) -> None:
        z = np.asarray(z, dtype=np.float64).reshape(3)
        meas_prec = np.asarray(meas_prec, dtype=np.float64).reshape(3, 3)
        # information-form Bayesian update on R^3 chart
        P = self.precision + meas_prec
        rhs = self.precision @ self.mean + meas_prec @ z
        self.mean = np.linalg.solve(P, rhs)
        self.precision = P
        self.n += 1


def _fisher_rao_gaussian_distance(
    m0: np.ndarray,
    P0: np.ndarray,
    m1: np.ndarray,
    P1: np.ndarray,
) -> float:
    """
    Closed-form Fisher-Rao geodesic length between two nondegenerate Gaussians
    on R^d with fixed-chart mean/precision (Amari-style information geometry).

    For equal-covariance Gaussians this reduces to Mahalanobis; the general
    formula includes a covariance geodesic term (see docs/proofs/IGMR.md).
    """
    m0 = np.asarray(m0, dtype=np.float64).reshape(-1)
    m1 = np.asarray(m1, dtype=np.float64).reshape(-1)
    C0 = np.linalg.inv(P0)
    C1 = np.linalg.inv(P1)
    # mean contribution under average metric
    Cbar = 0.5 * (C0 + C1)
    dm = m1 - m0
    mean_term = float(dm.T @ np.linalg.solve(Cbar, dm))
    # covariance contribution via affine-invariant metric on SPD
    # d^2 = ||log(C0^{-1/2} C1 C0^{-1/2})||_F^2
    w, V = np.linalg.eigh(C0)
    C0_inv_sqrt = V @ np.diag(1.0 / np.sqrt(np.maximum(w, 1e-12))) @ V.T
    M = C0_inv_sqrt @ C1 @ C0_inv_sqrt
    lw, _ = np.linalg.eigh(M)
    cov_term = float(np.sum(np.log(np.maximum(lw, 1e-12)) ** 2))
    return float(np.sqrt(max(0.0, mean_term + cov_term)))


def information_geometric_mount_residual(
    roll: float,
    pitch: float,
    yaw: float,
    state: IGMRState,
    *,
    meas_var: Tuple[float, float, float] = (0.05, 0.05, 0.08),
    update_state: bool = True,
) -> float:
    """
    NADIR IGMR: Fisher-Rao distance between the current mount posterior and the
    instantaneous measurement Gaussian on the rpy chart, with an SO(3) tie-break
    using ||Log(R_meas^T R_post)|| when the chart is near gimbal risk.
    """
    z = np.array([roll, pitch, yaw], dtype=np.float64)
    meas_prec = np.diag(1.0 / np.maximum(np.asarray(meas_var, dtype=np.float64), 1e-9))
    prior = IGMRState(mean=state.mean.copy(), precision=state.precision.copy(), n=state.n)
    if update_state:
        state.update(z, meas_prec)
        post = state
    else:
        # virtual update
        P = prior.precision + meas_prec
        rhs = prior.precision @ prior.mean + meas_prec @ z
        m = np.linalg.solve(P, rhs)
        post = IGMRState(mean=m, precision=P, n=prior.n + 1)

    d_fr = _fisher_rao_gaussian_distance(prior.mean, prior.precision, post.mean, post.precision)
    # Lie residual between chart means
    R0 = rpy_to_rot(*prior.mean.tolist())
    R1 = rpy_to_rot(*z.tolist())
    lie = float(np.linalg.norm(so3_log(R0.T @ R1)))
    # blend: information geometry dominates; Lie term guards chart singularities
    return float(0.75 * d_fr + 0.25 * lie)
