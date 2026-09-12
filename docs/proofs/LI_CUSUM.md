# Proof: Left-Invariant CUSUM on SO(3) (LI-CUSUM)

**Code:** `nadir_core.dashcam.math_novel.lie_cusum`

## Definition

Let \(\hat R_t\) be a filtered attitude and \(R_t\) a measurement attitude. The left-invariant innovation is

\[
e_t \;=\; \big\|\mathrm{Log}(\hat R_t^{\top} R_t)\big\|_2 \in \mathbb{R}_{\ge 0}.
\]

The LI-CUSUM statistic is \(S_0=0\) and

\[
S_t \;=\; \max\bigl(0,\; S_{t-1} + e_t - \nu\bigr),
\]

with threshold \(\lambda > 0\) and drift \(\nu > 0\). Alarm when \(S_t > \lambda\).

## Proposition 1 (nominal ARL lower bound)

Assume under \(H_0\) that \(e_t\) is i.i.d. nonnegative and \(\mathbb{E}[e^{-\theta e_1}] \le \exp(-\theta \mu + \tfrac12 \theta^2 \sigma^2)\) for some \(\mu < \nu\) (sub-exponential tail proxy). Then the average run length to false alarm satisfies

\[
\mathrm{ARL}_0 \;\ge\; \frac{\sigma}{2\nu}\,\exp\!\Big(\frac{2\lambda\nu}{\sigma^2}\Big)
\]

for the Chernoff parameter choice used in the NADIR open-core bound (`LeftInvariantCUSUM.arl_lower_bound`).

**Proof sketch.** Standard CUSUM change-detection analysis (Lordén / Siegmund) gives exponential ARL growth in \(\lambda\) when the increment \(e_t-\nu\) has negative mean under \(H_0\). Applying a Chernoff bound to the overshoot and optimizing \(\theta = 2\nu/\sigma^2\) produces the displayed constant. The bound is conservative for heavy-tailed vision innovations; it is used as a **design inequality**, not a tight calibration certificate. \(\square\)

## Proposition 2 (left-invariance)

If both \(\hat R\) and \(R\) are left-multiplied by the same \(S\in\mathrm{SO}(3)\), then \(e_t\) is unchanged.

**Proof.** \(\mathrm{Log}((S\hat R)^{\top}(SR)) = \mathrm{Log}(\hat R^{\top} R)\). \(\square\)

This is why LI-CUSUM is preferred over chart-wise CUSUM when the vehicle body frame is only known up to a fixed left action.
