from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Optional, Tuple
import numpy as np
from nadir_core.dashcam.geometry.lie_so3 import hat, so3_exp, so3_log, rpy_to_rot, rot_to_rpy

@dataclass
class MountState:
    roll: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0
    roll_rate: float = 0.0
    pitch_rate: float = 0.0
    yaw_rate: float = 0.0

    def as_vector(self) -> np.ndarray:
        return np.array([self.roll, self.pitch, self.yaw, self.roll_rate, self.pitch_rate, self.yaw_rate], dtype=np.float64)

    @classmethod
    def from_vector(cls, x: np.ndarray) -> 'MountState':
        x = np.asarray(x, dtype=np.float64).ravel()
        return cls(*[float(v) for v in x[:6]])


@dataclass
class MountEKF:
    x: np.ndarray = field(default_factory=lambda: np.zeros(6))
    P: np.ndarray = field(default_factory=lambda: np.eye(6) * 0.25)
    q_angle: float = 1e-4
    q_rate: float = 5e-3
    r_meas: float = 4e-2

    def predict(self, dt: float) -> None:
        dt = float(max(dt, 1e-4))
        F = np.eye(6)
        F[0, 3] = dt
        F[1, 4] = dt
        F[2, 5] = dt
        self.x = F @ self.x
        Q = np.diag([self.q_angle]*3 + [self.q_rate]*3)
        self.P = F @ self.P @ F.T + Q * dt

    def update_rpy(self, roll: float, pitch: float, yaw: float, Rdiag: Optional[np.ndarray] = None) -> MountState:
        z = np.array([roll, pitch, yaw], dtype=np.float64)
        H = np.zeros((3, 6))
        H[0, 0] = H[1, 1] = H[2, 2] = 1.0
        R = np.eye(3) * self.r_meas if Rdiag is None else np.diag(np.asarray(Rdiag, dtype=np.float64))
        y = z - H @ self.x
        S = H @ self.P @ H.T + R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        I = np.eye(6)
        self.P = (I - K @ H) @ self.P
        return MountState.from_vector(self.x)

    def innovation_mahal(self, roll: float, pitch: float, yaw: float) -> float:
        z = np.array([roll, pitch, yaw], dtype=np.float64)
        H = np.zeros((3, 6)); H[0,0]=H[1,1]=H[2,2]=1.0
        y = z - H @ self.x
        S = H @ self.P @ H.T + np.eye(3) * self.r_meas
        return float(y.T @ np.linalg.solve(S, y))

def process_noise_schedule_0(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00001000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_0(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.02000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_1(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00002000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_1(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.03000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_2(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00003000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_2(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.04000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_3(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00004000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_3(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.05000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_4(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00005000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_4(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.06000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_5(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00006000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_5(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.07000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_6(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00007000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_6(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.08000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_7(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00008000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_7(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.09000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_8(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00009000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_8(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.10000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_9(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00010000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_9(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.11000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_10(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00011000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_10(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.12000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_11(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00012000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_11(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.13000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_12(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00013000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_12(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.14000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_13(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00014000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_13(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.15000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_14(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00015000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_14(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.16000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_15(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00016000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_15(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.17000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_16(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00017000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_16(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.18000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_17(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00018000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_17(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.19000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_18(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00019000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_18(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.20000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_19(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00020000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_19(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.21000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_20(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00021000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_20(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.22000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_21(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00022000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_21(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.23000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_22(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00023000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_22(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.24000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_23(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00024000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_23(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.25000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_24(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00025000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_24(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.26000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_25(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00026000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_25(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.27000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_26(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00027000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_26(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.28000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_27(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00028000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_27(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.29000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_28(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00029000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_28(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.30000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_29(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00030000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_29(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.31000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_30(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00031000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_30(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.32000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_31(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00032000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_31(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.33000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_32(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00033000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_32(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.34000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_33(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00034000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_33(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.35000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_34(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00035000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_34(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.36000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_35(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00036000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_35(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.37000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_36(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00037000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_36(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.38000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_37(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00038000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_37(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.39000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_38(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00039000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_38(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.40000 / c
    return np.diag([s, s*1.1, s*1.2])

def process_noise_schedule_39(speed_mps: float, vibration: float) -> np.ndarray:
    s = max(0.0, float(speed_mps))
    v = max(0.0, float(vibration))
    base = 0.00040000
    q = np.array([base*(1+0.01*s), base*(1+0.015*s), base*(1+0.02*s),
                 base*10*(1+v), base*12*(1+v), base*14*(1+v)], dtype=np.float64)
    return np.diag(q)

def measurement_noise_from_conf_39(conf: float) -> np.ndarray:
    c = float(np.clip(conf, 0.05, 1.0))
    s = 0.41000 / c
    return np.diag([s, s*1.1, s*1.2])
