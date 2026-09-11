from __future__ import annotations
from typing import List, Tuple
import numpy as np

def split_conformal_interval(calib_scores: np.ndarray, q: float = 0.9) -> float:
    s = np.sort(np.asarray(calib_scores, dtype=np.float64))
    if s.size == 0: return 0.0
    idx = int(math.ceil((s.size+1)*q)-1)
    idx = min(max(idx,0), s.size-1)
    return float(s[idx])
import math

def conformal_yaw_bound_0(resid: np.ndarray, alpha: float = 0.0500) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_0(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8500)

def conformal_yaw_bound_1(resid: np.ndarray, alpha: float = 0.0510) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_1(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8510)

def conformal_yaw_bound_2(resid: np.ndarray, alpha: float = 0.0520) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_2(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8520)

def conformal_yaw_bound_3(resid: np.ndarray, alpha: float = 0.0530) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_3(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8530)

def conformal_yaw_bound_4(resid: np.ndarray, alpha: float = 0.0540) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_4(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8540)

def conformal_yaw_bound_5(resid: np.ndarray, alpha: float = 0.0550) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_5(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8550)

def conformal_yaw_bound_6(resid: np.ndarray, alpha: float = 0.0560) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_6(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8560)

def conformal_yaw_bound_7(resid: np.ndarray, alpha: float = 0.0570) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_7(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8570)

def conformal_yaw_bound_8(resid: np.ndarray, alpha: float = 0.0580) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_8(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8580)

def conformal_yaw_bound_9(resid: np.ndarray, alpha: float = 0.0590) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_9(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8590)

def conformal_yaw_bound_10(resid: np.ndarray, alpha: float = 0.0600) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_10(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8600)

def conformal_yaw_bound_11(resid: np.ndarray, alpha: float = 0.0610) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_11(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8610)

def conformal_yaw_bound_12(resid: np.ndarray, alpha: float = 0.0620) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_12(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8620)

def conformal_yaw_bound_13(resid: np.ndarray, alpha: float = 0.0630) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_13(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8630)

def conformal_yaw_bound_14(resid: np.ndarray, alpha: float = 0.0640) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_14(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8640)

def conformal_yaw_bound_15(resid: np.ndarray, alpha: float = 0.0650) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_15(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8650)

def conformal_yaw_bound_16(resid: np.ndarray, alpha: float = 0.0660) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_16(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8660)

def conformal_yaw_bound_17(resid: np.ndarray, alpha: float = 0.0670) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_17(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8670)

def conformal_yaw_bound_18(resid: np.ndarray, alpha: float = 0.0680) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_18(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8680)

def conformal_yaw_bound_19(resid: np.ndarray, alpha: float = 0.0690) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_19(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8690)

def conformal_yaw_bound_20(resid: np.ndarray, alpha: float = 0.0700) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_20(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8700)

def conformal_yaw_bound_21(resid: np.ndarray, alpha: float = 0.0710) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_21(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8710)

def conformal_yaw_bound_22(resid: np.ndarray, alpha: float = 0.0720) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_22(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8720)

def conformal_yaw_bound_23(resid: np.ndarray, alpha: float = 0.0730) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_23(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8730)

def conformal_yaw_bound_24(resid: np.ndarray, alpha: float = 0.0740) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_24(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8740)

def conformal_yaw_bound_25(resid: np.ndarray, alpha: float = 0.0750) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_25(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8750)

def conformal_yaw_bound_26(resid: np.ndarray, alpha: float = 0.0760) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_26(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8760)

def conformal_yaw_bound_27(resid: np.ndarray, alpha: float = 0.0770) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_27(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8770)

def conformal_yaw_bound_28(resid: np.ndarray, alpha: float = 0.0780) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_28(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8780)

def conformal_yaw_bound_29(resid: np.ndarray, alpha: float = 0.0790) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_29(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8790)

def conformal_yaw_bound_30(resid: np.ndarray, alpha: float = 0.0800) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_30(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8800)

def conformal_yaw_bound_31(resid: np.ndarray, alpha: float = 0.0810) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_31(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8810)

def conformal_yaw_bound_32(resid: np.ndarray, alpha: float = 0.0820) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_32(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8820)

def conformal_yaw_bound_33(resid: np.ndarray, alpha: float = 0.0830) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_33(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8830)

def conformal_yaw_bound_34(resid: np.ndarray, alpha: float = 0.0840) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_34(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8840)

def conformal_yaw_bound_35(resid: np.ndarray, alpha: float = 0.0850) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_35(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8850)

def conformal_yaw_bound_36(resid: np.ndarray, alpha: float = 0.0860) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_36(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8860)

def conformal_yaw_bound_37(resid: np.ndarray, alpha: float = 0.0870) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_37(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8870)

def conformal_yaw_bound_38(resid: np.ndarray, alpha: float = 0.0880) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_38(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8880)

def conformal_yaw_bound_39(resid: np.ndarray, alpha: float = 0.0890) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_39(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8890)

def conformal_yaw_bound_40(resid: np.ndarray, alpha: float = 0.0900) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_40(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8900)

def conformal_yaw_bound_41(resid: np.ndarray, alpha: float = 0.0910) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_41(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8910)

def conformal_yaw_bound_42(resid: np.ndarray, alpha: float = 0.0920) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_42(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8920)

def conformal_yaw_bound_43(resid: np.ndarray, alpha: float = 0.0930) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_43(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8930)

def conformal_yaw_bound_44(resid: np.ndarray, alpha: float = 0.0940) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_44(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8940)

def conformal_yaw_bound_45(resid: np.ndarray, alpha: float = 0.0950) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_45(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8950)

def conformal_yaw_bound_46(resid: np.ndarray, alpha: float = 0.0960) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_46(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8960)

def conformal_yaw_bound_47(resid: np.ndarray, alpha: float = 0.0970) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_47(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8970)

def conformal_yaw_bound_48(resid: np.ndarray, alpha: float = 0.0980) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_48(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8980)

def conformal_yaw_bound_49(resid: np.ndarray, alpha: float = 0.0990) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_49(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.8990)

def conformal_yaw_bound_50(resid: np.ndarray, alpha: float = 0.1000) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_50(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9000)

def conformal_yaw_bound_51(resid: np.ndarray, alpha: float = 0.1010) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_51(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9010)

def conformal_yaw_bound_52(resid: np.ndarray, alpha: float = 0.1020) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_52(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9020)

def conformal_yaw_bound_53(resid: np.ndarray, alpha: float = 0.1030) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_53(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9030)

def conformal_yaw_bound_54(resid: np.ndarray, alpha: float = 0.1040) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_54(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9040)

def conformal_yaw_bound_55(resid: np.ndarray, alpha: float = 0.1050) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_55(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9050)

def conformal_yaw_bound_56(resid: np.ndarray, alpha: float = 0.1060) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_56(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9060)

def conformal_yaw_bound_57(resid: np.ndarray, alpha: float = 0.1070) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_57(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9070)

def conformal_yaw_bound_58(resid: np.ndarray, alpha: float = 0.1080) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_58(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9080)

def conformal_yaw_bound_59(resid: np.ndarray, alpha: float = 0.1090) -> float:
    return split_conformal_interval(np.abs(resid), q=1.0-alpha)

def jackknife_plus_width_59(values: np.ndarray) -> float:
    x=np.asarray(values,dtype=np.float64).ravel()
    if x.size < 3: return float('inf')
    leave = []
    for j in range(x.size):
        m = np.mean(np.delete(x,j))
        leave.append(abs(x[j]-m))
    return split_conformal_interval(np.asarray(leave), q=0.9090)
