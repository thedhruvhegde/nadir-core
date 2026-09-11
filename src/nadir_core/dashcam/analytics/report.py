from __future__ import annotations
from typing import Dict, List
from nadir_core.dashcam.health import HealthSeries

def render_text_report(series: HealthSeries) -> str:
    s = series.summary(); lines=['NADIR dashcam health report','='*28]
    for k,v in s.items(): lines.append(f'{k}: {v}')
    if series.cusum_triggered: lines.append('alert: CUSUM yaw shift')
    if series.gradual_slope_alert: lines.append('alert: gradual yaw slope')
    lines.append('boundary: vision mount health only')
    return '\n'.join(lines)

def advice_card_0(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.40: bits.append('check windshield mount yaw')
    if abs(roll)>0.50: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.60: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_1(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.42: bits.append('check windshield mount yaw')
    if abs(roll)>0.52: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.62: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_2(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.44: bits.append('check windshield mount yaw')
    if abs(roll)>0.54: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.64: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_3(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.46: bits.append('check windshield mount yaw')
    if abs(roll)>0.56: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.66: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_4(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.48: bits.append('check windshield mount yaw')
    if abs(roll)>0.58: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.68: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_5(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.50: bits.append('check windshield mount yaw')
    if abs(roll)>0.60: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.70: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_6(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.52: bits.append('check windshield mount yaw')
    if abs(roll)>0.62: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.72: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_7(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.54: bits.append('check windshield mount yaw')
    if abs(roll)>0.64: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.74: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_8(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.56: bits.append('check windshield mount yaw')
    if abs(roll)>0.66: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.76: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_9(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.58: bits.append('check windshield mount yaw')
    if abs(roll)>0.68: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.78: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_10(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.60: bits.append('check windshield mount yaw')
    if abs(roll)>0.70: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.80: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_11(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.62: bits.append('check windshield mount yaw')
    if abs(roll)>0.72: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.82: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_12(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.64: bits.append('check windshield mount yaw')
    if abs(roll)>0.74: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.84: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_13(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.66: bits.append('check windshield mount yaw')
    if abs(roll)>0.76: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.86: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_14(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.68: bits.append('check windshield mount yaw')
    if abs(roll)>0.78: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.88: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_15(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.70: bits.append('check windshield mount yaw')
    if abs(roll)>0.80: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.90: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_16(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.72: bits.append('check windshield mount yaw')
    if abs(roll)>0.82: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.92: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_17(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.74: bits.append('check windshield mount yaw')
    if abs(roll)>0.84: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.94: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_18(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.76: bits.append('check windshield mount yaw')
    if abs(roll)>0.86: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.96: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_19(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.78: bits.append('check windshield mount yaw')
    if abs(roll)>0.88: bits.append('check roll / adhesive sag')
    if abs(pitch)>0.98: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_20(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.80: bits.append('check windshield mount yaw')
    if abs(roll)>0.90: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.00: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_21(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.82: bits.append('check windshield mount yaw')
    if abs(roll)>0.92: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.02: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_22(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.84: bits.append('check windshield mount yaw')
    if abs(roll)>0.94: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.04: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_23(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.86: bits.append('check windshield mount yaw')
    if abs(roll)>0.96: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.06: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_24(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.88: bits.append('check windshield mount yaw')
    if abs(roll)>0.98: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.08: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_25(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.90: bits.append('check windshield mount yaw')
    if abs(roll)>1.00: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.10: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_26(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.92: bits.append('check windshield mount yaw')
    if abs(roll)>1.02: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.12: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_27(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.94: bits.append('check windshield mount yaw')
    if abs(roll)>1.04: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.14: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_28(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.96: bits.append('check windshield mount yaw')
    if abs(roll)>1.06: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.16: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_29(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>0.98: bits.append('check windshield mount yaw')
    if abs(roll)>1.08: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.18: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_30(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.00: bits.append('check windshield mount yaw')
    if abs(roll)>1.10: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.20: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_31(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.02: bits.append('check windshield mount yaw')
    if abs(roll)>1.12: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.22: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_32(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.04: bits.append('check windshield mount yaw')
    if abs(roll)>1.14: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.24: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_33(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.06: bits.append('check windshield mount yaw')
    if abs(roll)>1.16: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.26: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_34(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.08: bits.append('check windshield mount yaw')
    if abs(roll)>1.18: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.28: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_35(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.10: bits.append('check windshield mount yaw')
    if abs(roll)>1.20: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.30: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_36(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.12: bits.append('check windshield mount yaw')
    if abs(roll)>1.22: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.32: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_37(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.14: bits.append('check windshield mount yaw')
    if abs(roll)>1.24: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.34: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_38(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.16: bits.append('check windshield mount yaw')
    if abs(roll)>1.26: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.36: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_39(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.18: bits.append('check windshield mount yaw')
    if abs(roll)>1.28: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.38: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_40(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.20: bits.append('check windshield mount yaw')
    if abs(roll)>1.30: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.40: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_41(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.22: bits.append('check windshield mount yaw')
    if abs(roll)>1.32: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.42: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_42(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.24: bits.append('check windshield mount yaw')
    if abs(roll)>1.34: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.44: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_43(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.26: bits.append('check windshield mount yaw')
    if abs(roll)>1.36: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.46: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_44(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.28: bits.append('check windshield mount yaw')
    if abs(roll)>1.38: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.48: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_45(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.30: bits.append('check windshield mount yaw')
    if abs(roll)>1.40: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.50: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_46(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.32: bits.append('check windshield mount yaw')
    if abs(roll)>1.42: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.52: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_47(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.34: bits.append('check windshield mount yaw')
    if abs(roll)>1.44: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.54: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_48(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.36: bits.append('check windshield mount yaw')
    if abs(roll)>1.46: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.56: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_49(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.38: bits.append('check windshield mount yaw')
    if abs(roll)>1.48: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.58: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_50(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.40: bits.append('check windshield mount yaw')
    if abs(roll)>1.50: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.60: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_51(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.42: bits.append('check windshield mount yaw')
    if abs(roll)>1.52: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.62: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_52(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.44: bits.append('check windshield mount yaw')
    if abs(roll)>1.54: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.64: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_53(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.46: bits.append('check windshield mount yaw')
    if abs(roll)>1.56: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.66: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_54(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.48: bits.append('check windshield mount yaw')
    if abs(roll)>1.58: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.68: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_55(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.50: bits.append('check windshield mount yaw')
    if abs(roll)>1.60: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.70: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_56(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.52: bits.append('check windshield mount yaw')
    if abs(roll)>1.62: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.72: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_57(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.54: bits.append('check windshield mount yaw')
    if abs(roll)>1.64: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.74: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_58(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.56: bits.append('check windshield mount yaw')
    if abs(roll)>1.66: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.76: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'

def advice_card_59(yaw: float, roll: float, pitch: float) -> str:
    bits=[]
    if abs(yaw)>1.58: bits.append('check windshield mount yaw')
    if abs(roll)>1.68: bits.append('check roll / adhesive sag')
    if abs(pitch)>1.78: bits.append('check pitch / suction cup creep')
    return '; '.join(bits) if bits else 'geometry nominal vs baseline'
