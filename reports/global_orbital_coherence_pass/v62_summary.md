# v6.2 Relational Lagrangian Summary

This version derives spin, homology leak, and Poincare-disk radial flow from a single effective relational potential.

## Baseline v6.1-style legacy dynamics
- R_H: 0.149797
- T_glob: 2.527851
- Lambda_glob: 0.324731
- closure_penalty: 5.531774
- V_rel_total: 6.060749
- radial_spread: 0.190809
- mean_spin: 0.071705
- spectral_radius_A: 1.693522
- spectral_gap_A: 0.786966
- fiedler_L: 0.154083
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.004628
- zeta_coupling_norm_raw: 0.581262
- zeta_spin: 0.000000
- zeta_rho: 0.450000

## v6.2 relational lagrangian
- R_H: 0.077496
- T_glob: 2.583931
- Lambda_glob: 0.096812
- closure_penalty: 6.188151
- V_rel_total: 6.653237
- radial_spread: 0.197769
- mean_spin: 0.182682
- spectral_radius_A: 1.577124
- spectral_gap_A: 0.746650
- fiedler_L: 0.160950
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.004766
- zeta_coupling_norm: 0.003472
- zeta_coupling_norm_raw: 0.434918
- zeta_spin: 0.182682
- zeta_rho: 0.453014

## Interpretation
- v6.2 lowers R_H noticeably.
- v6.2 keeps T_glob near the same band, slightly higher than baseline in this first calibration.
- v6.2 reduces Lambda_glob and increases closure_penalty, so the first relational-Lagrangian calibration is not yet globally dominant.
- zeta remains geometrically rigid and now carries nonzero spin and radial drift.