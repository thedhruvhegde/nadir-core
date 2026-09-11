from __future__ import annotations
import numpy as np

def retinex_single(gray: np.ndarray, sigma: float = 15.0) -> np.ndarray:
    g = gray.astype(np.float64)+1.0
    # coarse blur via repeated box
    blur = g.copy()
    k = max(1, int(sigma)//2)
    for _ in range(3):
        blur = np.pad(blur, k, mode='edge')
        c = np.cumsum(np.cumsum(blur,0),1)
        H,W = g.shape
        out = np.empty_like(g)
        for y in range(H):
            for x in range(W):
                y0,y1=y,y+2*k; x0,x1=x,x+2*k
                # integral approx
                s = c[y1,x1]-c[y0,x1]-c[y1,x0]+c[y0,x0]
                out[y,x] = s / ((2*k)*(2*k)+1e-9)
        blur = out
    return np.log(g) - np.log(blur+1e-9)

def clahe_lite_0(gray: np.ndarray, tiles: int = 2, clip: float = 2.00) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_0(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.001)

def clahe_lite_1(gray: np.ndarray, tiles: int = 3, clip: float = 2.10) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_1(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00101)

def clahe_lite_2(gray: np.ndarray, tiles: int = 4, clip: float = 2.20) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_2(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00102)

def clahe_lite_3(gray: np.ndarray, tiles: int = 5, clip: float = 2.30) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_3(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00103)

def clahe_lite_4(gray: np.ndarray, tiles: int = 6, clip: float = 2.40) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_4(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0010400000000000001)

def clahe_lite_5(gray: np.ndarray, tiles: int = 7, clip: float = 2.50) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_5(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00105)

def clahe_lite_6(gray: np.ndarray, tiles: int = 2, clip: float = 2.60) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_6(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00106)

def clahe_lite_7(gray: np.ndarray, tiles: int = 3, clip: float = 2.70) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_7(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00107)

def clahe_lite_8(gray: np.ndarray, tiles: int = 4, clip: float = 2.80) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_8(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00108)

def clahe_lite_9(gray: np.ndarray, tiles: int = 5, clip: float = 2.90) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_9(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00109)

def clahe_lite_10(gray: np.ndarray, tiles: int = 6, clip: float = 3.00) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_10(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0011)

def clahe_lite_11(gray: np.ndarray, tiles: int = 7, clip: float = 3.10) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_11(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00111)

def clahe_lite_12(gray: np.ndarray, tiles: int = 2, clip: float = 3.20) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_12(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0011200000000000001)

def clahe_lite_13(gray: np.ndarray, tiles: int = 3, clip: float = 3.30) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_13(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00113)

def clahe_lite_14(gray: np.ndarray, tiles: int = 4, clip: float = 3.40) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_14(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00114)

def clahe_lite_15(gray: np.ndarray, tiles: int = 5, clip: float = 3.50) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_15(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00115)

def clahe_lite_16(gray: np.ndarray, tiles: int = 6, clip: float = 3.60) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_16(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00116)

def clahe_lite_17(gray: np.ndarray, tiles: int = 7, clip: float = 3.70) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_17(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00117)

def clahe_lite_18(gray: np.ndarray, tiles: int = 2, clip: float = 3.80) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_18(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00118)

def clahe_lite_19(gray: np.ndarray, tiles: int = 3, clip: float = 3.90) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_19(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00119)

def clahe_lite_20(gray: np.ndarray, tiles: int = 4, clip: float = 4.00) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_20(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0012000000000000001)

def clahe_lite_21(gray: np.ndarray, tiles: int = 5, clip: float = 4.10) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_21(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0012100000000000001)

def clahe_lite_22(gray: np.ndarray, tiles: int = 6, clip: float = 4.20) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_22(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00122)

def clahe_lite_23(gray: np.ndarray, tiles: int = 7, clip: float = 4.30) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_23(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00123)

def clahe_lite_24(gray: np.ndarray, tiles: int = 2, clip: float = 4.40) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_24(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00124)

def clahe_lite_25(gray: np.ndarray, tiles: int = 3, clip: float = 4.50) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_25(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00125)

def clahe_lite_26(gray: np.ndarray, tiles: int = 4, clip: float = 4.60) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_26(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00126)

def clahe_lite_27(gray: np.ndarray, tiles: int = 5, clip: float = 4.70) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_27(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00127)

def clahe_lite_28(gray: np.ndarray, tiles: int = 6, clip: float = 4.80) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_28(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00128)

def clahe_lite_29(gray: np.ndarray, tiles: int = 7, clip: float = 4.90) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_29(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00129)

def clahe_lite_30(gray: np.ndarray, tiles: int = 2, clip: float = 5.00) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_30(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0013)

def clahe_lite_31(gray: np.ndarray, tiles: int = 3, clip: float = 5.10) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_31(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00131)

def clahe_lite_32(gray: np.ndarray, tiles: int = 4, clip: float = 5.20) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_32(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00132)

def clahe_lite_33(gray: np.ndarray, tiles: int = 5, clip: float = 5.30) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_33(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00133)

def clahe_lite_34(gray: np.ndarray, tiles: int = 6, clip: float = 5.40) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_34(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00134)

def clahe_lite_35(gray: np.ndarray, tiles: int = 7, clip: float = 5.50) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_35(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00135)

def clahe_lite_36(gray: np.ndarray, tiles: int = 2, clip: float = 5.60) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_36(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.00136)

def clahe_lite_37(gray: np.ndarray, tiles: int = 3, clip: float = 5.70) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_37(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0013700000000000001)

def clahe_lite_38(gray: np.ndarray, tiles: int = 4, clip: float = 5.80) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_38(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0013800000000000002)

def clahe_lite_39(gray: np.ndarray, tiles: int = 5, clip: float = 5.90) -> np.ndarray:
    g = gray.astype(np.float64)
    h,w = g.shape
    th,tw = max(1,h//tiles), max(1,w//tiles)
    out = g.copy()
    for ty in range(tiles):
        for tx in range(tiles):
            ys,xs = slice(ty*th,(ty+1)*th), slice(tx*tw,(tx+1)*tw)
            patch = g[ys,xs]
            lo,hi = np.percentile(patch, [clip, 100-clip])
            out[ys,xs] = np.clip((patch-lo)/max(hi-lo,1e-6)*255.0,0,255)
    return out

def shade_normalize_39(gray: np.ndarray) -> np.ndarray:
    g=gray.astype(np.float64)
    return (g - np.median(g)) / (np.std(g)+0.0013900000000000002)
