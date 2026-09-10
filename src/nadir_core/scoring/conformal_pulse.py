"""Split-conformal lite for Pulse — single-modality strata (P9)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Mapping, Optional, Sequence

from .conformal import ConformalConfig, SplitConformalCalibrator, empirical_caution_rate
from .types import DriftTier


SINGLE_MODALITY_STRATA = ("camera", "radar", "lidar")


@dataclass(frozen=True)
class PulseConformalLiteConfig:
    alpha: float = 0.10
    min_calibration_per_stratum: int = 6


@dataclass
class PulseConformalLite:
    """
    Lightweight Mondrian conformal gate for Pulse single-modality strata.

    Unlike Meridian multi-modal conformal, each stratum key is ``MODALITY:single``.
    """

    config: PulseConformalLiteConfig = field(default_factory=PulseConformalLiteConfig)
    _calibrator: SplitConformalCalibrator = field(init=False)

    def __post_init__(self) -> None:
        inner = ConformalConfig(
            alpha=self.config.alpha,
            min_calibration_per_stratum=self.config.min_calibration_per_stratum,
        )
        self._calibrator = SplitConformalCalibrator(inner)
        self._seed_default_quantiles()

    def _seed_default_quantiles(self) -> None:
        self._calibrator.global_quantile = 2.8
        for modality in SINGLE_MODALITY_STRATA:
            self._calibrator.quantiles[f"DEFAULT:{modality}"] = {
                "camera": 2.6,
                "radar": 3.0,
                "lidar": 2.9,
            }[modality]

    def fit_from_records(
        self,
        records: Sequence[Mapping[str, object]],
    ) -> None:
        enriched = []
        for rec in records:
            modality = str(rec.get("dominant_modality", "camera"))
            enriched.append({**rec, "dominant_modality": modality})
        self._calibrator.fit(enriched, motion_segments=[None] * len(enriched))

    def dominant_modality_from_vector(
        self,
        fault_vector: Mapping[str, float],
    ) -> str:
        ranked = sorted(
            ((key, float(fault_vector.get(key, 0.0))) for key in ("camera", "radar", "lidar")),
            key=lambda item: item[1],
            reverse=True,
        )
        return ranked[0][0]

    def apply(
        self,
        mahal: float,
        *,
        raw_tier: DriftTier,
        dominant_modality: str,
        motion_segment: Optional[str] = None,
    ) -> dict[str, object]:
        gate = self._calibrator.apply(
            mahal,
            motion_segment=motion_segment,
            modality=f"{dominant_modality}",
            raw_tier=raw_tier,
        )
        return {
            "enabled": True,
            "alpha": self.config.alpha,
            "stratum": gate.stratum.key(),
            "threshold": round(gate.threshold, 4),
            "raw_score": round(gate.raw_score, 4),
            "exceeds_threshold": gate.exceeds_threshold,
            "adjusted_tier": gate.adjusted_tier.value,
        }


_default_lite: Optional[PulseConformalLite] = None


def get_pulse_conformal_lite() -> PulseConformalLite:
    global _default_lite
    if _default_lite is None:
        _default_lite = PulseConformalLite()
    return _default_lite


def reset_pulse_conformal_lite() -> None:
    global _default_lite
    _default_lite = None


def empirical_caution_rate_from_gates(gates: Sequence[Mapping[str, object]]) -> float:
    return empirical_caution_rate(g.get("adjusted_tier", "NOMINAL") for g in gates)
