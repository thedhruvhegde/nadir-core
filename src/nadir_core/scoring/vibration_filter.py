"""Vibration-notch residual pre-filter for Pulse (P6).

Attenuates normalized residuals when operating context indicates energy in the
10–30 Hz band (road vibration, post-collision shake) so Mahalanobis fusion is
less sensitive to mechanical coupling spikes.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Optional, Tuple

from .math import round_score


@dataclass(frozen=True)
class VibrationFilterConfig:
    band_low_hz: float = 10.0
    band_high_hz: float = 30.0
    """Fraction of in-band residual magnitude retained after notch (0–1)."""
    attenuation: float = 0.35
    vibration_index_threshold: float = 0.35
    dominant_freq_tolerance_hz: float = 2.5


@dataclass(frozen=True)
class VibrationFilterResult:
    cam_n: float
    rad_n: float
    lid_n: float
    applied: bool
    band_energy: float
    attenuation_factor: float
    dominant_freq_hz: Optional[float] = None
    reason: Optional[str] = None

    def to_dict(self) -> dict[str, object]:
        body: dict[str, object] = {
            "applied": self.applied,
            "band_energy": round(self.band_energy, 4),
            "attenuation_factor": round(self.attenuation_factor, 4),
        }
        if self.dominant_freq_hz is not None:
            body["dominant_freq_hz"] = round(self.dominant_freq_hz, 2)
        if self.reason is not None:
            body["reason"] = self.reason
        return body


def _extract_operating_context(
    pulse_context: Optional[Mapping[str, object]],
) -> Mapping[str, object]:
    if pulse_context is None:
        return {}
    oc = pulse_context.get("operating_context")
    if isinstance(oc, Mapping):
        return oc
    return {}


def _dominant_vibration_freq_hz(pulse_context: Optional[Mapping[str, object]]) -> Optional[float]:
    if pulse_context is None:
        return None
    meta = pulse_context.get("metadata")
    if isinstance(meta, Mapping):
        raw = meta.get("dominant_vibration_hz")
        if isinstance(raw, (int, float)):
            return float(raw)
    spectrum = pulse_context.get("vibration_spectrum")
    if isinstance(spectrum, Mapping):
        peaks = spectrum.get("peak_hz")
        if isinstance(peaks, (list, tuple)) and peaks:
            first = peaks[0]
            if isinstance(first, (int, float)):
                return float(first)
        raw = spectrum.get("dominant_hz")
        if isinstance(raw, (int, float)):
            return float(raw)
    return None


def estimate_vibration_band_energy(
    pulse_context: Optional[Mapping[str, object]],
    *,
    config: Optional[VibrationFilterConfig] = None,
) -> Tuple[float, Optional[float]]:
    """Return (band_energy 0–1, dominant_freq_hz)."""
    cfg = config or VibrationFilterConfig()
    oc = _extract_operating_context(pulse_context)
    vib_index = oc.get("vibration_index")
    if isinstance(vib_index, (int, float)):
        energy = float(max(0.0, min(1.0, vib_index)))
        freq = _dominant_vibration_freq_hz(pulse_context)
        return energy, freq

    if pulse_context is not None:
        meta = pulse_context.get("metadata")
        if isinstance(meta, Mapping) and meta.get("scenario") in {"vibration", "post_collision"}:
            energy = float(meta.get("vibration_energy", 0.55))
            return max(0.0, min(1.0, energy)), _dominant_vibration_freq_hz(pulse_context)

    gyro_rms = oc.get("imu_gyro_rms_radps")
    if isinstance(gyro_rms, (int, float)):
        energy = float(max(0.0, min(1.0, gyro_rms / 0.8)))
        return energy, _dominant_vibration_freq_hz(pulse_context)

    return 0.0, _dominant_vibration_freq_hz(pulse_context)


def _in_notch_band(
    freq_hz: Optional[float],
    *,
    config: VibrationFilterConfig,
) -> bool:
    if freq_hz is None:
        return True
    return (
        config.band_low_hz - config.dominant_freq_tolerance_hz
        <= freq_hz
        <= config.band_high_hz + config.dominant_freq_tolerance_hz
    )


def apply_vibration_notch_filter(
    cam_n: float,
    rad_n: float,
    lid_n: float,
    pulse_context: Optional[Mapping[str, object]] = None,
    *,
    config: Optional[VibrationFilterConfig] = None,
) -> VibrationFilterResult:
    """
    Attenuate normalized residuals when vibration band energy exceeds threshold.

    Radar and LiDAR channels are attenuated more aggressively than camera yaw
    because mechanical vibration couples strongly into range/registration residuals.
    """
    cfg = config or VibrationFilterConfig()
    energy, freq = estimate_vibration_band_energy(pulse_context, config=cfg)

    if energy < cfg.vibration_index_threshold or not _in_notch_band(freq, config=cfg):
        return VibrationFilterResult(
            cam_n=cam_n,
            rad_n=rad_n,
            lid_n=lid_n,
            applied=False,
            band_energy=energy,
            attenuation_factor=1.0,
            dominant_freq_hz=freq,
            reason="below_threshold" if energy < cfg.vibration_index_threshold else "outside_band",
        )

    # Scale attenuation with band energy; radar/lidar get extra notch depth.
    base = cfg.attenuation + (1.0 - cfg.attenuation) * (1.0 - energy)
    cam_factor = base + (1.0 - base) * 0.35
    range_factor = base
    lid_factor = base * 0.92

    out_cam = round_score(cam_n * cam_factor)
    out_rad = round_score(rad_n * range_factor)
    out_lid = round_score(lid_n * lid_factor)

    return VibrationFilterResult(
        cam_n=out_cam,
        rad_n=out_rad,
        lid_n=out_lid,
        applied=True,
        band_energy=energy,
        attenuation_factor=range_factor,
        dominant_freq_hz=freq,
        reason="notch_applied",
    )


def compare_tiers_on_post_collision_fixture(
    *,
    vibration_spikes: list[tuple[float, float, float]],
    nominal: tuple[float, float, float],
    thresholds: object,
    pulse_context: Mapping[str, object],
) -> dict[str, int | bool]:
    """Count false CAUTION Mahalanobis hits with and without vibration notch."""
    from .math import mahalanobis_distance
    from .types import ScoringThresholds

    cfg = thresholds if isinstance(thresholds, ScoringThresholds) else ScoringThresholds()
    raw_caution = 0
    filtered_caution = 0
    cam0, rad0, lid0 = nominal
    nominal_mahal = mahalanobis_distance((cam0, rad0, lid0))

    for cam_n, rad_n, lid_n in vibration_spikes:
        mahal_raw = mahalanobis_distance((cam_n, rad_n, lid_n))
        if mahal_raw >= cfg.mahal_caution and nominal_mahal < cfg.mahal_caution:
            raw_caution += 1

        filt = apply_vibration_notch_filter(cam_n, rad_n, lid_n, pulse_context)
        mahal_f = mahalanobis_distance((filt.cam_n, filt.rad_n, filt.lid_n))
        if mahal_f >= cfg.mahal_caution and nominal_mahal < cfg.mahal_caution:
            filtered_caution += 1

    filt_nom = apply_vibration_notch_filter(cam0, rad0, lid0, pulse_context)
    nominal_filtered = mahalanobis_distance((filt_nom.cam_n, filt_nom.rad_n, filt_nom.lid_n))

    return {
        "raw_false_caution": raw_caution,
        "filtered_false_caution": filtered_caution,
        "nominal_tier_stable": nominal_mahal < cfg.mahal_caution
        and nominal_filtered < cfg.mahal_caution,
    }
