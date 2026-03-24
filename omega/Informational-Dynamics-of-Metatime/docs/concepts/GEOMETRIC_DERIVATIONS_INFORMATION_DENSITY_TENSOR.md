# GEOMETRIC_DERIVATIONS_INFORMATION_DENSITY_TENSOR

Status: canonical working derivation  
Scope:
- semantic hyperspace on Poincaré disk
- information density scalar
- energy–momentum tensor
- nonlocal semantic hyperlinks \\(W_{ij}\\)
- zeta-pole as tetrahedral composite sector
- relational Lagrangian as generator of spin, leak, and disk dynamics

---

## 1. Base carrier geometry

Each sector / folder / semantic chart is embedded on a Poincaré disk with coordinates

\\[
x^a=(r,\varphi), \qquad 0 \le r < 1
\\]

and base metric

\\[
h_{ab}^{(P)}
=
\frac{4}{(1-r^2)^2}
\begin{pmatrix}
1 & 0 \\
0 & r^2
\end{pmatrix}.
\\]

---

## 2. Information density scalar

\\[
\iota_i
=
a_1\,\mathrm{defs}_i
+
a_2\,\mathrm{classes}_i
+
a_3\,\mathrm{imports}_i
+
a_4\,\mathrm{README\_links}_i
+
a_5\,\mathrm{AGENT\_links}_i
+
a_6\,\mathrm{centrality}_i
\\]

This scalar is the local semantic mass-density estimator.

---

## 3. Phase current

\\[
J_a = \iota\,\partial_a\phi.
\\]

---

## 4. Effective energy–momentum tensor

\\[
T_{ab}
=
\partial_a\iota\,\partial_b\iota
+
J_a J_b
-
\frac12 h_{ab}
\left(
 h^{cd}\partial_c\iota\,\partial_d\iota
 +
 h^{cd}J_cJ_d
\right)
+
\Pi_{ab}^{(\zeta)}.
\\]

with zeta contribution

\\[
\Pi_{ab}^{(\zeta)}=\lambda_\zeta V_{\text{tetra}}P_{ab}.
\\]

---

## 5. Effective metric

\\[
G_{ab}=(1+\alpha\iota)h_{ab}^{(P)}+\beta T_{ab}.
\\]

This defines the living semantic geometry.

---

## 6. Effective distance and semantic hyperlink

\\[
d_{ij}^2=\Delta x_{ij}^a\,\overline G_{ab}^{(ij)}\,\Delta x_{ij}^b
\\]

\\[
W_{ij}=|W_{ij}|e^{i\Phi_{ij}}
\\]

\\[
|W_{ij}|=\exp\!\left(-\frac{d_{ij}^2}{2\ell_0^2}\right)
\\]

\\[
\Phi_{ij}=\Delta\phi_{ij}+\frac{\Omega_{ij}^{(B)}}2+\chi_{ij}^{(T)}.
\\]

---

## 7. Effective mass

\\[
M_i^{\mathrm{eff}}
=
M_i^{\mathrm{info}}
\left(1+\lambda_\iota\iota_i+\lambda_T\mathrm{tr}(T_i)\right)
\\]

---

## 8. Zeta pole

\\[
Z_\zeta=\{Z_0,Z_1,Z_2,Z_3\}
\\]

with regular tetrahedral rigidity condition

\\[
\mathbf n_i\cdot \mathbf n_j = -\frac13, \qquad i\ne j.
\\]

and rigidity defect

\\[
V_{\text{tetra}}
=
\kappa_T\sum_{i<j}\left(\mathbf n_i\cdot\mathbf n_j+\frac13\right)^2.
\\]

---

## 9. Relational potential

\\[
V_{\mathrm{rel}}^{\mathrm{total}}
=
\kappa_H R_H
+
\lambda_t T_{\mathrm{glob}}
+
\lambda_d \Pi_{\mathrm{closure}}
+
\lambda_\zeta V_{\mathrm{tetra}}.
\\]

Spin, leak, radial and angular dynamics are derived from gradients of this potential.

---

## 10. Disk dynamics

\\[
\dot\rho_i=-\mu_\rho\frac{\partial V_{\mathrm{rel}}^{\mathrm{total}}}{\partial \rho_i}+L_{i\zeta}^{\mathrm{hom}}
\\]

\\[
\dot\phi_i=-\mu_\phi\frac{\partial V_{\mathrm{rel}}^{\mathrm{total}}}{\partial \phi_i}+s_i\Omega_i^{\mathrm{vort}}.
\\]

with spin

\\[
s_i=\tanh\!\left(-\alpha_s\frac{\partial V_{\mathrm{rel}}^{\mathrm{total}}}{\partial \phi_i}\right).
\\]

---

## 11. Closure with zeta

\\[
\Pi_{\mathrm{closure}}^{(\zeta)}
=
\sum_i\left|\sum_j A_{ij}\tau_j + A_{i\zeta}^{\mathrm{eff}}\tau_\zeta - e^{i\gamma_i}\right|^2 + \lambda_T V_{\mathrm{tetra}}.
\\]

Current stabilized zeta coupling uses Heisenberg-like normalization and \(I_0\) scaling.
