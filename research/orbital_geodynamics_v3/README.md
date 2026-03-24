# orbital_geodynamics_v3

Third-generation orbital engine.

Adds:
- complex global transport operator \(A_{ij}(\tau_i,\tau_j,\Omega_{ij},d_{ij})\),
- tau-driven coupling amplitudes,
- Berry/Bloch/Poincaré geometry in the coupling itself,
- closure residual test \(\sum_j A_{ij}\tau_j \leftrightarrow e^{i\gamma_i}\),
- comparison run against v2.

Main files:
- `extract_real_geometry_v3.py`
- `model.py`
- `metrics.py`
- `dynamics.py`
- `run_v3_demo.py`
- `tests/test_v3_basic.py`
