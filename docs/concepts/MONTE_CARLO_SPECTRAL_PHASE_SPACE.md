# MONTE_CARLO_SPECTRAL_PHASE_SPACE

This note records the next methodological step after v4 adaptive tau closure:

1. sample the free parameter space,
2. evaluate distributions of:
   - R_H
   - T_glob
   - Lambda_glob
   - closure_penalty
3. compute spectral observables from A_ij and the induced Laplacian,
4. identify which parameters truly control stability.

Interpretation:
Single runs are no longer enough.
The orbital model must be understood as a phase space with stable and unstable regions.
