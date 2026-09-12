import numpy as np

from nadir_core.dashcam.math_novel.bridge_coupling import (
    bridge_score_scalar,
    coupling_matrix_eigs,
    soft_coupling_energy,
)
from nadir_core.dashcam.math_novel.igmr import IGMRState, information_geometric_mount_residual
from nadir_core.dashcam.math_novel.lie_cusum import LeftInvariantCUSUM, lie_innovation


def test_sce_spd_and_monotone():
    e0 = soft_coupling_energy(0, 0, 0)
    e1 = soft_coupling_energy(1.0, 0, 0)
    assert e0 == 0.0
    assert e1 > e0
    assert bridge_score_scalar(e1) > bridge_score_scalar(e0)
    w = coupling_matrix_eigs()
    assert min(w) > 0


def test_igmr_positive_on_offset():
    st = IGMRState.identity()
    r0 = information_geometric_mount_residual(0.0, 0.0, 0.0, st)
    r1 = information_geometric_mount_residual(0.0, 0.0, 0.2, st)
    assert r1 >= 0 and r0 >= 0


def test_li_cusum_triggers_on_large_innov():
    det = LeftInvariantCUSUM(nu=0.05, lam=0.3)
    for _ in range(20):
        det.update(0.2)
    assert det.triggered
    assert det.arl_lower_bound() > 1.0


def test_lie_innovation_zero_when_equal():
    assert lie_innovation(0.1, -0.05, 0.2, 0.1, -0.05, 0.2) < 1e-9
