from __future__ import annotations
import numpy as np
import math

def whiten_residuals_0(X: np.ndarray, eps: float = 1.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_0(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_1(X: np.ndarray, eps: float = 2.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_1(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_2(X: np.ndarray, eps: float = 3.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_2(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_3(X: np.ndarray, eps: float = 4.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_3(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_4(X: np.ndarray, eps: float = 5.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_4(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_5(X: np.ndarray, eps: float = 6.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_5(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_6(X: np.ndarray, eps: float = 7.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_6(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_7(X: np.ndarray, eps: float = 8.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_7(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_8(X: np.ndarray, eps: float = 9.00e-06) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_8(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_9(X: np.ndarray, eps: float = 1.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_9(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_10(X: np.ndarray, eps: float = 1.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_10(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_11(X: np.ndarray, eps: float = 1.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_11(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_12(X: np.ndarray, eps: float = 1.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_12(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_13(X: np.ndarray, eps: float = 1.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_13(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_14(X: np.ndarray, eps: float = 1.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_14(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_15(X: np.ndarray, eps: float = 1.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_15(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_16(X: np.ndarray, eps: float = 1.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_16(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_17(X: np.ndarray, eps: float = 1.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_17(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_18(X: np.ndarray, eps: float = 1.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_18(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_19(X: np.ndarray, eps: float = 2.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_19(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_20(X: np.ndarray, eps: float = 2.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_20(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_21(X: np.ndarray, eps: float = 2.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_21(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_22(X: np.ndarray, eps: float = 2.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_22(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_23(X: np.ndarray, eps: float = 2.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_23(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_24(X: np.ndarray, eps: float = 2.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_24(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_25(X: np.ndarray, eps: float = 2.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_25(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_26(X: np.ndarray, eps: float = 2.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_26(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_27(X: np.ndarray, eps: float = 2.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_27(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_28(X: np.ndarray, eps: float = 2.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_28(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_29(X: np.ndarray, eps: float = 3.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_29(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_30(X: np.ndarray, eps: float = 3.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_30(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_31(X: np.ndarray, eps: float = 3.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_31(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_32(X: np.ndarray, eps: float = 3.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_32(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_33(X: np.ndarray, eps: float = 3.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_33(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_34(X: np.ndarray, eps: float = 3.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_34(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_35(X: np.ndarray, eps: float = 3.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_35(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_36(X: np.ndarray, eps: float = 3.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_36(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_37(X: np.ndarray, eps: float = 3.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_37(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_38(X: np.ndarray, eps: float = 3.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_38(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_39(X: np.ndarray, eps: float = 4.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_39(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_40(X: np.ndarray, eps: float = 4.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_40(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_41(X: np.ndarray, eps: float = 4.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_41(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_42(X: np.ndarray, eps: float = 4.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_42(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_43(X: np.ndarray, eps: float = 4.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_43(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_44(X: np.ndarray, eps: float = 4.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_44(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_45(X: np.ndarray, eps: float = 4.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_45(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_46(X: np.ndarray, eps: float = 4.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_46(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_47(X: np.ndarray, eps: float = 4.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_47(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_48(X: np.ndarray, eps: float = 4.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_48(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_49(X: np.ndarray, eps: float = 5.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_49(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_50(X: np.ndarray, eps: float = 5.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_50(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_51(X: np.ndarray, eps: float = 5.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_51(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_52(X: np.ndarray, eps: float = 5.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_52(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_53(X: np.ndarray, eps: float = 5.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_53(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_54(X: np.ndarray, eps: float = 5.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_54(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_55(X: np.ndarray, eps: float = 5.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_55(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_56(X: np.ndarray, eps: float = 5.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_56(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_57(X: np.ndarray, eps: float = 5.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_57(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_58(X: np.ndarray, eps: float = 5.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_58(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_59(X: np.ndarray, eps: float = 6.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_59(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_60(X: np.ndarray, eps: float = 6.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_60(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_61(X: np.ndarray, eps: float = 6.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_61(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_62(X: np.ndarray, eps: float = 6.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_62(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_63(X: np.ndarray, eps: float = 6.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_63(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_64(X: np.ndarray, eps: float = 6.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_64(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_65(X: np.ndarray, eps: float = 6.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_65(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_66(X: np.ndarray, eps: float = 6.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_66(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_67(X: np.ndarray, eps: float = 6.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_67(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_68(X: np.ndarray, eps: float = 6.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_68(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_69(X: np.ndarray, eps: float = 7.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_69(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_70(X: np.ndarray, eps: float = 7.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_70(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_71(X: np.ndarray, eps: float = 7.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_71(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_72(X: np.ndarray, eps: float = 7.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_72(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_73(X: np.ndarray, eps: float = 7.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_73(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_74(X: np.ndarray, eps: float = 7.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_74(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_75(X: np.ndarray, eps: float = 7.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_75(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_76(X: np.ndarray, eps: float = 7.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_76(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_77(X: np.ndarray, eps: float = 7.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_77(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_78(X: np.ndarray, eps: float = 7.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_78(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_79(X: np.ndarray, eps: float = 8.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_79(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_80(X: np.ndarray, eps: float = 8.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_80(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_81(X: np.ndarray, eps: float = 8.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_81(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_82(X: np.ndarray, eps: float = 8.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_82(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_83(X: np.ndarray, eps: float = 8.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_83(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_84(X: np.ndarray, eps: float = 8.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_84(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_85(X: np.ndarray, eps: float = 8.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_85(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_86(X: np.ndarray, eps: float = 8.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_86(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_87(X: np.ndarray, eps: float = 8.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_87(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_88(X: np.ndarray, eps: float = 8.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_88(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_89(X: np.ndarray, eps: float = 9.00e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_89(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_90(X: np.ndarray, eps: float = 9.10e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_90(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_91(X: np.ndarray, eps: float = 9.20e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_91(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_92(X: np.ndarray, eps: float = 9.30e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_92(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_93(X: np.ndarray, eps: float = 9.40e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_93(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_94(X: np.ndarray, eps: float = 9.50e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_94(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_95(X: np.ndarray, eps: float = 9.60e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_95(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_96(X: np.ndarray, eps: float = 9.70e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_96(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_97(X: np.ndarray, eps: float = 9.80e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_97(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_98(X: np.ndarray, eps: float = 9.90e-05) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_98(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_99(X: np.ndarray, eps: float = 1.00e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_99(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_100(X: np.ndarray, eps: float = 1.01e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_100(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_101(X: np.ndarray, eps: float = 1.02e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_101(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_102(X: np.ndarray, eps: float = 1.03e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_102(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_103(X: np.ndarray, eps: float = 1.04e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_103(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_104(X: np.ndarray, eps: float = 1.05e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_104(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_105(X: np.ndarray, eps: float = 1.06e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_105(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_106(X: np.ndarray, eps: float = 1.07e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_106(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_107(X: np.ndarray, eps: float = 1.08e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_107(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_108(X: np.ndarray, eps: float = 1.09e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_108(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_109(X: np.ndarray, eps: float = 1.10e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_109(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_110(X: np.ndarray, eps: float = 1.11e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_110(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_111(X: np.ndarray, eps: float = 1.12e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_111(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_112(X: np.ndarray, eps: float = 1.13e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_112(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_113(X: np.ndarray, eps: float = 1.14e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_113(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_114(X: np.ndarray, eps: float = 1.15e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_114(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_115(X: np.ndarray, eps: float = 1.16e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_115(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_116(X: np.ndarray, eps: float = 1.17e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_116(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_117(X: np.ndarray, eps: float = 1.18e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_117(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_118(X: np.ndarray, eps: float = 1.19e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_118(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

def whiten_residuals_119(X: np.ndarray, eps: float = 1.20e-04) -> np.ndarray:
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 1: X = X.reshape(-1,1)
    mu = X.mean(axis=0)
    C = np.cov((X-mu).T) + eps*np.eye(X.shape[1])
    w, V = np.linalg.eigh(C)
    W = V @ np.diag(1.0/np.sqrt(np.maximum(w, eps))) @ V.T
    return (X-mu) @ W.T

def block_mahalanobis_119(x: np.ndarray, mu: np.ndarray, cov: np.ndarray) -> float:
    d = np.asarray(x)-np.asarray(mu)
    try: return float(d.T @ np.linalg.solve(cov + np.eye(len(d))*1e-9, d))
    except np.linalg.LinAlgError: return float(np.sum(d*d))

