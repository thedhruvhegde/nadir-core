from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List
import numpy as np
from nadir_core.dashcam.sources.synthetic import make_road_frame

@dataclass
class Scenario:
    name: str; yaw: float; roll: float; pitch: float; n: int=40

def run_scenario(sc: Scenario, seed: int = 0) -> List[np.ndarray]:
    frames=[]
    for i in range(sc.n):
        f=i/max(1,sc.n-1)
        frames.append(make_road_frame(horizon_y=0.45+sc.pitch*f*0.04, roll_deg=sc.roll*f, yaw_shift_px=sc.yaw*f*8, seed=seed+i))
    return frames

SCENARIO_0 = Scenario(name='sc_0', yaw=0.000, roll=-0.150, pitch=-0.040, n=24)

def frames_scenario_0(seed: int = 0) -> List[np.ndarray]:
    return run_scenario(SCENARIO_0, seed=seed)

SCENARIO_1 = Scenario(name='sc_1', yaw=0.100, roll=-0.100, pitch=-0.020, n=25)

def frames_scenario_1(seed: int = 1) -> List[np.ndarray]:
    return run_scenario(SCENARIO_1, seed=seed)

SCENARIO_2 = Scenario(name='sc_2', yaw=0.200, roll=-0.050, pitch=0.000, n=26)

def frames_scenario_2(seed: int = 2) -> List[np.ndarray]:
    return run_scenario(SCENARIO_2, seed=seed)

SCENARIO_3 = Scenario(name='sc_3', yaw=0.300, roll=0.000, pitch=0.020, n=27)

def frames_scenario_3(seed: int = 3) -> List[np.ndarray]:
    return run_scenario(SCENARIO_3, seed=seed)

SCENARIO_4 = Scenario(name='sc_4', yaw=0.400, roll=0.050, pitch=0.040, n=28)

def frames_scenario_4(seed: int = 4) -> List[np.ndarray]:
    return run_scenario(SCENARIO_4, seed=seed)

SCENARIO_5 = Scenario(name='sc_5', yaw=0.500, roll=0.100, pitch=-0.040, n=29)

def frames_scenario_5(seed: int = 5) -> List[np.ndarray]:
    return run_scenario(SCENARIO_5, seed=seed)

SCENARIO_6 = Scenario(name='sc_6', yaw=0.600, roll=0.150, pitch=-0.020, n=30)

def frames_scenario_6(seed: int = 6) -> List[np.ndarray]:
    return run_scenario(SCENARIO_6, seed=seed)

SCENARIO_7 = Scenario(name='sc_7', yaw=0.700, roll=-0.150, pitch=0.000, n=31)

def frames_scenario_7(seed: int = 7) -> List[np.ndarray]:
    return run_scenario(SCENARIO_7, seed=seed)

SCENARIO_8 = Scenario(name='sc_8', yaw=0.800, roll=-0.100, pitch=0.020, n=32)

def frames_scenario_8(seed: int = 8) -> List[np.ndarray]:
    return run_scenario(SCENARIO_8, seed=seed)

SCENARIO_9 = Scenario(name='sc_9', yaw=0.900, roll=-0.050, pitch=0.040, n=33)

def frames_scenario_9(seed: int = 9) -> List[np.ndarray]:
    return run_scenario(SCENARIO_9, seed=seed)

SCENARIO_10 = Scenario(name='sc_10', yaw=1.000, roll=0.000, pitch=-0.040, n=34)

def frames_scenario_10(seed: int = 10) -> List[np.ndarray]:
    return run_scenario(SCENARIO_10, seed=seed)

SCENARIO_11 = Scenario(name='sc_11', yaw=1.100, roll=0.050, pitch=-0.020, n=35)

def frames_scenario_11(seed: int = 11) -> List[np.ndarray]:
    return run_scenario(SCENARIO_11, seed=seed)

SCENARIO_12 = Scenario(name='sc_12', yaw=1.200, roll=0.100, pitch=0.000, n=36)

def frames_scenario_12(seed: int = 12) -> List[np.ndarray]:
    return run_scenario(SCENARIO_12, seed=seed)

SCENARIO_13 = Scenario(name='sc_13', yaw=1.300, roll=0.150, pitch=0.020, n=37)

def frames_scenario_13(seed: int = 13) -> List[np.ndarray]:
    return run_scenario(SCENARIO_13, seed=seed)

SCENARIO_14 = Scenario(name='sc_14', yaw=1.400, roll=-0.150, pitch=0.040, n=38)

def frames_scenario_14(seed: int = 14) -> List[np.ndarray]:
    return run_scenario(SCENARIO_14, seed=seed)

SCENARIO_15 = Scenario(name='sc_15', yaw=1.500, roll=-0.100, pitch=-0.040, n=39)

def frames_scenario_15(seed: int = 15) -> List[np.ndarray]:
    return run_scenario(SCENARIO_15, seed=seed)

SCENARIO_16 = Scenario(name='sc_16', yaw=1.600, roll=-0.050, pitch=-0.020, n=40)

def frames_scenario_16(seed: int = 16) -> List[np.ndarray]:
    return run_scenario(SCENARIO_16, seed=seed)

SCENARIO_17 = Scenario(name='sc_17', yaw=1.700, roll=0.000, pitch=0.000, n=41)

def frames_scenario_17(seed: int = 17) -> List[np.ndarray]:
    return run_scenario(SCENARIO_17, seed=seed)

SCENARIO_18 = Scenario(name='sc_18', yaw=1.800, roll=0.050, pitch=0.020, n=42)

def frames_scenario_18(seed: int = 18) -> List[np.ndarray]:
    return run_scenario(SCENARIO_18, seed=seed)

SCENARIO_19 = Scenario(name='sc_19', yaw=1.900, roll=0.100, pitch=0.040, n=43)

def frames_scenario_19(seed: int = 19) -> List[np.ndarray]:
    return run_scenario(SCENARIO_19, seed=seed)

SCENARIO_20 = Scenario(name='sc_20', yaw=2.000, roll=0.150, pitch=-0.040, n=24)

def frames_scenario_20(seed: int = 20) -> List[np.ndarray]:
    return run_scenario(SCENARIO_20, seed=seed)

SCENARIO_21 = Scenario(name='sc_21', yaw=2.100, roll=-0.150, pitch=-0.020, n=25)

def frames_scenario_21(seed: int = 21) -> List[np.ndarray]:
    return run_scenario(SCENARIO_21, seed=seed)

SCENARIO_22 = Scenario(name='sc_22', yaw=2.200, roll=-0.100, pitch=0.000, n=26)

def frames_scenario_22(seed: int = 22) -> List[np.ndarray]:
    return run_scenario(SCENARIO_22, seed=seed)

SCENARIO_23 = Scenario(name='sc_23', yaw=2.300, roll=-0.050, pitch=0.020, n=27)

def frames_scenario_23(seed: int = 23) -> List[np.ndarray]:
    return run_scenario(SCENARIO_23, seed=seed)

SCENARIO_24 = Scenario(name='sc_24', yaw=2.400, roll=0.000, pitch=0.040, n=28)

def frames_scenario_24(seed: int = 24) -> List[np.ndarray]:
    return run_scenario(SCENARIO_24, seed=seed)

SCENARIO_25 = Scenario(name='sc_25', yaw=2.500, roll=0.050, pitch=-0.040, n=29)

def frames_scenario_25(seed: int = 25) -> List[np.ndarray]:
    return run_scenario(SCENARIO_25, seed=seed)

SCENARIO_26 = Scenario(name='sc_26', yaw=2.600, roll=0.100, pitch=-0.020, n=30)

def frames_scenario_26(seed: int = 26) -> List[np.ndarray]:
    return run_scenario(SCENARIO_26, seed=seed)

SCENARIO_27 = Scenario(name='sc_27', yaw=2.700, roll=0.150, pitch=0.000, n=31)

def frames_scenario_27(seed: int = 27) -> List[np.ndarray]:
    return run_scenario(SCENARIO_27, seed=seed)

SCENARIO_28 = Scenario(name='sc_28', yaw=2.800, roll=-0.150, pitch=0.020, n=32)

def frames_scenario_28(seed: int = 28) -> List[np.ndarray]:
    return run_scenario(SCENARIO_28, seed=seed)

SCENARIO_29 = Scenario(name='sc_29', yaw=2.900, roll=-0.100, pitch=0.040, n=33)

def frames_scenario_29(seed: int = 29) -> List[np.ndarray]:
    return run_scenario(SCENARIO_29, seed=seed)

SCENARIO_30 = Scenario(name='sc_30', yaw=3.000, roll=-0.050, pitch=-0.040, n=34)

def frames_scenario_30(seed: int = 30) -> List[np.ndarray]:
    return run_scenario(SCENARIO_30, seed=seed)

SCENARIO_31 = Scenario(name='sc_31', yaw=3.100, roll=0.000, pitch=-0.020, n=35)

def frames_scenario_31(seed: int = 31) -> List[np.ndarray]:
    return run_scenario(SCENARIO_31, seed=seed)

SCENARIO_32 = Scenario(name='sc_32', yaw=3.200, roll=0.050, pitch=0.000, n=36)

def frames_scenario_32(seed: int = 32) -> List[np.ndarray]:
    return run_scenario(SCENARIO_32, seed=seed)

SCENARIO_33 = Scenario(name='sc_33', yaw=3.300, roll=0.100, pitch=0.020, n=37)

def frames_scenario_33(seed: int = 33) -> List[np.ndarray]:
    return run_scenario(SCENARIO_33, seed=seed)

SCENARIO_34 = Scenario(name='sc_34', yaw=3.400, roll=0.150, pitch=0.040, n=38)

def frames_scenario_34(seed: int = 34) -> List[np.ndarray]:
    return run_scenario(SCENARIO_34, seed=seed)

SCENARIO_35 = Scenario(name='sc_35', yaw=3.500, roll=-0.150, pitch=-0.040, n=39)

def frames_scenario_35(seed: int = 35) -> List[np.ndarray]:
    return run_scenario(SCENARIO_35, seed=seed)

SCENARIO_36 = Scenario(name='sc_36', yaw=3.600, roll=-0.100, pitch=-0.020, n=40)

def frames_scenario_36(seed: int = 36) -> List[np.ndarray]:
    return run_scenario(SCENARIO_36, seed=seed)

SCENARIO_37 = Scenario(name='sc_37', yaw=3.700, roll=-0.050, pitch=0.000, n=41)

def frames_scenario_37(seed: int = 37) -> List[np.ndarray]:
    return run_scenario(SCENARIO_37, seed=seed)

SCENARIO_38 = Scenario(name='sc_38', yaw=3.800, roll=0.000, pitch=0.020, n=42)

def frames_scenario_38(seed: int = 38) -> List[np.ndarray]:
    return run_scenario(SCENARIO_38, seed=seed)

SCENARIO_39 = Scenario(name='sc_39', yaw=3.900, roll=0.050, pitch=0.040, n=43)

def frames_scenario_39(seed: int = 39) -> List[np.ndarray]:
    return run_scenario(SCENARIO_39, seed=seed)

SCENARIO_40 = Scenario(name='sc_40', yaw=4.000, roll=0.100, pitch=-0.040, n=24)

def frames_scenario_40(seed: int = 40) -> List[np.ndarray]:
    return run_scenario(SCENARIO_40, seed=seed)

SCENARIO_41 = Scenario(name='sc_41', yaw=4.100, roll=0.150, pitch=-0.020, n=25)

def frames_scenario_41(seed: int = 41) -> List[np.ndarray]:
    return run_scenario(SCENARIO_41, seed=seed)

SCENARIO_42 = Scenario(name='sc_42', yaw=4.200, roll=-0.150, pitch=0.000, n=26)

def frames_scenario_42(seed: int = 42) -> List[np.ndarray]:
    return run_scenario(SCENARIO_42, seed=seed)

SCENARIO_43 = Scenario(name='sc_43', yaw=4.300, roll=-0.100, pitch=0.020, n=27)

def frames_scenario_43(seed: int = 43) -> List[np.ndarray]:
    return run_scenario(SCENARIO_43, seed=seed)

SCENARIO_44 = Scenario(name='sc_44', yaw=4.400, roll=-0.050, pitch=0.040, n=28)

def frames_scenario_44(seed: int = 44) -> List[np.ndarray]:
    return run_scenario(SCENARIO_44, seed=seed)

SCENARIO_45 = Scenario(name='sc_45', yaw=4.500, roll=0.000, pitch=-0.040, n=29)

def frames_scenario_45(seed: int = 45) -> List[np.ndarray]:
    return run_scenario(SCENARIO_45, seed=seed)

SCENARIO_46 = Scenario(name='sc_46', yaw=4.600, roll=0.050, pitch=-0.020, n=30)

def frames_scenario_46(seed: int = 46) -> List[np.ndarray]:
    return run_scenario(SCENARIO_46, seed=seed)

SCENARIO_47 = Scenario(name='sc_47', yaw=4.700, roll=0.100, pitch=0.000, n=31)

def frames_scenario_47(seed: int = 47) -> List[np.ndarray]:
    return run_scenario(SCENARIO_47, seed=seed)

SCENARIO_48 = Scenario(name='sc_48', yaw=4.800, roll=0.150, pitch=0.020, n=32)

def frames_scenario_48(seed: int = 48) -> List[np.ndarray]:
    return run_scenario(SCENARIO_48, seed=seed)

SCENARIO_49 = Scenario(name='sc_49', yaw=4.900, roll=-0.150, pitch=0.040, n=33)

def frames_scenario_49(seed: int = 49) -> List[np.ndarray]:
    return run_scenario(SCENARIO_49, seed=seed)

SCENARIO_50 = Scenario(name='sc_50', yaw=5.000, roll=-0.100, pitch=-0.040, n=34)

def frames_scenario_50(seed: int = 50) -> List[np.ndarray]:
    return run_scenario(SCENARIO_50, seed=seed)

SCENARIO_51 = Scenario(name='sc_51', yaw=5.100, roll=-0.050, pitch=-0.020, n=35)

def frames_scenario_51(seed: int = 51) -> List[np.ndarray]:
    return run_scenario(SCENARIO_51, seed=seed)

SCENARIO_52 = Scenario(name='sc_52', yaw=5.200, roll=0.000, pitch=0.000, n=36)

def frames_scenario_52(seed: int = 52) -> List[np.ndarray]:
    return run_scenario(SCENARIO_52, seed=seed)

SCENARIO_53 = Scenario(name='sc_53', yaw=5.300, roll=0.050, pitch=0.020, n=37)

def frames_scenario_53(seed: int = 53) -> List[np.ndarray]:
    return run_scenario(SCENARIO_53, seed=seed)

SCENARIO_54 = Scenario(name='sc_54', yaw=5.400, roll=0.100, pitch=0.040, n=38)

def frames_scenario_54(seed: int = 54) -> List[np.ndarray]:
    return run_scenario(SCENARIO_54, seed=seed)

SCENARIO_55 = Scenario(name='sc_55', yaw=5.500, roll=0.150, pitch=-0.040, n=39)

def frames_scenario_55(seed: int = 55) -> List[np.ndarray]:
    return run_scenario(SCENARIO_55, seed=seed)

SCENARIO_56 = Scenario(name='sc_56', yaw=5.600, roll=-0.150, pitch=-0.020, n=40)

def frames_scenario_56(seed: int = 56) -> List[np.ndarray]:
    return run_scenario(SCENARIO_56, seed=seed)

SCENARIO_57 = Scenario(name='sc_57', yaw=5.700, roll=-0.100, pitch=0.000, n=41)

def frames_scenario_57(seed: int = 57) -> List[np.ndarray]:
    return run_scenario(SCENARIO_57, seed=seed)

SCENARIO_58 = Scenario(name='sc_58', yaw=5.800, roll=-0.050, pitch=0.020, n=42)

def frames_scenario_58(seed: int = 58) -> List[np.ndarray]:
    return run_scenario(SCENARIO_58, seed=seed)

SCENARIO_59 = Scenario(name='sc_59', yaw=5.900, roll=0.000, pitch=0.040, n=43)

def frames_scenario_59(seed: int = 59) -> List[np.ndarray]:
    return run_scenario(SCENARIO_59, seed=seed)

SCENARIO_60 = Scenario(name='sc_60', yaw=6.000, roll=0.050, pitch=-0.040, n=24)

def frames_scenario_60(seed: int = 60) -> List[np.ndarray]:
    return run_scenario(SCENARIO_60, seed=seed)

SCENARIO_61 = Scenario(name='sc_61', yaw=6.100, roll=0.100, pitch=-0.020, n=25)

def frames_scenario_61(seed: int = 61) -> List[np.ndarray]:
    return run_scenario(SCENARIO_61, seed=seed)

SCENARIO_62 = Scenario(name='sc_62', yaw=6.200, roll=0.150, pitch=0.000, n=26)

def frames_scenario_62(seed: int = 62) -> List[np.ndarray]:
    return run_scenario(SCENARIO_62, seed=seed)

SCENARIO_63 = Scenario(name='sc_63', yaw=6.300, roll=-0.150, pitch=0.020, n=27)

def frames_scenario_63(seed: int = 63) -> List[np.ndarray]:
    return run_scenario(SCENARIO_63, seed=seed)

SCENARIO_64 = Scenario(name='sc_64', yaw=6.400, roll=-0.100, pitch=0.040, n=28)

def frames_scenario_64(seed: int = 64) -> List[np.ndarray]:
    return run_scenario(SCENARIO_64, seed=seed)

SCENARIO_65 = Scenario(name='sc_65', yaw=6.500, roll=-0.050, pitch=-0.040, n=29)

def frames_scenario_65(seed: int = 65) -> List[np.ndarray]:
    return run_scenario(SCENARIO_65, seed=seed)

SCENARIO_66 = Scenario(name='sc_66', yaw=6.600, roll=0.000, pitch=-0.020, n=30)

def frames_scenario_66(seed: int = 66) -> List[np.ndarray]:
    return run_scenario(SCENARIO_66, seed=seed)

SCENARIO_67 = Scenario(name='sc_67', yaw=6.700, roll=0.050, pitch=0.000, n=31)

def frames_scenario_67(seed: int = 67) -> List[np.ndarray]:
    return run_scenario(SCENARIO_67, seed=seed)

SCENARIO_68 = Scenario(name='sc_68', yaw=6.800, roll=0.100, pitch=0.020, n=32)

def frames_scenario_68(seed: int = 68) -> List[np.ndarray]:
    return run_scenario(SCENARIO_68, seed=seed)

SCENARIO_69 = Scenario(name='sc_69', yaw=6.900, roll=0.150, pitch=0.040, n=33)

def frames_scenario_69(seed: int = 69) -> List[np.ndarray]:
    return run_scenario(SCENARIO_69, seed=seed)

SCENARIO_70 = Scenario(name='sc_70', yaw=7.000, roll=-0.150, pitch=-0.040, n=34)

def frames_scenario_70(seed: int = 70) -> List[np.ndarray]:
    return run_scenario(SCENARIO_70, seed=seed)

SCENARIO_71 = Scenario(name='sc_71', yaw=7.100, roll=-0.100, pitch=-0.020, n=35)

def frames_scenario_71(seed: int = 71) -> List[np.ndarray]:
    return run_scenario(SCENARIO_71, seed=seed)

SCENARIO_72 = Scenario(name='sc_72', yaw=7.200, roll=-0.050, pitch=0.000, n=36)

def frames_scenario_72(seed: int = 72) -> List[np.ndarray]:
    return run_scenario(SCENARIO_72, seed=seed)

SCENARIO_73 = Scenario(name='sc_73', yaw=7.300, roll=0.000, pitch=0.020, n=37)

def frames_scenario_73(seed: int = 73) -> List[np.ndarray]:
    return run_scenario(SCENARIO_73, seed=seed)

SCENARIO_74 = Scenario(name='sc_74', yaw=7.400, roll=0.050, pitch=0.040, n=38)

def frames_scenario_74(seed: int = 74) -> List[np.ndarray]:
    return run_scenario(SCENARIO_74, seed=seed)

SCENARIO_75 = Scenario(name='sc_75', yaw=7.500, roll=0.100, pitch=-0.040, n=39)

def frames_scenario_75(seed: int = 75) -> List[np.ndarray]:
    return run_scenario(SCENARIO_75, seed=seed)

SCENARIO_76 = Scenario(name='sc_76', yaw=7.600, roll=0.150, pitch=-0.020, n=40)

def frames_scenario_76(seed: int = 76) -> List[np.ndarray]:
    return run_scenario(SCENARIO_76, seed=seed)

SCENARIO_77 = Scenario(name='sc_77', yaw=7.700, roll=-0.150, pitch=0.000, n=41)

def frames_scenario_77(seed: int = 77) -> List[np.ndarray]:
    return run_scenario(SCENARIO_77, seed=seed)

SCENARIO_78 = Scenario(name='sc_78', yaw=7.800, roll=-0.100, pitch=0.020, n=42)

def frames_scenario_78(seed: int = 78) -> List[np.ndarray]:
    return run_scenario(SCENARIO_78, seed=seed)

SCENARIO_79 = Scenario(name='sc_79', yaw=7.900, roll=-0.050, pitch=0.040, n=43)

def frames_scenario_79(seed: int = 79) -> List[np.ndarray]:
    return run_scenario(SCENARIO_79, seed=seed)

SCENARIO_80 = Scenario(name='sc_80', yaw=8.000, roll=0.000, pitch=-0.040, n=24)

def frames_scenario_80(seed: int = 80) -> List[np.ndarray]:
    return run_scenario(SCENARIO_80, seed=seed)

SCENARIO_81 = Scenario(name='sc_81', yaw=8.100, roll=0.050, pitch=-0.020, n=25)

def frames_scenario_81(seed: int = 81) -> List[np.ndarray]:
    return run_scenario(SCENARIO_81, seed=seed)

SCENARIO_82 = Scenario(name='sc_82', yaw=8.200, roll=0.100, pitch=0.000, n=26)

def frames_scenario_82(seed: int = 82) -> List[np.ndarray]:
    return run_scenario(SCENARIO_82, seed=seed)

SCENARIO_83 = Scenario(name='sc_83', yaw=8.300, roll=0.150, pitch=0.020, n=27)

def frames_scenario_83(seed: int = 83) -> List[np.ndarray]:
    return run_scenario(SCENARIO_83, seed=seed)

SCENARIO_84 = Scenario(name='sc_84', yaw=8.400, roll=-0.150, pitch=0.040, n=28)

def frames_scenario_84(seed: int = 84) -> List[np.ndarray]:
    return run_scenario(SCENARIO_84, seed=seed)

SCENARIO_85 = Scenario(name='sc_85', yaw=8.500, roll=-0.100, pitch=-0.040, n=29)

def frames_scenario_85(seed: int = 85) -> List[np.ndarray]:
    return run_scenario(SCENARIO_85, seed=seed)

SCENARIO_86 = Scenario(name='sc_86', yaw=8.600, roll=-0.050, pitch=-0.020, n=30)

def frames_scenario_86(seed: int = 86) -> List[np.ndarray]:
    return run_scenario(SCENARIO_86, seed=seed)

SCENARIO_87 = Scenario(name='sc_87', yaw=8.700, roll=0.000, pitch=0.000, n=31)

def frames_scenario_87(seed: int = 87) -> List[np.ndarray]:
    return run_scenario(SCENARIO_87, seed=seed)

SCENARIO_88 = Scenario(name='sc_88', yaw=8.800, roll=0.050, pitch=0.020, n=32)

def frames_scenario_88(seed: int = 88) -> List[np.ndarray]:
    return run_scenario(SCENARIO_88, seed=seed)

SCENARIO_89 = Scenario(name='sc_89', yaw=8.900, roll=0.100, pitch=0.040, n=33)

def frames_scenario_89(seed: int = 89) -> List[np.ndarray]:
    return run_scenario(SCENARIO_89, seed=seed)

SCENARIO_90 = Scenario(name='sc_90', yaw=9.000, roll=0.150, pitch=-0.040, n=34)

def frames_scenario_90(seed: int = 90) -> List[np.ndarray]:
    return run_scenario(SCENARIO_90, seed=seed)

SCENARIO_91 = Scenario(name='sc_91', yaw=9.100, roll=-0.150, pitch=-0.020, n=35)

def frames_scenario_91(seed: int = 91) -> List[np.ndarray]:
    return run_scenario(SCENARIO_91, seed=seed)

SCENARIO_92 = Scenario(name='sc_92', yaw=9.200, roll=-0.100, pitch=0.000, n=36)

def frames_scenario_92(seed: int = 92) -> List[np.ndarray]:
    return run_scenario(SCENARIO_92, seed=seed)

SCENARIO_93 = Scenario(name='sc_93', yaw=9.300, roll=-0.050, pitch=0.020, n=37)

def frames_scenario_93(seed: int = 93) -> List[np.ndarray]:
    return run_scenario(SCENARIO_93, seed=seed)

SCENARIO_94 = Scenario(name='sc_94', yaw=9.400, roll=0.000, pitch=0.040, n=38)

def frames_scenario_94(seed: int = 94) -> List[np.ndarray]:
    return run_scenario(SCENARIO_94, seed=seed)

SCENARIO_95 = Scenario(name='sc_95', yaw=9.500, roll=0.050, pitch=-0.040, n=39)

def frames_scenario_95(seed: int = 95) -> List[np.ndarray]:
    return run_scenario(SCENARIO_95, seed=seed)

SCENARIO_96 = Scenario(name='sc_96', yaw=9.600, roll=0.100, pitch=-0.020, n=40)

def frames_scenario_96(seed: int = 96) -> List[np.ndarray]:
    return run_scenario(SCENARIO_96, seed=seed)

SCENARIO_97 = Scenario(name='sc_97', yaw=9.700, roll=0.150, pitch=0.000, n=41)

def frames_scenario_97(seed: int = 97) -> List[np.ndarray]:
    return run_scenario(SCENARIO_97, seed=seed)

SCENARIO_98 = Scenario(name='sc_98', yaw=9.800, roll=-0.150, pitch=0.020, n=42)

def frames_scenario_98(seed: int = 98) -> List[np.ndarray]:
    return run_scenario(SCENARIO_98, seed=seed)

SCENARIO_99 = Scenario(name='sc_99', yaw=9.900, roll=-0.100, pitch=0.040, n=43)

def frames_scenario_99(seed: int = 99) -> List[np.ndarray]:
    return run_scenario(SCENARIO_99, seed=seed)
