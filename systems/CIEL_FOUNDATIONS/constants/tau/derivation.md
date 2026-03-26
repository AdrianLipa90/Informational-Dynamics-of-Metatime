# Derivation of tau

## Canonical role
The current runtime fixes $	au_i$ as the mode coordinates that enter both the amplitude of
$A_{ij}$ and the closure contraction $\sum_j A_{ij}	au_j$.

## Main equations
\[
\mathcal T_{ij} = \exp\!\left[-rac12\left(rac{\log(	au_i/	au_j)}{\sigma}ight)^2ight],
\qquad
A_{ij} = (w_{ij}\mathcal T_{ij}) e^{i(eta\Omega_{ij}-\gamma d_{ij})}.
\]

\[
\sum_j A_{ij}	au_j + A_{i\zeta}	au_\zeta pprox e^{i\gamma_i^{\mathrm{eff}}}.
\]

## Canonical values used by the orbital branch
\[
	au_1 = 0.263,\qquad 	au_2 = 0.353,\qquad 	au_3 = 0.489.
\]

## Branch distinction
The older Metatime / neutrino-seed branch uses
\[
(0.02, 0.05, 0.10),
\]
which should be preserved as provenance, not silently merged with the relational triad.

## Dependencies
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/metrics.py`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/dynamics.py`
- `../../derivations/D-0101-phase-components-from-aij-tau.md`
