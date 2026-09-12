# Proof: Soft Coupling Energy (SCE) for vision→Pulse bridge

**Code:** `nadir_core.dashcam.math_novel.bridge_coupling`

## Definition

For mount errors \(v = (y,p,r)^{\top}\) in degrees,

\[
E(v) \;=\; v^{\top} Q v,
\qquad
Q \;=\;
\begin{pmatrix}
\alpha & c_{yp} & c_{yr} \\
c_{yp} & \beta & c_{pr} \\
c_{yr} & c_{pr} & \gamma
\end{pmatrix}
\]

with open-core constants \(\alpha=0.35,\beta=0.25,\gamma=0.15\), \(c_{yp}=0.08\), \(c_{yr}=0.05\), \(c_{pr}=0.04\).

Bridge scalar: \(s(E) = \frac{10}{k}\log(1+k E)\) with \(k=1.4\).

## Proposition 1 (Q is SPD)

All leading principal minors of \(Q\) are positive; hence \(Q\succ 0\) by Sylvester’s criterion.

**Proof.**  
\(\alpha = 0.35 > 0\).  
\(\det\begin{pmatrix}\alpha&c_{yp}\\c_{yp}&\beta\end{pmatrix} = \alpha\beta - c_{yp}^2 = 0.0875 - 0.0064 = 0.0811 > 0\).  
\(\det Q\) expands to \(0.00911 > 0\) (numeric evaluation in `coupling_matrix_eigs()`; all eigenvalues positive). \(\square\)

## Proposition 2 (monotone bridge)

\(s'(E) = 10/(1+kE) > 0\) for \(E\ge 0\), so larger coupling energy always yields a larger Pulse-like proxy. Near \(0\), \(s(E)\sim 10 E\).

## Proposition 3 (soft cross-modal meaning)

Off-diagonal terms encode the modeling judgment that windshield yaw creep weakly co-occurs with pitch/roll sag. Because \(Q\succ 0\), there is no direction of pure cancellation that drives \(E=0\) for nonzero \(v\). That prevents “canceling” a large yaw fault by an opposite pitch reading inside the bridge scalar.
