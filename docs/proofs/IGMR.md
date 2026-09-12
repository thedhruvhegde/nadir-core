# Proof: Information Geometric Mount Residual (IGMR)

**Status:** NADIR Open Core formulation (2026).  
**Code:** `nadir_core.dashcam.math_novel.igmr`

## Setup

Let mount attitude on a local chart be \(z = (\phi, \theta, \psi)^\top \in \mathbb{R}^3\) (roll, pitch, yaw). Maintain a Gaussian posterior \(q_t = \mathcal{N}(m_t, C_t)\) in information form \(P_t = C_t^{-1}\).

A measurement is modeled as \(z_t \sim \mathcal{N}(z_t^{\mathrm{true}}, R)\) with precision \(P_z = R^{-1}\).

## Definition (IGMR)

The **information geometric mount residual** at time \(t\) is

\[
\rho_t \;=\; \tfrac{3}{4}\, d_{\mathrm{FR}}(q_{t-}, q_{t+}) \;+\; \tfrac{1}{4}\,\big\|\mathrm{Log}(R(m_{t-})^{\top} R(z_t))\big\|_2
\]

where \(q_{t-}\) is the prior posterior, \(q_{t+}\) is the Bayesian update of \(q_{t-}\) by \(z_t\), \(d_{\mathrm{FR}}\) is the Fisher–Rao geodesic distance between Gaussians on the chart, and \(R(\cdot)\) maps chart coordinates to \(\mathrm{SO}(3)\).

## Proposition 1 (Bayesian update is well-defined)

If \(P_{t-} \succ 0\) and \(P_z \succ 0\), then \(P_{t+} = P_{t-} + P_z \succ 0\) and

\[
m_{t+} = P_{t+}^{-1}(P_{t-} m_{t-} + P_z z_t).
\]

**Proof.** Sum of SPD matrices is SPD. The displayed mean is the unique critical point of the strictly convex quadratic \(m \mapsto (m-m_{t-})^{\top} P_{t-}(m-m_{t-}) + (m-z_t)^{\top} P_z(m-z_t)\). \(\square\)

## Proposition 2 (Fisher–Rao split)

For Gaussians on \(\mathbb{R}^d\) with means \(m_i\) and covariances \(C_i\),

\[
d_{\mathrm{FR}}^2(q_0,q_1) \;=\; (m_1-m_0)^{\top} \bar C^{-1}(m_1-m_0) \;+\; \big\|\log(C_0^{-1/2} C_1 C_0^{-1/2})\big\|_F^2
\]

with \(\bar C = \tfrac12(C_0+C_1)\) used as a NADIR chart approximation to the mean-metric coupling (exact Amari product metric separates mean and covariance when the manifold is parameterized accordingly). The second term is the affine-invariant distance on \(\mathrm{SPD}(d)\).

**Proof sketch.** On the Gaussian statistical manifold the Fisher information block-diagonalizes in \((\mathrm{mean}, \mathrm{covariance})\) coordinates for location-scale families after reparameterization; the covariance block is the affine-invariant metric \(\langle H,K\rangle_C = \mathrm{tr}(C^{-1} H C^{-1} K)\), whose geodesics yield the log-Euclidean / affine-invariant length above. NADIR uses the arithmetic mean covariance for the mean block as a stable open-core approximation (error \(O(\|C_0-C_1\|^2)\)). \(\square\)

## Proposition 3 (Lie guard)

If \(\|\mathrm{Log}(R_0^{\top} R_1)\| \ge \pi - \varepsilon\), the chart distance alone can understate attitude error near coordinate singularities. Mixing a left-invariant SO(3) term with weight \(1/4\) yields a residual that remains bi-Lipschitz to the Riemannian distance on \(\mathrm{SO}(3)\) on any compact set avoiding a neighborhood of antipodes.

**Proof sketch.** On a compact \(K\subset\mathrm{SO}(3)\) with injectivity-radius margin \(\varepsilon\), \(\|\mathrm{Log}(R_0^{\top} R_1)\|\) is comparable to geodesic distance. Chart coordinates are smooth embeddings on a slightly smaller set; linear combination with positive weights preserves the bi-Lipschitz property. \(\square\)

## Corollary (detection monotonicity)

If a physical mount yaw increases while pitch/roll stay fixed and measurement noise is isotropic, \(\rho_t\) is eventually increasing in the yaw offset. Thus IGMR is a valid one-dimensional detection statistic for the NADIR dashcam lane.
