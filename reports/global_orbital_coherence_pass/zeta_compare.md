# Zeta Pole Compare

Comparison of global orbital pass with and without `zeta_pole`.

## Without zeta
- R_H: 0.174195
- T_glob: 2.517631
- Lambda_glob: 0.165156
- closure_penalty: 5.475675
- spectral_radius_A: 1.716730
- spectral_gap_A: 0.792482
- fiedler_L: 0.170651
- zeta_enabled: False

## With zeta
- R_H: 0.397884
- T_glob: 3.332045
- Lambda_glob: 0.243779
- closure_penalty: 5.653751
- spectral_radius_A: 1.712657
- spectral_gap_A: 0.785051
- fiedler_L: 0.157616
- zeta_enabled: True
- zeta_tetra_defect: 0.000000
- zeta_effective_tau: 0.364500
- zeta_effective_phase: 0.000000
- zeta_coupling_norm: 0.578215

## Immediate reading
- `zeta_pole` increased global chirality in this first patch.
- But it also increased `R_H`, `T_glob`, and `closure_penalty` compared to the no-zeta baseline.
- The tetrahedron itself remained numerically rigid (`zeta_tetra_defect` ~ 0).
- This means the remaining issue is not tetrahedral rigidity, but coupling calibration into the main six-sector system.