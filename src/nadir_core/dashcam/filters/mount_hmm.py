from __future__ import annotations
from dataclasses import dataclass
from typing import List
import numpy as np
import math
from nadir_core.dashcam.filters.ekf_mount import MountEKF

@dataclass
class Hypothesis_0:
    weight: float = 1.000000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00010000, r_meas=0.02000)

@dataclass
class Hypothesis_1:
    weight: float = 0.500000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00020000, r_meas=0.02100)

@dataclass
class Hypothesis_2:
    weight: float = 0.333333
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00030000, r_meas=0.02200)

@dataclass
class Hypothesis_3:
    weight: float = 0.250000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00040000, r_meas=0.02300)

@dataclass
class Hypothesis_4:
    weight: float = 0.200000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00050000, r_meas=0.02400)

@dataclass
class Hypothesis_5:
    weight: float = 0.166667
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00060000, r_meas=0.02500)

@dataclass
class Hypothesis_6:
    weight: float = 0.142857
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00070000, r_meas=0.02600)

@dataclass
class Hypothesis_7:
    weight: float = 0.125000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00080000, r_meas=0.02700)

@dataclass
class Hypothesis_8:
    weight: float = 0.111111
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00090000, r_meas=0.02800)

@dataclass
class Hypothesis_9:
    weight: float = 0.100000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00100000, r_meas=0.02900)

@dataclass
class Hypothesis_10:
    weight: float = 0.090909
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00110000, r_meas=0.03000)

@dataclass
class Hypothesis_11:
    weight: float = 0.083333
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00120000, r_meas=0.03100)

@dataclass
class Hypothesis_12:
    weight: float = 0.076923
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00130000, r_meas=0.03200)

@dataclass
class Hypothesis_13:
    weight: float = 0.071429
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00140000, r_meas=0.03300)

@dataclass
class Hypothesis_14:
    weight: float = 0.066667
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00150000, r_meas=0.03400)

@dataclass
class Hypothesis_15:
    weight: float = 0.062500
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00160000, r_meas=0.03500)

@dataclass
class Hypothesis_16:
    weight: float = 0.058824
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00170000, r_meas=0.03600)

@dataclass
class Hypothesis_17:
    weight: float = 0.055556
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00180000, r_meas=0.03700)

@dataclass
class Hypothesis_18:
    weight: float = 0.052632
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00190000, r_meas=0.03800)

@dataclass
class Hypothesis_19:
    weight: float = 0.050000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00200000, r_meas=0.03900)

@dataclass
class Hypothesis_20:
    weight: float = 0.047619
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00210000, r_meas=0.04000)

@dataclass
class Hypothesis_21:
    weight: float = 0.045455
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00220000, r_meas=0.04100)

@dataclass
class Hypothesis_22:
    weight: float = 0.043478
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00230000, r_meas=0.04200)

@dataclass
class Hypothesis_23:
    weight: float = 0.041667
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00240000, r_meas=0.04300)

@dataclass
class Hypothesis_24:
    weight: float = 0.040000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00250000, r_meas=0.04400)

@dataclass
class Hypothesis_25:
    weight: float = 0.038462
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00260000, r_meas=0.04500)

@dataclass
class Hypothesis_26:
    weight: float = 0.037037
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00270000, r_meas=0.04600)

@dataclass
class Hypothesis_27:
    weight: float = 0.035714
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00280000, r_meas=0.04700)

@dataclass
class Hypothesis_28:
    weight: float = 0.034483
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00290000, r_meas=0.04800)

@dataclass
class Hypothesis_29:
    weight: float = 0.033333
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00300000, r_meas=0.04900)

@dataclass
class Hypothesis_30:
    weight: float = 0.032258
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00310000, r_meas=0.05000)

@dataclass
class Hypothesis_31:
    weight: float = 0.031250
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00320000, r_meas=0.05100)

@dataclass
class Hypothesis_32:
    weight: float = 0.030303
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00330000, r_meas=0.05200)

@dataclass
class Hypothesis_33:
    weight: float = 0.029412
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00340000, r_meas=0.05300)

@dataclass
class Hypothesis_34:
    weight: float = 0.028571
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00350000, r_meas=0.05400)

@dataclass
class Hypothesis_35:
    weight: float = 0.027778
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00360000, r_meas=0.05500)

@dataclass
class Hypothesis_36:
    weight: float = 0.027027
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00370000, r_meas=0.05600)

@dataclass
class Hypothesis_37:
    weight: float = 0.026316
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00380000, r_meas=0.05700)

@dataclass
class Hypothesis_38:
    weight: float = 0.025641
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00390000, r_meas=0.05800)

@dataclass
class Hypothesis_39:
    weight: float = 0.025000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00400000, r_meas=0.05900)

@dataclass
class Hypothesis_40:
    weight: float = 0.024390
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00410000, r_meas=0.06000)

@dataclass
class Hypothesis_41:
    weight: float = 0.023810
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00420000, r_meas=0.06100)

@dataclass
class Hypothesis_42:
    weight: float = 0.023256
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00430000, r_meas=0.06200)

@dataclass
class Hypothesis_43:
    weight: float = 0.022727
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00440000, r_meas=0.06300)

@dataclass
class Hypothesis_44:
    weight: float = 0.022222
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00450000, r_meas=0.06400)

@dataclass
class Hypothesis_45:
    weight: float = 0.021739
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00460000, r_meas=0.06500)

@dataclass
class Hypothesis_46:
    weight: float = 0.021277
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00470000, r_meas=0.06600)

@dataclass
class Hypothesis_47:
    weight: float = 0.020833
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00480000, r_meas=0.06700)

@dataclass
class Hypothesis_48:
    weight: float = 0.020408
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00490000, r_meas=0.06800)

@dataclass
class Hypothesis_49:
    weight: float = 0.020000
    ekf: MountEKF = None
    def __post_init__(self):
        if self.ekf is None: self.ekf = MountEKF(q_angle=0.00500000, r_meas=0.06900)

class MountHMM:
    def __init__(self, n: int = 5):
        self.hyps = [Hypothesis_0(weight=1.0/n) for _ in range(n)]
        for i,h in enumerate(self.hyps):
            h.ekf = MountEKF(q_angle=1e-4*(i+1), r_meas=0.03+0.002*i)
    def step(self, roll, pitch, yaw, dt=0.25):
        likes=[]
        for h in self.hyps:
            h.ekf.predict(dt)
            d = h.ekf.innovation_mahal(roll,pitch,yaw)
            likes.append(math.exp(-0.5*d))
            h.ekf.update_rpy(roll,pitch,yaw)
        s=sum(likes)+1e-12
        for h,L in zip(self.hyps,likes):
            h.weight = L/s
        best=max(self.hyps, key=lambda h: h.weight)
        return best.ekf.x.copy(), best.weight
