"""Huber-robust Mahalanobis fusion for NADIR Pulse tier."""

from __future__ import annotations

import importlib
from dataclasses import dataclass
from typing import Mapping, Optional, Sequence, Tuple

import numpy as np

from .math import mahalanobis_distance, round_score
from .types import ScoringThresholds


def _robust_losses_module():
    """Lazy import avoids scoring ↔ perception circular import at package load."""
    return importlib.import_module("nadir_sdk.perception.optimization.robust_losses")


@dataclass(frozen=True)
class RobustMahalanobisConfig:
    """Per-modality Huber scales for Pulse robust fusion."""

    huber_delta: float = 2.5
    use_modality_scales: bool = False
    modality_scales: Optional[object] = None


def _modality_losses(
    cfg: RobustMahalanobisConfig,
):
    mod = _robust_losses_module()
    RobustLoss = mod.RobustLoss
    delta = cfg.huber_delta
    if cfg.use_modality_scales:
        scales = cfg.modality_scales or mod.load_modality_scales()
        return (
            RobustLoss.huber(max(scales.camera, delta)),
            RobustLoss.huber(max(scales.radar, delta)),
            RobustLoss.huber(max(scales.lidar, delta)),
        )
    return RobustLoss.huber(delta), RobustLoss.huber(delta), RobustLoss.huber(delta)


def robust_psi_vector(
    cam_n: float,
    rad_n: float,
    lid_n: float,
    *,
    config: Optional[RobustMahalanobisConfig] = None,
) -> Tuple[float, float, float]:
    """Apply per-modality Huber ψ to normalized innovations."""
    cfg = config or RobustMahalanobisConfig()
    cam_loss, rad_loss, lid_loss = _modality_losses(cfg)
    return (
        float(cam_loss.psi(cam_n)),
        float(rad_loss.psi(rad_n)),
        float(lid_loss.psi(lid_n)),
    )


def _disagreement_ratio(cam_n: float, rad_n: float, lid_n: float) -> float:
    vec = np.abs(np.array([cam_n, rad_n, lid_n], dtype=np.float64))
    active = vec[vec > 1e-9]
    if active.size < 2:
        return 1.0
    return float(np.max(active) / max(float(np.min(active)), 1e-9))


def pulse_robust_mahalanobis(
    cam_n: float,
    rad_n: float,
    lid_n: float,
    *,
    config: Optional[RobustMahalanobisConfig] = None,
    sigma_diag: Optional[Sequence[float]] = None,
) -> float:
    """
    Robustified Mahalanobis scalar for Pulse tier.

    Applies Huber ψ per modality in **normalized innovation space**, then uses a
    hybrid rule: when cross-modal disagreement is low (coupled drift), retain L2
    Mahalanobis so true multi-modal elevation still tiers correctly.
    """
    cfg = config or RobustMahalanobisConfig()
    vec = np.array([cam_n, rad_n, lid_n], dtype=np.float64)
    if sigma_diag is not None:
        sig = np.array(sigma_diag, dtype=np.float64)
        vec = vec / (sig + 1e-9)

    l2 = float(np.linalg.norm(vec))
    cam_loss, rad_loss, lid_loss = _modality_losses(cfg)
    psi = np.array(
        [
            float(cam_loss.psi(vec[0])),
            float(rad_loss.psi(vec[1])),
            float(lid_loss.psi(vec[2])),
        ],
        dtype=np.float64,
    )
    robust = float(np.sqrt(float(psi @ psi)))

    disagreement = _disagreement_ratio(vec[0], vec[1], vec[2])
    if disagreement <= 2.5:
        return l2
    return robust


def compare_l2_vs_robust_on_vibration_fixture(
    *,
    vibration_spikes: Sequence[Tuple[float, float, float]],
    nominal: Tuple[float, float, float],
    thresholds: ScoringThresholds,
    config: Optional[RobustMahalanobisConfig] = None,
) -> Mapping[str, float]:
    """
    Benchmark helper: count CAUTION-tier frames under L2 vs robust Mahalanobis.

    Returns false CAUTION rates for nominal-only classification on spike frames.
    """
    cfg = config or RobustMahalanobisConfig()
    l2_caution = 0
    robust_caution = 0
    total = len(vibration_spikes)
    if total == 0:
        return {"l2_false_caution_rate": 0.0, "robust_false_caution_rate": 0.0, "trials": 0}

    nominal_vec = np.array(nominal, dtype=np.float64)
    l2_nominal = float(np.linalg.norm(nominal_vec))
    robust_nominal = pulse_robust_mahalanobis(*nominal, config=cfg)

    for cam_n, rad_n, lid_n in vibration_spikes:
        l2 = float(np.linalg.norm([cam_n, rad_n, lid_n]))
        robust = pulse_robust_mahalanobis(cam_n, rad_n, lid_n, config=cfg)
        if l2 >= thresholds.mahal_caution and l2_nominal < thresholds.mahal_caution:
            l2_caution += 1
        if robust >= thresholds.mahal_caution and robust_nominal < thresholds.mahal_caution:
            robust_caution += 1

    return {
        "l2_false_caution_rate": l2_caution / total,
        "robust_false_caution_rate": robust_caution / total,
        "trials": float(total),
        "improvement_ratio": (l2_caution - robust_caution) / max(l2_caution, 1),
    }


def score_mahalanobis_pair(
    cam_n: float,
    rad_n: float,
    lid_n: float,
    *,
    use_robust: bool,
    config: Optional[RobustMahalanobisConfig] = None,
) -> Tuple[float, float]:
    """Return (tier_mahal, l2_mahal) where tier_mahal uses hybrid robust rule when enabled."""
    drift_vec = (cam_n, rad_n, lid_n)
    l2 = round_score(mahalanobis_distance(drift_vec))
    hybrid = round_score(pulse_robust_mahalanobis(cam_n, rad_n, lid_n, config=config))
    if use_robust:
        return hybrid, l2
    return l2, hybrid
