# Global orbital geodynamics v3 report

## What changed

v3 replaces static real-mesh couplings with a complex transport operator:

\[
A_{ij} = A_{ij}(	au_i, 	au_j, \Omega_{ij}, d_{ij})
\]

where:
- coupling amplitude depends on the \(	au_i/	au_j\) resonance,
- coupling phase depends on Berry/Bloch/Poincare geometry,
- dynamics uses the closure residual
\(\sum_j A_{ij}	au_j \leftrightarrow e^{i\gamma_i}\)
inside the update rule.

## Test status

- `tests/test_v3_basic.py` -> passed
- `tests/test_v3_vs_v2.py` -> passed

## Comparison: v2 vs v3 after 20 steps

### Global coherence
- v2 final \(R_H\): **1.248511**
- v3 final \(R_H\): **0.278533**

Improvement factor:

\[
rac{R_H^{(v2)}}{R_H^{(v3)}} pprox 4.482
\]

### Global chord tension
- v2 final \(T_{glob}\): **10.192459**
- v3 final \(T_{glob}\): **3.922352**

### Global chirality
- v2 final \(\Lambda_{glob}\): **0.008770**
- v3 final \(\Lambda_{glob}\): **0.833059**

### Closure penalty (v3 only)
- initial closure penalty: **7.197595**
- final closure penalty: **7.236776**

## Interpretation

v3 is globally better than v2 in the most important metric:
- it preserves a much lower global holonomy defect after evolution,
- it keeps chord tension lower,
- and it sustains a strong nonzero chirality.

This means the repo-level geometry derived from \(A_{ij}	au_i\) is more stable than the hand-weighted real-mesh dynamics.

## Remaining issue

The closure penalty does **not** yet relax downward. This means that the system-level geometry is improved, but the strict local closure equation

\[
\sum_j A_{ij}	au_j \leftrightarrow e^{i\gamma_i}
\]

is not yet fully self-tuning.

So the next tuning target is not the global geometry anymore. It is the **local closure relaxation law**.
