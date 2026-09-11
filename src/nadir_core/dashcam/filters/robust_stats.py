from __future__ import annotations\nimport math\nfrom typing import Callable, Optional, Sequence, Tuple\nimport numpy as np\n\n
def weight_huber(r: np.ndarray, c: float = 1.345) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    w = np.ones_like(a)\n    m = a > c\n    w[m] = c / (a[m] + 1e-12)\n    return w\n
def weight_tukey(r: np.ndarray, c: float = 4.685) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    w = np.zeros_like(a)\n    m = a <= c\n    u = a[m] / c\n    w[m] = (1.0 - u * u) ** 2\n    return w\n
def weight_cauchy(r: np.ndarray, c: float = 2.385) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    return 1.0 / (1.0 + (a / c) ** 2)\n
def weight_welsch(r: np.ndarray, c: float = 2.985) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    return np.exp(-(a / c) ** 2)\n
def weight_andrews(r: np.ndarray, c: float = 1.339) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    w = np.zeros_like(a)\n    m = a <= c * math.pi\n    w[m] = np.sin(a[m] / c) / (a[m] / c + 1e-12)\n    return w\n
def weight_fair(r: np.ndarray, c: float = 1.4) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    return 1.0 / (1.0 + a / c)\n
def weight_talwar(r: np.ndarray, c: float = 2.795) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    return (a <= c).astype(np.float64)\n
def weight_ramanujan(r: np.ndarray, c: float = 1.0) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.abs(r)
    return 1.0 / (1.0 + a)\n
def mad_scale(r: np.ndarray) -> float:
    r = np.asarray(r, dtype=np.float64)
    med = np.median(r)
    return float(1.4826 * np.median(np.abs(r - med)) + 1e-12)


def irls_location(x: np.ndarray, weight_fn: Callable[[np.ndarray], np.ndarray], iters: int = 30) -> float:
    x = np.asarray(x, dtype=np.float64).ravel()
    mu = float(np.median(x))
    for _ in range(iters):
        r = (x - mu) / mad_scale(x - mu)
        w = weight_fn(r)
        mu = float(np.sum(w * x) / (np.sum(w) + 1e-12))
    return mu


def irls_regression(A: np.ndarray, b: np.ndarray, weight_fn: Callable[[np.ndarray], np.ndarray], iters: int = 25) -> np.ndarray:
    A = np.asarray(A, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64).ravel()
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    for _ in range(iters):
        r = A @ x - b
        w = weight_fn(r / mad_scale(r))
        W = np.diag(w)
        x, *_ = np.linalg.lstsq(W @ A, W @ b, rcond=None)
    return x

def gaussian_kde_bw_0(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 0.05
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_1(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 0.1
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_2(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 0.2
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_3(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 0.35
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_4(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 0.5
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_5(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 0.75
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_6(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 1.0
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_7(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 1.5
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_8(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 2.0
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def gaussian_kde_bw_9(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    grid = np.asarray(grid, dtype=np.float64).ravel()
    bw = 3.0
    if x.size == 0:
        return np.zeros_like(grid)
    z = (grid[:, None] - x[None, :]) / bw
    return np.exp(-0.5 * z * z).mean(axis=1) / (bw * math.sqrt(2.0 * math.pi))

def polynomial_basis_1(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(1+1)]).T

def polynomial_basis_2(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(2+1)]).T

def polynomial_basis_3(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(3+1)]).T

def polynomial_basis_4(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(4+1)]).T

def polynomial_basis_5(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(5+1)]).T

def polynomial_basis_6(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(6+1)]).T

def polynomial_basis_7(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(7+1)]).T

def polynomial_basis_8(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(8+1)]).T

def polynomial_basis_9(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(9+1)]).T

def polynomial_basis_10(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(10+1)]).T

def polynomial_basis_11(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(11+1)]).T

def polynomial_basis_12(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(12+1)]).T

def polynomial_basis_13(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(13+1)]).T

def polynomial_basis_14(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(14+1)]).T

def polynomial_basis_15(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(15+1)]).T

def polynomial_basis_16(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(16+1)]).T

def polynomial_basis_17(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(17+1)]).T

def polynomial_basis_18(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(18+1)]).T

def polynomial_basis_19(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(19+1)]).T

def polynomial_basis_20(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64).ravel()
    return np.vstack([x ** k for k in range(20+1)]).T
