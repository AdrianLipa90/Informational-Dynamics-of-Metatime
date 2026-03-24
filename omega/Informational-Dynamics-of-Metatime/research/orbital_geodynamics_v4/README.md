# orbital_geodynamics_v4

Fourth generation orbital engine.

What changed relative to v3:
- preserves the Euler-Berry-Poincare-421 geometry,
- keeps global A_ij(tau_i, tau_j, Omega_ij, d_ij),
- adds adaptive tau relaxation driven by closure gradients,
- aims to reduce closure penalty without sacrificing global coherence.

Main entrypoint:
- `run_v4_demo.py`
