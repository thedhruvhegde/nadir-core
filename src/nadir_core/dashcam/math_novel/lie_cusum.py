from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from nadir_core.dashcam.geometry.lie_so3 import rpy_to_rot, so3_log


def lie_innovation(roll: float, pitch: float, yaw: float, roll_h: float, pitch_h: float, yaw_h: float) -> float:
    """Left-invariant innovation magnitude ||Log(R_hat^{-1} R)|| on SO(3)."""
    R = rpy_to_rot(roll, pitch, yaw)
    Rh = rpy_to_rot(roll_h, pitch_h, yaw_h)
    return float(np.linalg.norm(so3_log(Rh.T @ R)))


@dataclass
class LeftInvariantCUSUM:
    """
    NADIR LI-CUSUM: Page-Hinkley style detector on left-invariant SO(3) innovations.

    Under the nominal model, innovations are treated as sub-exponential with scale
    sigma; the threshold lambda yields an explicit average-run-length lower bound
    (see docs/proofs/LI_CUSUM.md).
    """

    nu: float = 0.08
    lam: float = 1.25
    sigma: float = 0.12
    s: float = 0.0
    triggered: bool = False
    history: list = field(default_factory=list)

    def update(self, innov: float) -> bool:
        self.s = max(0.0, self.s + float(innov) - self.nu)
        self.history.append(self.s)
        self.triggered = self.s > self.lam
        return self.triggered

    def arl_lower_bound(self) -> float:
        # ARL0 >= exp(2*lam*nu / sigma^2) / (2*nu/sigma)   (Chernoff-style bound used in proof)
        if self.sigma <= 0 or self.nu <= 0:
            return float("inf")
        return float(np.exp(2.0 * self.lam * self.nu / (self.sigma ** 2)) / (2.0 * self.nu / self.sigma))
