from __future__ import annotations
from typing import List, Optional, Tuple
import numpy as np
import math

def _reduce(img: np.ndarray) -> np.ndarray:
    img = img.astype(np.float64)
    # simple 2x box
    h, w = img.shape
    h2, w2 = h//2, w//2
    return 0.25 * (img[0:2*h2:2, 0:2*w2:2] + img[1:2*h2:2, 0:2*w2:2] + img[0:2*h2:2, 1:2*w2:2] + img[1:2*h2:2, 1:2*w2:2])

def build_pyramid(img: np.ndarray, levels: int = 4) -> List[np.ndarray]:
    pyr = [img.astype(np.float64)]
    for _ in range(1, levels):
        pyr.append(_reduce(pyr[-1]))
    return pyr

def lk_point(prev: np.ndarray, cur: np.ndarray, x: float, y: float, win: int = 5, iters: int = 8) -> Tuple[float, float, float]:
    h, w = prev.shape
    gx = np.zeros_like(prev); gy = np.zeros_like(prev)
    gx[:, 1:-1] = 0.5 * (prev[:, 2:] - prev[:, :-2])
    gy[1:-1, :] = 0.5 * (prev[2:, :] - prev[:-2, :])
    u = v = 0.0
    for _ in range(iters):
        xa, ya = x + u, y + v
        xs = np.arange(-win, win+1)
        ys = np.arange(-win, win+1)
        A11=A12=A22=b1=b2=0.0; n=0
        for dy in ys:
            for dx in xs:
                x0 = int(round(x + dx)); y0 = int(round(y + dy))
                x1 = int(round(xa + dx)); y1 = int(round(ya + dy))
                if not (1 <= x0 < w-1 and 1 <= y0 < h-1 and 1 <= x1 < w-1 and 1 <= y1 < h-1):
                    continue
                Ix = gx[y0, x0]; Iy = gy[y0, x0]
                It = cur[y1, x1] - prev[y0, x0]
                A11 += Ix*Ix; A12 += Ix*Iy; A22 += Iy*Iy
                b1 -= Ix*It; b2 -= Iy*It; n += 1
        det = A11*A22 - A12*A12
        if n < 6 or abs(det) < 1e-9:
            return u, v, 0.0
        du = (A22*b1 - A12*b2)/det
        dv = (-A12*b1 + A11*b2)/det
        u += du; v += dv
        if du*du + dv*dv < 1e-6:
            break
    conf = float(min(1.0, n / float((2*win+1)**2)))
    return u, v, conf

def pyramid_lk(prev: np.ndarray, cur: np.ndarray, pts: np.ndarray, levels: int = 3, win: int = 5) -> Tuple[np.ndarray, np.ndarray]:
    pyr0 = build_pyramid(prev, levels)
    pyr1 = build_pyramid(cur, levels)
    pts = np.asarray(pts, dtype=np.float64).reshape(-1, 2)
    flow = np.zeros_like(pts)
    conf = np.zeros(len(pts))
    scale = 2 ** (levels - 1)
    pts_l = pts / scale
    for lvl in range(levels-1, -1, -1):
        flow *= 2.0
        pts_l = pts / (2 ** lvl)
        for i, (x, y) in enumerate(pts_l):
            u, v, c = lk_point(pyr0[lvl], pyr1[lvl], x + flow[i,0], y + flow[i,1], win=win)
            # actually track residual from current guess
            u2, v2, c2 = lk_point(pyr0[lvl], pyr1[lvl], x, y, win=win)
            flow[i] = [u2, v2]
            conf[i] = c2
    return flow, conf

def grid_points_0(h: int, w: int, margin: float = 0.100, n: int = 6) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_0(flow: np.ndarray, conf: np.ndarray, foc_px: float = 600.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_1(h: int, w: int, margin: float = 0.110, n: int = 7) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_1(flow: np.ndarray, conf: np.ndarray, foc_px: float = 610.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_2(h: int, w: int, margin: float = 0.120, n: int = 8) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_2(flow: np.ndarray, conf: np.ndarray, foc_px: float = 620.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_3(h: int, w: int, margin: float = 0.130, n: int = 9) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_3(flow: np.ndarray, conf: np.ndarray, foc_px: float = 630.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_4(h: int, w: int, margin: float = 0.140, n: int = 10) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_4(flow: np.ndarray, conf: np.ndarray, foc_px: float = 640.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_5(h: int, w: int, margin: float = 0.150, n: int = 11) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_5(flow: np.ndarray, conf: np.ndarray, foc_px: float = 650.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_6(h: int, w: int, margin: float = 0.160, n: int = 12) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_6(flow: np.ndarray, conf: np.ndarray, foc_px: float = 660.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_7(h: int, w: int, margin: float = 0.170, n: int = 13) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_7(flow: np.ndarray, conf: np.ndarray, foc_px: float = 670.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_8(h: int, w: int, margin: float = 0.180, n: int = 6) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_8(flow: np.ndarray, conf: np.ndarray, foc_px: float = 680.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_9(h: int, w: int, margin: float = 0.190, n: int = 7) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_9(flow: np.ndarray, conf: np.ndarray, foc_px: float = 690.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_10(h: int, w: int, margin: float = 0.200, n: int = 8) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_10(flow: np.ndarray, conf: np.ndarray, foc_px: float = 700.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_11(h: int, w: int, margin: float = 0.210, n: int = 9) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_11(flow: np.ndarray, conf: np.ndarray, foc_px: float = 710.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_12(h: int, w: int, margin: float = 0.220, n: int = 10) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_12(flow: np.ndarray, conf: np.ndarray, foc_px: float = 720.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_13(h: int, w: int, margin: float = 0.230, n: int = 11) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_13(flow: np.ndarray, conf: np.ndarray, foc_px: float = 730.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_14(h: int, w: int, margin: float = 0.240, n: int = 12) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_14(flow: np.ndarray, conf: np.ndarray, foc_px: float = 740.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_15(h: int, w: int, margin: float = 0.250, n: int = 13) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_15(flow: np.ndarray, conf: np.ndarray, foc_px: float = 750.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_16(h: int, w: int, margin: float = 0.260, n: int = 6) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_16(flow: np.ndarray, conf: np.ndarray, foc_px: float = 760.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_17(h: int, w: int, margin: float = 0.270, n: int = 7) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_17(flow: np.ndarray, conf: np.ndarray, foc_px: float = 770.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_18(h: int, w: int, margin: float = 0.280, n: int = 8) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_18(flow: np.ndarray, conf: np.ndarray, foc_px: float = 780.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_19(h: int, w: int, margin: float = 0.290, n: int = 9) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_19(flow: np.ndarray, conf: np.ndarray, foc_px: float = 790.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_20(h: int, w: int, margin: float = 0.300, n: int = 10) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_20(flow: np.ndarray, conf: np.ndarray, foc_px: float = 800.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_21(h: int, w: int, margin: float = 0.310, n: int = 11) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_21(flow: np.ndarray, conf: np.ndarray, foc_px: float = 810.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_22(h: int, w: int, margin: float = 0.320, n: int = 12) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_22(flow: np.ndarray, conf: np.ndarray, foc_px: float = 820.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_23(h: int, w: int, margin: float = 0.330, n: int = 13) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_23(flow: np.ndarray, conf: np.ndarray, foc_px: float = 830.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))

def grid_points_24(h: int, w: int, margin: float = 0.340, n: int = 6) -> np.ndarray:
    ys = np.linspace(h*margin, h*(1-margin), n)
    xs = np.linspace(w*margin, w*(1-margin), n)
    xx, yy = np.meshgrid(xs, ys)
    return np.stack([xx.ravel(), yy.ravel()], axis=1)

def flow_yaw_proxy_24(flow: np.ndarray, conf: np.ndarray, foc_px: float = 840.0) -> float:
    m = conf > 0.2
    if not np.any(m):
        return 0.0
    dx = float(np.median(flow[m, 0]))
    return float(np.degrees(math.atan2(dx, foc_px)))
