"""Split and Mondrian conformal calibration for tier thresholds."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np

from .types import DriftTier, ScoringThresholds


@dataclass(frozen=True)
class ConformalStratum:
    motion_segment: str
    modality: str

    @classmethod
    def from_parts(
        cls,
        motion_segment: Optional[str],
        modality: str = "multi",
    ) -> "ConformalStratum":
        return cls((motion_segment or "DEFAULT").upper(), modality.lower())

    def key(self) -> str:
        return f"{self.motion_segment}:{self.modality}"


@dataclass
class ConformalConfig:
    alpha: float = 0.05
    calibration_fraction: float = 0.35
    score_key: str = "mahal_distance"
    min_calibration_per_stratum: int = 8


@dataclass
class ConformalCalibrationResult:
    quantiles: Dict[str, float]
    global_quantile: float
    alpha: float
    calibration_samples: int
    strata: Dict[str, int] = field(default_factory=dict)


@dataclass
class ConformalGateResult:
    raw_score: float
    threshold: float
    stratum: ConformalStratum
    exceeds_threshold: bool
    adjusted_tier: DriftTier


class SplitConformalCalibrator:
    """
    Split conformal quantiles on scalar score S with Mondrian strata.

    Target: empirical CAUTION rate ≈ α on nominal holdout replay.
    """

    def __init__(self, config: Optional[ConformalConfig] = None) -> None:
        self.config = config or ConformalConfig()
        self.quantiles: Dict[str, float] = {}
        self.global_quantile: float = 0.0
        self.strata_counts: Dict[str, int] = {}
        self.calibration_samples: int = 0

    def fit(
        self,
        records: Sequence[Mapping[str, object]],
        *,
        motion_segments: Optional[Sequence[Optional[str]]] = None,
    ) -> ConformalCalibrationResult:
        cfg = self.config
        n = len(records)
        if n == 0:
            return ConformalCalibrationResult({}, 0.0, cfg.alpha, 0)

        cal_n = max(cfg.min_calibration_per_stratum, int(round(n * cfg.calibration_fraction)))
        cal_n = min(cal_n, n - 1) if n > 1 else n
        cal_records = list(records[:cal_n])
        motion_segments = list(motion_segments or [None] * n)[:cal_n]

        residuals_by_stratum: Dict[str, List[float]] = {}
        all_scores: List[float] = []
        for rec, seg in zip(cal_records, motion_segments):
            score = float(rec.get(cfg.score_key, rec.get("residual_score", 0.0)))
            all_scores.append(score)
            stratum = ConformalStratum.from_parts(seg, str(rec.get("dominant_modality", "multi")))
            residuals_by_stratum.setdefault(stratum.key(), []).append(score)

        q_level = 1.0 - cfg.alpha
        sorted_scores = sorted(all_scores)
        cal_size = len(sorted_scores)
        if cal_size > 0:
            rank = min(cal_size, max(1, int(math.ceil((cal_size + 1) * q_level))))
            self.global_quantile = float(sorted_scores[rank - 1])
        else:
            self.global_quantile = 0.0
        self.quantiles = {}
        self.strata_counts = {}
        for key, scores in residuals_by_stratum.items():
            s_sorted = sorted(scores)
            if len(s_sorted) >= cfg.min_calibration_per_stratum:
                rank = min(len(s_sorted), max(1, int(math.ceil((len(s_sorted) + 1) * q_level))))
                self.quantiles[key] = float(s_sorted[rank - 1])
            else:
                self.quantiles[key] = self.global_quantile
            self.strata_counts[key] = len(scores)
        self.calibration_samples = cal_n
        return ConformalCalibrationResult(
            quantiles=dict(self.quantiles),
            global_quantile=self.global_quantile,
            alpha=cfg.alpha,
            calibration_samples=cal_n,
            strata=dict(self.strata_counts),
        )

    def threshold_for(
        self,
        stratum: ConformalStratum,
    ) -> float:
        return float(self.quantiles.get(stratum.key(), self.global_quantile))

    def apply(
        self,
        score: float,
        *,
        motion_segment: Optional[str] = None,
        modality: str = "multi",
        raw_tier: DriftTier,
    ) -> ConformalGateResult:
        stratum = ConformalStratum.from_parts(motion_segment, modality)
        threshold = self.threshold_for(stratum)
        exceeds = float(score) > threshold
        adjusted = raw_tier
        if raw_tier is DriftTier.CAUTION and not exceeds:
            adjusted = DriftTier.NOMINAL
        if raw_tier is DriftTier.NOMINAL and exceeds:
            adjusted = DriftTier.CAUTION
        return ConformalGateResult(
            raw_score=float(score),
            threshold=threshold,
            stratum=stratum,
            exceeds_threshold=exceeds,
            adjusted_tier=adjusted,
        )


def empirical_caution_rate(tiers: Iterable[str]) -> float:
    tiers_list = list(tiers)
    if not tiers_list:
        return 0.0
    return sum(1 for t in tiers_list if t == DriftTier.CAUTION.value) / len(tiers_list)
