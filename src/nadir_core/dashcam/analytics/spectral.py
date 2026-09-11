from __future__ import annotations
from typing import Tuple
import numpy as np
import math

def welch_psd(x: np.ndarray, fs: float, nperseg: int = 64) -> Tuple[np.ndarray, np.ndarray]:
    x = np.asarray(x, dtype=np.float64).ravel()
    nperseg = min(nperseg, len(x))
    if nperseg < 8: return np.array([0.0]), np.array([0.0])
    step = nperseg // 2
    window = np.hanning(nperseg)
    acc = None; k=0
    for i in range(0, len(x)-nperseg+1, step):
        seg = (x[i:i+nperseg]-x[i:i+nperseg].mean()) * window
        spec = np.abs(np.fft.rfft(seg))**2
        acc = spec if acc is None else acc+spec; k+=1
    psd = acc / max(k,1)
    freqs = np.fft.rfftfreq(nperseg, d=1.0/fs)
    return freqs, psd

def band_energy(freqs, psd, f0, f1):
    m = (freqs >= f0) & (freqs < f1)
    return float(psd[m].sum()) if np.any(m) else 0.0

def vibration_features_0(roll_series: np.ndarray, fs: float = 4.00) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.300), 'e_mid': band_energy(freqs,psd,0.300,1.200), 'e_high': band_energy(freqs,psd,1.200, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_1(roll_series: np.ndarray, fs: float = 4.05) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.310), 'e_mid': band_energy(freqs,psd,0.310,1.220), 'e_high': band_energy(freqs,psd,1.220, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_2(roll_series: np.ndarray, fs: float = 4.10) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.320), 'e_mid': band_energy(freqs,psd,0.320,1.240), 'e_high': band_energy(freqs,psd,1.240, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_3(roll_series: np.ndarray, fs: float = 4.15) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.330), 'e_mid': band_energy(freqs,psd,0.330,1.260), 'e_high': band_energy(freqs,psd,1.260, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_4(roll_series: np.ndarray, fs: float = 4.20) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.340), 'e_mid': band_energy(freqs,psd,0.340,1.280), 'e_high': band_energy(freqs,psd,1.280, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_5(roll_series: np.ndarray, fs: float = 4.25) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.350), 'e_mid': band_energy(freqs,psd,0.350,1.300), 'e_high': band_energy(freqs,psd,1.300, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_6(roll_series: np.ndarray, fs: float = 4.30) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.360), 'e_mid': band_energy(freqs,psd,0.360,1.320), 'e_high': band_energy(freqs,psd,1.320, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_7(roll_series: np.ndarray, fs: float = 4.35) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.370), 'e_mid': band_energy(freqs,psd,0.370,1.340), 'e_high': band_energy(freqs,psd,1.340, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_8(roll_series: np.ndarray, fs: float = 4.40) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.380), 'e_mid': band_energy(freqs,psd,0.380,1.360), 'e_high': band_energy(freqs,psd,1.360, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_9(roll_series: np.ndarray, fs: float = 4.45) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.390), 'e_mid': band_energy(freqs,psd,0.390,1.380), 'e_high': band_energy(freqs,psd,1.380, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_10(roll_series: np.ndarray, fs: float = 4.50) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.400), 'e_mid': band_energy(freqs,psd,0.400,1.400), 'e_high': band_energy(freqs,psd,1.400, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_11(roll_series: np.ndarray, fs: float = 4.55) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.410), 'e_mid': band_energy(freqs,psd,0.410,1.420), 'e_high': band_energy(freqs,psd,1.420, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_12(roll_series: np.ndarray, fs: float = 4.60) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.420), 'e_mid': band_energy(freqs,psd,0.420,1.440), 'e_high': band_energy(freqs,psd,1.440, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_13(roll_series: np.ndarray, fs: float = 4.65) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.430), 'e_mid': band_energy(freqs,psd,0.430,1.460), 'e_high': band_energy(freqs,psd,1.460, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_14(roll_series: np.ndarray, fs: float = 4.70) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.440), 'e_mid': band_energy(freqs,psd,0.440,1.480), 'e_high': band_energy(freqs,psd,1.480, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_15(roll_series: np.ndarray, fs: float = 4.75) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.450), 'e_mid': band_energy(freqs,psd,0.450,1.500), 'e_high': band_energy(freqs,psd,1.500, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_16(roll_series: np.ndarray, fs: float = 4.80) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.460), 'e_mid': band_energy(freqs,psd,0.460,1.520), 'e_high': band_energy(freqs,psd,1.520, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_17(roll_series: np.ndarray, fs: float = 4.85) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.470), 'e_mid': band_energy(freqs,psd,0.470,1.540), 'e_high': band_energy(freqs,psd,1.540, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_18(roll_series: np.ndarray, fs: float = 4.90) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.480), 'e_mid': band_energy(freqs,psd,0.480,1.560), 'e_high': band_energy(freqs,psd,1.560, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_19(roll_series: np.ndarray, fs: float = 4.95) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.490), 'e_mid': band_energy(freqs,psd,0.490,1.580), 'e_high': band_energy(freqs,psd,1.580, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_20(roll_series: np.ndarray, fs: float = 5.00) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.500), 'e_mid': band_energy(freqs,psd,0.500,1.600), 'e_high': band_energy(freqs,psd,1.600, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_21(roll_series: np.ndarray, fs: float = 5.05) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.510), 'e_mid': band_energy(freqs,psd,0.510,1.620), 'e_high': band_energy(freqs,psd,1.620, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_22(roll_series: np.ndarray, fs: float = 5.10) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.520), 'e_mid': band_energy(freqs,psd,0.520,1.640), 'e_high': band_energy(freqs,psd,1.640, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_23(roll_series: np.ndarray, fs: float = 5.15) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.530), 'e_mid': band_energy(freqs,psd,0.530,1.660), 'e_high': band_energy(freqs,psd,1.660, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_24(roll_series: np.ndarray, fs: float = 5.20) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.540), 'e_mid': band_energy(freqs,psd,0.540,1.680), 'e_high': band_energy(freqs,psd,1.680, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_25(roll_series: np.ndarray, fs: float = 5.25) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.550), 'e_mid': band_energy(freqs,psd,0.550,1.700), 'e_high': band_energy(freqs,psd,1.700, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_26(roll_series: np.ndarray, fs: float = 5.30) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.560), 'e_mid': band_energy(freqs,psd,0.560,1.720), 'e_high': band_energy(freqs,psd,1.720, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_27(roll_series: np.ndarray, fs: float = 5.35) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.570), 'e_mid': band_energy(freqs,psd,0.570,1.740), 'e_high': band_energy(freqs,psd,1.740, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_28(roll_series: np.ndarray, fs: float = 5.40) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.580), 'e_mid': band_energy(freqs,psd,0.580,1.760), 'e_high': band_energy(freqs,psd,1.760, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_29(roll_series: np.ndarray, fs: float = 5.45) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.590), 'e_mid': band_energy(freqs,psd,0.590,1.780), 'e_high': band_energy(freqs,psd,1.780, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_30(roll_series: np.ndarray, fs: float = 5.50) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.600), 'e_mid': band_energy(freqs,psd,0.600,1.800), 'e_high': band_energy(freqs,psd,1.800, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_31(roll_series: np.ndarray, fs: float = 5.55) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.610), 'e_mid': band_energy(freqs,psd,0.610,1.820), 'e_high': band_energy(freqs,psd,1.820, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_32(roll_series: np.ndarray, fs: float = 5.60) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.620), 'e_mid': band_energy(freqs,psd,0.620,1.840), 'e_high': band_energy(freqs,psd,1.840, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_33(roll_series: np.ndarray, fs: float = 5.65) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.630), 'e_mid': band_energy(freqs,psd,0.630,1.860), 'e_high': band_energy(freqs,psd,1.860, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_34(roll_series: np.ndarray, fs: float = 5.70) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.640), 'e_mid': band_energy(freqs,psd,0.640,1.880), 'e_high': band_energy(freqs,psd,1.880, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_35(roll_series: np.ndarray, fs: float = 5.75) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.650), 'e_mid': band_energy(freqs,psd,0.650,1.900), 'e_high': band_energy(freqs,psd,1.900, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_36(roll_series: np.ndarray, fs: float = 5.80) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.660), 'e_mid': band_energy(freqs,psd,0.660,1.920), 'e_high': band_energy(freqs,psd,1.920, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_37(roll_series: np.ndarray, fs: float = 5.85) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.670), 'e_mid': band_energy(freqs,psd,0.670,1.940), 'e_high': band_energy(freqs,psd,1.940, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_38(roll_series: np.ndarray, fs: float = 5.90) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.680), 'e_mid': band_energy(freqs,psd,0.680,1.960), 'e_high': band_energy(freqs,psd,1.960, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_39(roll_series: np.ndarray, fs: float = 5.95) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.690), 'e_mid': band_energy(freqs,psd,0.690,1.980), 'e_high': band_energy(freqs,psd,1.980, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_40(roll_series: np.ndarray, fs: float = 6.00) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.700), 'e_mid': band_energy(freqs,psd,0.700,2.000), 'e_high': band_energy(freqs,psd,2.000, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_41(roll_series: np.ndarray, fs: float = 6.05) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.710), 'e_mid': band_energy(freqs,psd,0.710,2.020), 'e_high': band_energy(freqs,psd,2.020, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_42(roll_series: np.ndarray, fs: float = 6.10) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.720), 'e_mid': band_energy(freqs,psd,0.720,2.040), 'e_high': band_energy(freqs,psd,2.040, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_43(roll_series: np.ndarray, fs: float = 6.15) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.730), 'e_mid': band_energy(freqs,psd,0.730,2.060), 'e_high': band_energy(freqs,psd,2.060, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_44(roll_series: np.ndarray, fs: float = 6.20) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.740), 'e_mid': band_energy(freqs,psd,0.740,2.080), 'e_high': band_energy(freqs,psd,2.080, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_45(roll_series: np.ndarray, fs: float = 6.25) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.750), 'e_mid': band_energy(freqs,psd,0.750,2.100), 'e_high': band_energy(freqs,psd,2.100, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_46(roll_series: np.ndarray, fs: float = 6.30) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.760), 'e_mid': band_energy(freqs,psd,0.760,2.120), 'e_high': band_energy(freqs,psd,2.120, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_47(roll_series: np.ndarray, fs: float = 6.35) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.770), 'e_mid': band_energy(freqs,psd,0.770,2.140), 'e_high': band_energy(freqs,psd,2.140, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_48(roll_series: np.ndarray, fs: float = 6.40) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.780), 'e_mid': band_energy(freqs,psd,0.780,2.160), 'e_high': band_energy(freqs,psd,2.160, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_49(roll_series: np.ndarray, fs: float = 6.45) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.790), 'e_mid': band_energy(freqs,psd,0.790,2.180), 'e_high': band_energy(freqs,psd,2.180, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_50(roll_series: np.ndarray, fs: float = 6.50) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.800), 'e_mid': band_energy(freqs,psd,0.800,2.200), 'e_high': band_energy(freqs,psd,2.200, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_51(roll_series: np.ndarray, fs: float = 6.55) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.810), 'e_mid': band_energy(freqs,psd,0.810,2.220), 'e_high': band_energy(freqs,psd,2.220, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_52(roll_series: np.ndarray, fs: float = 6.60) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.820), 'e_mid': band_energy(freqs,psd,0.820,2.240), 'e_high': band_energy(freqs,psd,2.240, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_53(roll_series: np.ndarray, fs: float = 6.65) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.830), 'e_mid': band_energy(freqs,psd,0.830,2.260), 'e_high': band_energy(freqs,psd,2.260, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_54(roll_series: np.ndarray, fs: float = 6.70) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.840), 'e_mid': band_energy(freqs,psd,0.840,2.280), 'e_high': band_energy(freqs,psd,2.280, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_55(roll_series: np.ndarray, fs: float = 6.75) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.850), 'e_mid': band_energy(freqs,psd,0.850,2.300), 'e_high': band_energy(freqs,psd,2.300, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_56(roll_series: np.ndarray, fs: float = 6.80) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.860), 'e_mid': band_energy(freqs,psd,0.860,2.320), 'e_high': band_energy(freqs,psd,2.320, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_57(roll_series: np.ndarray, fs: float = 6.85) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.870), 'e_mid': band_energy(freqs,psd,0.870,2.340), 'e_high': band_energy(freqs,psd,2.340, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_58(roll_series: np.ndarray, fs: float = 6.90) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.880), 'e_mid': band_energy(freqs,psd,0.880,2.360), 'e_high': band_energy(freqs,psd,2.360, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_59(roll_series: np.ndarray, fs: float = 6.95) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.890), 'e_mid': band_energy(freqs,psd,0.890,2.380), 'e_high': band_energy(freqs,psd,2.380, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_60(roll_series: np.ndarray, fs: float = 7.00) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.900), 'e_mid': band_energy(freqs,psd,0.900,2.400), 'e_high': band_energy(freqs,psd,2.400, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_61(roll_series: np.ndarray, fs: float = 7.05) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.910), 'e_mid': band_energy(freqs,psd,0.910,2.420), 'e_high': band_energy(freqs,psd,2.420, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_62(roll_series: np.ndarray, fs: float = 7.10) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.920), 'e_mid': band_energy(freqs,psd,0.920,2.440), 'e_high': band_energy(freqs,psd,2.440, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_63(roll_series: np.ndarray, fs: float = 7.15) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.930), 'e_mid': band_energy(freqs,psd,0.930,2.460), 'e_high': band_energy(freqs,psd,2.460, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_64(roll_series: np.ndarray, fs: float = 7.20) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.940), 'e_mid': band_energy(freqs,psd,0.940,2.480), 'e_high': band_energy(freqs,psd,2.480, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_65(roll_series: np.ndarray, fs: float = 7.25) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.950), 'e_mid': band_energy(freqs,psd,0.950,2.500), 'e_high': band_energy(freqs,psd,2.500, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_66(roll_series: np.ndarray, fs: float = 7.30) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.960), 'e_mid': band_energy(freqs,psd,0.960,2.520), 'e_high': band_energy(freqs,psd,2.520, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_67(roll_series: np.ndarray, fs: float = 7.35) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.970), 'e_mid': band_energy(freqs,psd,0.970,2.540), 'e_high': band_energy(freqs,psd,2.540, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_68(roll_series: np.ndarray, fs: float = 7.40) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.980), 'e_mid': band_energy(freqs,psd,0.980,2.560), 'e_high': band_energy(freqs,psd,2.560, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_69(roll_series: np.ndarray, fs: float = 7.45) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,0.990), 'e_mid': band_energy(freqs,psd,0.990,2.580), 'e_high': band_energy(freqs,psd,2.580, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_70(roll_series: np.ndarray, fs: float = 7.50) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.000), 'e_mid': band_energy(freqs,psd,1.000,2.600), 'e_high': band_energy(freqs,psd,2.600, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_71(roll_series: np.ndarray, fs: float = 7.55) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.010), 'e_mid': band_energy(freqs,psd,1.010,2.620), 'e_high': band_energy(freqs,psd,2.620, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_72(roll_series: np.ndarray, fs: float = 7.60) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.020), 'e_mid': band_energy(freqs,psd,1.020,2.640), 'e_high': band_energy(freqs,psd,2.640, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_73(roll_series: np.ndarray, fs: float = 7.65) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.030), 'e_mid': band_energy(freqs,psd,1.030,2.660), 'e_high': band_energy(freqs,psd,2.660, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_74(roll_series: np.ndarray, fs: float = 7.70) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.040), 'e_mid': band_energy(freqs,psd,1.040,2.680), 'e_high': band_energy(freqs,psd,2.680, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_75(roll_series: np.ndarray, fs: float = 7.75) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.050), 'e_mid': band_energy(freqs,psd,1.050,2.700), 'e_high': band_energy(freqs,psd,2.700, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_76(roll_series: np.ndarray, fs: float = 7.80) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.060), 'e_mid': band_energy(freqs,psd,1.060,2.720), 'e_high': band_energy(freqs,psd,2.720, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_77(roll_series: np.ndarray, fs: float = 7.85) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.070), 'e_mid': band_energy(freqs,psd,1.070,2.740), 'e_high': band_energy(freqs,psd,2.740, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_78(roll_series: np.ndarray, fs: float = 7.90) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.080), 'e_mid': band_energy(freqs,psd,1.080,2.760), 'e_high': band_energy(freqs,psd,2.760, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}

def vibration_features_79(roll_series: np.ndarray, fs: float = 7.95) -> dict:
    x = np.asarray(roll_series, dtype=np.float64).ravel()
    if x.size < 16: return {'ok': False}
    freqs, psd = welch_psd(x, fs)
    return {'ok': True, 'e_low': band_energy(freqs,psd,0.0,1.090), 'e_mid': band_energy(freqs,psd,1.090,2.780), 'e_high': band_energy(freqs,psd,2.780, fs/2), 'peak_hz': float(freqs[int(np.argmax(psd))])}
