# GLOBAL_ORBITAL_IMPLEMENTATION

This note marks the transition from research-only orbital engines to a global read-only implementation inside
`systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/orbital/`.

Current status:
- geometry extracted from real repo structure,
- README mesh and AGENT mesh included,
- global \(A_{ij}(\tau_i,\tau_j,\Omega_{ij},d_{ij})\) computed inside the canonical package,
- read-only coherence pass available in `integrations/run_global_orbital_coherence_pass.py`,
- outputs written to `reports/global_orbital_coherence_pass/` and `manifests/orbital/`.

This is the first global implementation stage.
It is diagnostic, not yet auto-corrective.
