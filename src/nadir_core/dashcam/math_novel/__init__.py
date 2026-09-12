"""NADIR novel dashcam mathematics (Open Core formulations)."""

from nadir_core.dashcam.math_novel.igmr import IGMRState, information_geometric_mount_residual
from nadir_core.dashcam.math_novel.lie_cusum import LeftInvariantCUSUM, lie_innovation
from nadir_core.dashcam.math_novel.bridge_coupling import soft_coupling_energy, bridge_score_scalar

__all__ = [
    "IGMRState",
    "information_geometric_mount_residual",
    "LeftInvariantCUSUM",
    "lie_innovation",
    "soft_coupling_energy",
    "bridge_score_scalar",
]
