# ZETA_POLE_HEISENBERG_I0_NORMALIZATION

This note introduces v6.1 normalization for `zeta_pole`.

## Rule

The effective zeta coupling is no longer used raw. It is normalized by a Heisenberg-style soft clip and scaled by the Information Operator:

\[
A_{i\zeta}^{eff} = I_0\,rac{A_{i\zeta}}{\sqrt{1 + lpha |A_{i\zeta}|^2}}
\]

where:
- \(I_0\) sets the small relational coupling scale,
- \(lpha\) bounds excessive zeta influence without hard clipping.

## Intent

The goal is to keep the tetrahedral zeta frame active while preventing it from overcoupling to the six-sector global system.
