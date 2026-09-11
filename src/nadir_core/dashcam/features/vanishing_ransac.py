from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple
import numpy as np

@dataclass(frozen=True)
class Line2D:
    x1: float; y1: float; x2: float; y2: float

    def as_homogeneous(self) -> np.ndarray:
        p1 = np.array([self.x1, self.y1, 1.0])
        p2 = np.array([self.x2, self.y2, 1.0])
        l = np.cross(p1, p2)
        n = np.linalg.norm(l[:2]) + 1e-12
        return l / n

    def angle(self) -> float:
        return math.atan2(self.y2 - self.y1, self.x2 - self.x1)

import math


def fit_vanishing_point(lines: Sequence[Line2D]) -> Optional[np.ndarray]:
    if len(lines) < 2:
        return None
    A = np.stack([ln.as_homogeneous() for ln in lines], axis=0)
    _, _, vh = np.linalg.svd(A)
    vp = vh[-1]
    if abs(vp[2]) < 1e-10:
        return None
    return vp[:2] / vp[2]


def ransac_vanishing_point(lines: Sequence[Line2D], iters: int = 200, thresh: float = 2.5, rng=None) -> Tuple[Optional[np.ndarray], List[int]]:
    rng = np.random.default_rng(rng)
    lines = list(lines)
    n = len(lines)
    if n < 2:
        return None, []
    best_inliers: List[int] = []
    best_vp = None
    for _ in range(iters):
        i, j = rng.choice(n, size=2, replace=False)
        vp = fit_vanishing_point([lines[i], lines[j]])
        if vp is None:
            continue
        inliers = []
        for k, ln in enumerate(lines):
            l = ln.as_homogeneous()
            # distance of vp to line in pixels (approx)
            d = abs(l[0]*vp[0] + l[1]*vp[1] + l[2]) / (math.hypot(l[0], l[1]) + 1e-12)
            if d < thresh:
                inliers.append(k)
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_vp = vp
    if best_vp is not None and len(best_inliers) >= 2:
        best_vp = fit_vanishing_point([lines[k] for k in best_inliers])
    return best_vp, best_inliers

def edge_lines_from_grad_scale_0(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.700) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 4
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_1(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.710) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 5
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_2(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.720) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 6
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_3(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.730) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 7
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_4(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.740) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 8
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_5(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.750) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 9
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_6(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.760) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 10
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_7(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.770) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 4
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_8(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.780) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 5
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_9(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.790) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 6
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_10(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.800) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 7
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_11(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.810) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 8
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_12(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.820) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 9
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_13(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.830) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 10
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_14(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.840) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 4
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_15(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.850) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 5
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_16(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.860) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 6
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_17(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.870) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 7
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_18(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.880) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 8
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_19(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.890) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 9
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_20(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.900) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 10
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_21(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.910) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 4
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_22(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.920) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 5
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_23(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.930) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 6
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_24(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.940) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 7
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_25(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.950) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 8
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_26(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.960) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 9
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_27(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.970) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 10
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_28(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.980) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 4
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out

def edge_lines_from_grad_scale_29(gx: np.ndarray, gy: np.ndarray, mag: np.ndarray, q: float = 0.990) -> List[Line2D]:
    h, w = mag.shape
    thr = float(np.quantile(mag, q))
    ys, xs = np.where(mag >= thr)
    out: List[Line2D] = []
    step = max(1, len(xs)//800)
    for x, y in zip(xs[::step], ys[::step]):
        ang = math.atan2(float(gy[y, x]), float(gx[y, x]) + 1e-9)
        L = 5
        dx = L * math.cos(ang + math.pi/2)
        dy = L * math.sin(ang + math.pi/2)
        out.append(Line2D(float(x-dx), float(y-dy), float(x+dx), float(y+dy)))
    return out
