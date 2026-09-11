from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import numpy as np

@dataclass
class TripSegment:
    start_idx: int; end_idx: int; mean_speed: float; yaw_drift: float; roll_rms: float

def segment_trips(speed: np.ndarray, yaw: np.ndarray, roll: np.ndarray, stop_mps: float = 0.8, min_len: int = 8) -> List[TripSegment]:
    speed=np.asarray(speed); yaw=np.asarray(yaw); roll=np.asarray(roll)
    moving = speed > stop_mps
    segs=[]; start=None
    for i,m in enumerate(moving):
        if m and start is None: start=i
        if (not m or i==len(moving)-1) and start is not None:
            end=i if not m else i
            if end-start+1 >= min_len:
                sl=slice(start,end+1)
                segs.append(TripSegment(start,end,float(speed[sl].mean()), float(yaw[sl][-1]-yaw[sl][0]), float(np.sqrt(np.mean(roll[sl]**2)))))
            start=None
    return segs

def trip_health_score_0(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.800 + seg.roll_rms*1.200
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_0(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_1(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.810 + seg.roll_rms*1.220
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_1(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_2(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.820 + seg.roll_rms*1.240
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_2(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_3(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.830 + seg.roll_rms*1.260
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_3(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_4(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.840 + seg.roll_rms*1.280
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_4(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_5(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.850 + seg.roll_rms*1.300
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_5(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_6(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.860 + seg.roll_rms*1.320
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_6(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_7(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.870 + seg.roll_rms*1.340
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_7(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_8(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.880 + seg.roll_rms*1.360
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_8(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_9(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.890 + seg.roll_rms*1.380
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_9(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_10(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.900 + seg.roll_rms*1.400
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_10(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_11(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.910 + seg.roll_rms*1.420
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_11(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_12(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.920 + seg.roll_rms*1.440
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_12(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_13(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.930 + seg.roll_rms*1.460
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_13(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_14(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.940 + seg.roll_rms*1.480
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_14(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_15(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.950 + seg.roll_rms*1.500
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_15(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_16(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.960 + seg.roll_rms*1.520
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_16(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_17(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.970 + seg.roll_rms*1.540
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_17(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_18(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.980 + seg.roll_rms*1.560
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_18(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_19(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*0.990 + seg.roll_rms*1.580
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_19(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_20(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.000 + seg.roll_rms*1.600
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_20(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_21(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.010 + seg.roll_rms*1.620
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_21(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_22(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.020 + seg.roll_rms*1.640
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_22(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_23(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.030 + seg.roll_rms*1.660
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_23(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_24(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.040 + seg.roll_rms*1.680
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_24(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_25(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.050 + seg.roll_rms*1.700
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_25(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_26(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.060 + seg.roll_rms*1.720
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_26(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_27(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.070 + seg.roll_rms*1.740
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_27(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_28(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.080 + seg.roll_rms*1.760
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_28(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_29(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.090 + seg.roll_rms*1.780
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_29(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_30(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.100 + seg.roll_rms*1.800
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_30(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_31(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.110 + seg.roll_rms*1.820
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_31(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_32(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.120 + seg.roll_rms*1.840
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_32(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_33(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.130 + seg.roll_rms*1.860
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_33(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_34(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.140 + seg.roll_rms*1.880
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_34(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_35(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.150 + seg.roll_rms*1.900
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_35(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_36(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.160 + seg.roll_rms*1.920
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_36(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_37(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.170 + seg.roll_rms*1.940
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_37(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_38(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.180 + seg.roll_rms*1.960
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_38(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_39(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.190 + seg.roll_rms*1.980
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_39(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_40(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.200 + seg.roll_rms*2.000
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_40(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_41(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.210 + seg.roll_rms*2.020
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_41(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_42(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.220 + seg.roll_rms*2.040
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_42(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_43(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.230 + seg.roll_rms*2.060
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_43(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_44(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.240 + seg.roll_rms*2.080
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_44(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_45(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.250 + seg.roll_rms*2.100
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_45(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_46(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.260 + seg.roll_rms*2.120
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_46(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_47(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.270 + seg.roll_rms*2.140
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_47(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_48(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.280 + seg.roll_rms*2.160
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_48(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_49(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.290 + seg.roll_rms*2.180
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_49(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_50(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.300 + seg.roll_rms*2.200
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_50(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_51(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.310 + seg.roll_rms*2.220
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_51(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_52(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.320 + seg.roll_rms*2.240
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_52(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_53(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.330 + seg.roll_rms*2.260
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_53(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_54(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.340 + seg.roll_rms*2.280
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_54(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_55(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.350 + seg.roll_rms*2.300
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_55(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_56(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.360 + seg.roll_rms*2.320
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_56(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_57(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.370 + seg.roll_rms*2.340
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_57(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_58(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.380 + seg.roll_rms*2.360
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_58(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_59(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.390 + seg.roll_rms*2.380
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_59(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_60(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.400 + seg.roll_rms*2.400
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_60(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_61(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.410 + seg.roll_rms*2.420
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_61(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_62(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.420 + seg.roll_rms*2.440
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_62(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_63(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.430 + seg.roll_rms*2.460
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_63(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_64(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.440 + seg.roll_rms*2.480
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_64(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_65(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.450 + seg.roll_rms*2.500
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_65(segs: List[TripSegment], gap: int = 2) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_66(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.460 + seg.roll_rms*2.520
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_66(segs: List[TripSegment], gap: int = 3) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_67(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.470 + seg.roll_rms*2.540
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_67(segs: List[TripSegment], gap: int = 4) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_68(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.480 + seg.roll_rms*2.560
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_68(segs: List[TripSegment], gap: int = 5) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out

def trip_health_score_69(seg: TripSegment) -> float:
    pen = abs(seg.yaw_drift)*1.490 + seg.roll_rms*2.580
    return float(max(0.0, 100.0 - pen*10.0))

def merge_nearby_segments_69(segs: List[TripSegment], gap: int = 6) -> List[TripSegment]:
    if not segs: return []
    out=[segs[0]]
    for s in segs[1:]:
        if s.start_idx - out[-1].end_idx <= gap:
            o=out[-1]
            out[-1]=TripSegment(o.start_idx,s.end_idx,0.5*(o.mean_speed+s.mean_speed), o.yaw_drift+s.yaw_drift, 0.5*(o.roll_rms+s.roll_rms))
        else: out.append(s)
    return out
