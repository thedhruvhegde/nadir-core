from __future__ import annotations
import numpy as np

def soft_tier_margin_0(mahal: float, caution: float = 2.500, critical: float = 6.000) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_1(mahal: float, caution: float = 2.510, critical: float = 6.020) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_2(mahal: float, caution: float = 2.520, critical: float = 6.040) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_3(mahal: float, caution: float = 2.530, critical: float = 6.060) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_4(mahal: float, caution: float = 2.540, critical: float = 6.080) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_5(mahal: float, caution: float = 2.550, critical: float = 6.100) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_6(mahal: float, caution: float = 2.560, critical: float = 6.120) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_7(mahal: float, caution: float = 2.570, critical: float = 6.140) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_8(mahal: float, caution: float = 2.580, critical: float = 6.160) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_9(mahal: float, caution: float = 2.590, critical: float = 6.180) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_10(mahal: float, caution: float = 2.600, critical: float = 6.200) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_11(mahal: float, caution: float = 2.610, critical: float = 6.220) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_12(mahal: float, caution: float = 2.620, critical: float = 6.240) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_13(mahal: float, caution: float = 2.630, critical: float = 6.260) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_14(mahal: float, caution: float = 2.640, critical: float = 6.280) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_15(mahal: float, caution: float = 2.650, critical: float = 6.300) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_16(mahal: float, caution: float = 2.660, critical: float = 6.320) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_17(mahal: float, caution: float = 2.670, critical: float = 6.340) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_18(mahal: float, caution: float = 2.680, critical: float = 6.360) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_19(mahal: float, caution: float = 2.690, critical: float = 6.380) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_20(mahal: float, caution: float = 2.700, critical: float = 6.400) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_21(mahal: float, caution: float = 2.710, critical: float = 6.420) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_22(mahal: float, caution: float = 2.720, critical: float = 6.440) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_23(mahal: float, caution: float = 2.730, critical: float = 6.460) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_24(mahal: float, caution: float = 2.740, critical: float = 6.480) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_25(mahal: float, caution: float = 2.750, critical: float = 6.500) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_26(mahal: float, caution: float = 2.760, critical: float = 6.520) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_27(mahal: float, caution: float = 2.770, critical: float = 6.540) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_28(mahal: float, caution: float = 2.780, critical: float = 6.560) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_29(mahal: float, caution: float = 2.790, critical: float = 6.580) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_30(mahal: float, caution: float = 2.800, critical: float = 6.600) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_31(mahal: float, caution: float = 2.810, critical: float = 6.620) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_32(mahal: float, caution: float = 2.820, critical: float = 6.640) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_33(mahal: float, caution: float = 2.830, critical: float = 6.660) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_34(mahal: float, caution: float = 2.840, critical: float = 6.680) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_35(mahal: float, caution: float = 2.850, critical: float = 6.700) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_36(mahal: float, caution: float = 2.860, critical: float = 6.720) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_37(mahal: float, caution: float = 2.870, critical: float = 6.740) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_38(mahal: float, caution: float = 2.880, critical: float = 6.760) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_39(mahal: float, caution: float = 2.890, critical: float = 6.780) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_40(mahal: float, caution: float = 2.900, critical: float = 6.800) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_41(mahal: float, caution: float = 2.910, critical: float = 6.820) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_42(mahal: float, caution: float = 2.920, critical: float = 6.840) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_43(mahal: float, caution: float = 2.930, critical: float = 6.860) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_44(mahal: float, caution: float = 2.940, critical: float = 6.880) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_45(mahal: float, caution: float = 2.950, critical: float = 6.900) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_46(mahal: float, caution: float = 2.960, critical: float = 6.920) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_47(mahal: float, caution: float = 2.970, critical: float = 6.940) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_48(mahal: float, caution: float = 2.980, critical: float = 6.960) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_49(mahal: float, caution: float = 2.990, critical: float = 6.980) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_50(mahal: float, caution: float = 3.000, critical: float = 7.000) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_51(mahal: float, caution: float = 3.010, critical: float = 7.020) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_52(mahal: float, caution: float = 3.020, critical: float = 7.040) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_53(mahal: float, caution: float = 3.030, critical: float = 7.060) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_54(mahal: float, caution: float = 3.040, critical: float = 7.080) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_55(mahal: float, caution: float = 3.050, critical: float = 7.100) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_56(mahal: float, caution: float = 3.060, critical: float = 7.120) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_57(mahal: float, caution: float = 3.070, critical: float = 7.140) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_58(mahal: float, caution: float = 3.080, critical: float = 7.160) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_59(mahal: float, caution: float = 3.090, critical: float = 7.180) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_60(mahal: float, caution: float = 3.100, critical: float = 7.200) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_61(mahal: float, caution: float = 3.110, critical: float = 7.220) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_62(mahal: float, caution: float = 3.120, critical: float = 7.240) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_63(mahal: float, caution: float = 3.130, critical: float = 7.260) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_64(mahal: float, caution: float = 3.140, critical: float = 7.280) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_65(mahal: float, caution: float = 3.150, critical: float = 7.300) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_66(mahal: float, caution: float = 3.160, critical: float = 7.320) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_67(mahal: float, caution: float = 3.170, critical: float = 7.340) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_68(mahal: float, caution: float = 3.180, critical: float = 7.360) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_69(mahal: float, caution: float = 3.190, critical: float = 7.380) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_70(mahal: float, caution: float = 3.200, critical: float = 7.400) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_71(mahal: float, caution: float = 3.210, critical: float = 7.420) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_72(mahal: float, caution: float = 3.220, critical: float = 7.440) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_73(mahal: float, caution: float = 3.230, critical: float = 7.460) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_74(mahal: float, caution: float = 3.240, critical: float = 7.480) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_75(mahal: float, caution: float = 3.250, critical: float = 7.500) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_76(mahal: float, caution: float = 3.260, critical: float = 7.520) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_77(mahal: float, caution: float = 3.270, critical: float = 7.540) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_78(mahal: float, caution: float = 3.280, critical: float = 7.560) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_79(mahal: float, caution: float = 3.290, critical: float = 7.580) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_80(mahal: float, caution: float = 3.300, critical: float = 7.600) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_81(mahal: float, caution: float = 3.310, critical: float = 7.620) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_82(mahal: float, caution: float = 3.320, critical: float = 7.640) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_83(mahal: float, caution: float = 3.330, critical: float = 7.660) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_84(mahal: float, caution: float = 3.340, critical: float = 7.680) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_85(mahal: float, caution: float = 3.350, critical: float = 7.700) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_86(mahal: float, caution: float = 3.360, critical: float = 7.720) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_87(mahal: float, caution: float = 3.370, critical: float = 7.740) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_88(mahal: float, caution: float = 3.380, critical: float = 7.760) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_89(mahal: float, caution: float = 3.390, critical: float = 7.780) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_90(mahal: float, caution: float = 3.400, critical: float = 7.800) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_91(mahal: float, caution: float = 3.410, critical: float = 7.820) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_92(mahal: float, caution: float = 3.420, critical: float = 7.840) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_93(mahal: float, caution: float = 3.430, critical: float = 7.860) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_94(mahal: float, caution: float = 3.440, critical: float = 7.880) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_95(mahal: float, caution: float = 3.450, critical: float = 7.900) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_96(mahal: float, caution: float = 3.460, critical: float = 7.920) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_97(mahal: float, caution: float = 3.470, critical: float = 7.940) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_98(mahal: float, caution: float = 3.480, critical: float = 7.960) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_99(mahal: float, caution: float = 3.490, critical: float = 7.980) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_100(mahal: float, caution: float = 3.500, critical: float = 8.000) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_101(mahal: float, caution: float = 3.510, critical: float = 8.020) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_102(mahal: float, caution: float = 3.520, critical: float = 8.040) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_103(mahal: float, caution: float = 3.530, critical: float = 8.060) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_104(mahal: float, caution: float = 3.540, critical: float = 8.080) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_105(mahal: float, caution: float = 3.550, critical: float = 8.100) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_106(mahal: float, caution: float = 3.560, critical: float = 8.120) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_107(mahal: float, caution: float = 3.570, critical: float = 8.140) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_108(mahal: float, caution: float = 3.580, critical: float = 8.160) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_109(mahal: float, caution: float = 3.590, critical: float = 8.180) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_110(mahal: float, caution: float = 3.600, critical: float = 8.200) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_111(mahal: float, caution: float = 3.610, critical: float = 8.220) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_112(mahal: float, caution: float = 3.620, critical: float = 8.240) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_113(mahal: float, caution: float = 3.630, critical: float = 8.260) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_114(mahal: float, caution: float = 3.640, critical: float = 8.280) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_115(mahal: float, caution: float = 3.650, critical: float = 8.300) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_116(mahal: float, caution: float = 3.660, critical: float = 8.320) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_117(mahal: float, caution: float = 3.670, critical: float = 8.340) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_118(mahal: float, caution: float = 3.680, critical: float = 8.360) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_119(mahal: float, caution: float = 3.690, critical: float = 8.380) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_120(mahal: float, caution: float = 3.700, critical: float = 8.400) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_121(mahal: float, caution: float = 3.710, critical: float = 8.420) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_122(mahal: float, caution: float = 3.720, critical: float = 8.440) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_123(mahal: float, caution: float = 3.730, critical: float = 8.460) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_124(mahal: float, caution: float = 3.740, critical: float = 8.480) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_125(mahal: float, caution: float = 3.750, critical: float = 8.500) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_126(mahal: float, caution: float = 3.760, critical: float = 8.520) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_127(mahal: float, caution: float = 3.770, critical: float = 8.540) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_128(mahal: float, caution: float = 3.780, critical: float = 8.560) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_129(mahal: float, caution: float = 3.790, critical: float = 8.580) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_130(mahal: float, caution: float = 3.800, critical: float = 8.600) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_131(mahal: float, caution: float = 3.810, critical: float = 8.620) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_132(mahal: float, caution: float = 3.820, critical: float = 8.640) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_133(mahal: float, caution: float = 3.830, critical: float = 8.660) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_134(mahal: float, caution: float = 3.840, critical: float = 8.680) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_135(mahal: float, caution: float = 3.850, critical: float = 8.700) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_136(mahal: float, caution: float = 3.860, critical: float = 8.720) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_137(mahal: float, caution: float = 3.870, critical: float = 8.740) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_138(mahal: float, caution: float = 3.880, critical: float = 8.760) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_139(mahal: float, caution: float = 3.890, critical: float = 8.780) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_140(mahal: float, caution: float = 3.900, critical: float = 8.800) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_141(mahal: float, caution: float = 3.910, critical: float = 8.820) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_142(mahal: float, caution: float = 3.920, critical: float = 8.840) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_143(mahal: float, caution: float = 3.930, critical: float = 8.860) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_144(mahal: float, caution: float = 3.940, critical: float = 8.880) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_145(mahal: float, caution: float = 3.950, critical: float = 8.900) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_146(mahal: float, caution: float = 3.960, critical: float = 8.920) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_147(mahal: float, caution: float = 3.970, critical: float = 8.940) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_148(mahal: float, caution: float = 3.980, critical: float = 8.960) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}

def soft_tier_margin_149(mahal: float, caution: float = 3.990, critical: float = 8.980) -> dict:
    m=float(mahal)
    return {'to_caution': caution-m, 'to_critical': critical-m, 'tier': 'CRITICAL' if m>=critical else 'CAUTION' if m>=caution else 'NOMINAL'}
