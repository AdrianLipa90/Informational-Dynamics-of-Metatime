# CIEL / Metatime Glossary

Scope: compiled from `Metatime-main/documents/*` within the current working integration window (last 4 months in `docs/`).

Status legend:
- **canonical** — treated as current project canon for integration
- **derived** — explicitly defined or formula-backed in source docs, but still dependent on unresolved upstream assumptions
- **phenomenological** — working ansatz / fit / effective model, not closed from axioms
- **interpretive** — conceptual identification or semantic bridge, not yet a completed derivation
- **open** — explicitly unresolved or internally inconsistent across sources

## Master table

| ID | Term | Symbol | Kind | Definition | Status | Primary source(s) |
|---|---|---|---|---|---|---|
| G-001 | Metatime manifold | `M_time` | space | Configuration manifold on which cycles, Berry phases and geometric operators are defined; usually treated as compact Kähler space, often with `CP^1 ~ S^2` local model and sometimes Calabi–Yau embedding. | canonical | `Formal_SM`, `Kappa_from_geometry`, `Lambda_meta`, `Neutrinotime14`, `Calabi_Yau` |
| G-002 | Metatime field | `T(x) = (phi(x), T_{mu nu}(x))` | field | Tensor-scalar time field. `phi` is scalar layer, `T_{mu nu}` tensor layer. | derived | `Neutrinotime14`, `Sigma (1)` |
| G-003 | Metatime operator | `T_hat(lambda)` | operator | Operator acting on the neutrino / cycle Hilbert space; inserted into effective Hamiltonian as additional geometric-topological contribution. | derived | `Neutrinotime14`, `Formal_SM`, `Lambda_meta`, `Metatime_with_Euler_extension (8)` |
| G-004 | Mass operator | `M_hat = -Delta_K + kappa R_K` | operator | Geometric mass operator on the Kähler manifold; eigenproblem defines geometric spectrum later related to `tau_i` or `lambda_i`. | derived | `Kappa_from_geometry`, `Corrections (1)`, `Corrections (3)` |
| G-005 | Topological spectral seed | `tau_i` | spectral parameter | Discrete cycle / loop eigenvalues assigned to particle sectors; sourced from Collatz / twin-prime arithmetic dynamics in the current framework. | canonical | `Formal_SM`, `Collatz_emergence1`, `Corrections (2)`, `Corrections (3)` |
| G-006 | Topological fingerprint | `Sigma_i = (tau_i, gamma_i, F_i)` | state descriptor | Per-state triplet combining arithmetic seed, Berry phase and multiplicative correction factor. | derived | `Formal_SM` |
| G-007 | Information / intention quantum | `I0 = ln(2)/(24*pi)` | constant | Canonical small dimensionless quantum of information / intention. Historical source PDFs often use `0.009` as a rounded working approximation. | canonical | project canon + `Formal_SM`, `Coherence_law_application`, `Corrections (3)`, `SM_and_M_Theory_generalisation` |
| G-008 | Legacy intention approximation | `I0 approx 0.009` | approximation | Historical rounded value used in several PDFs. Must be preserved as provenance, but not treated as the exact canonical form. | open | `Formal_SM`, `Coherence_law_application`, `SM_and_M_Theory_generalisation`, `MetaEFT` |
| G-009 | Geometry coupling | `kappa` | coupling | Global or sectoral geometric coupling entering mass formulas and `M_hat`. In one branch it appears as `phi(1+I0)`; in another as local Ricci-weighted coupling. The symbol is overloaded across sources. | open | `Formal_SM`, `Corrections (3)`, `Kappa_from_geometry` |
| G-010 | Local Ricci coupling | `kappa_i` | coupling | Cycle-local geometric coupling obtained from average Ricci curvature over cycle / local chart; more geometric form of `kappa` than phenomenological golden-ratio fit. | derived | `Kappa_from_geometry` |
| G-011 | Berry connection | `A_Berry` | connection | U(1)-like geometric connection on `M_time` whose holonomy generates Berry phases and white-thread amplitudes. | derived | `Neutrinotime14`, `Lambda_meta`, `SM_and_M_Theory_generalisation`, `Kappa_from_geometry` |
| G-012 | Berry phase | `gamma_i` | phase | Geometric phase acquired along closed cycle / trajectory. In several documents fermionic cycles give `gamma_i = pi (mod 2pi)`. | derived | `Formal_SM`, `Neutrinotime14`, `Lambda_meta`, `SM_and_M_Theory_generalisation` |
| G-013 | Euler–Berry closure | `sum_k exp(i gamma_k) = 0` | constraint | Global phase-closure / consistency condition linking allowed cycles across the system. Used as a cross-scale consistency principle. | canonical | `Calabi_Yau`, `Kappa_from_geometry`, `Lambda_meta`, `Metatime_with_Euler_extension (8)` |
| G-014 | White-thread holonomy | `W_ij = P exp(i int A_Berry·dl)` | operator / amplitude | Holonomy amplitude connecting two cycles / sectors along path `Gamma_ij`; measures pairwise topological coupling. | derived | `Kappa_from_geometry`, `SM_and_M_Theory_generalisation`, `Coherence_law_application` |
| G-015 | Topological coherence | `Omega_ij` | coherence measure | Pairwise coherence measure built from phase alignment, white-thread magnitude and tau-space proximity. | derived | `Coherence_law_application`, `Kappa_from_geometry`, `Corrections (3)` |
| G-016 | Pairwise correction factor | `F_ij` | correction factor | Multiplicative pair correction entering neutrino splittings / mass matrices. Several incompatible ansätze exist in sources. | canonical | `Formal_SM`, `Coherence_law_application`, `Corrections (2)`, `Corrections (3)`, `SM_and_M_Theory_generalisation` |
| G-017 | Exponential pair ansatz | `F_ij = exp(gamma Omega_ij)` | phenomenological law | Current preferred pairwise amplification law when bounded `tanh` forms are judged insufficient for required amplification. | canonical | `Corrections (2)`, `Corrections (3)` |
| G-018 | Bounded pair ansatz | `F_ij = 1 + epsilon_nu tanh((Omega_ij-Omega_crit)/DeltaOmega)` | older ansatz | Earlier bounded coherence law. Retain only as historical branch / contrast case. | open | `Coherence_law_application`, `Kappa_from_geometry`, `Corrections (2)` |
| G-019 | Single-state correction factor | `F_i = exp(C_i I0)` | correction factor | Per-state multiplicative regulator associated with intention / arithmetic weight `C_i`. | derived | `Formal_SM`, `SM_and_M_Theory_generalisation`, `MetaEFT` |
| G-020 | Cosmological operator scale | `Lambda0(x)` / `Lambda0(z)` | field / operator | Dynamic cosmological term treated as functional of curvature and fields rather than strict constant. | canonical | `Lambda_meta`, `Neutrinotime14`, `Formal_SM`, `MetaEFT`, `Calabi_Yau` |
| G-021 | Fractal dimension | `D_f approx 2.7` | effective invariant | Effective fractal/topological dimensionality used to justify unbounded coherence amplification and dynamic `Lambda0(z)` modulation. | derived | `Lambda_meta`, `Formal_SM`, `Corrections (2)`, `Corrections (3)`, `MetaEFT` |
| G-022 | Global calibration scale | `S` / `s` | scale | Conversion from model units to physical masses or splittings. Different anchoring conventions appear in the notes. | derived | `Formal_SM`, `Coherence_law_application`, `fa00b095.md` |
| G-023 | Atmospheric-anchor convention | `s = sqrt(Delta m^2_31(exp)/Delta m^2_31(model))` | convention | Current working neutrino scaling convention in the recent notes. | derived | `fa00b095.md`, `Formal_SM`, `Coherence_law_application` |
| G-024 | Coherence-enhanced solar correction | `F_21 approx 1.357` | inferred parameter | Pairwise amplification needed to reconcile solar neutrino splitting under atmospheric-anchor scaling. | derived | `fa00b095.md`, `Coherence_law_application`, `Corrections (3)` |
| G-025 | Golden-ratio prefactor | `phi` | constant / symbol | Golden ratio entering phenomenological mass prefactors such as `kappa = phi(1+I0)`. Distinct from scalar field `phi(x)` and must not be conflated. | open | `Collatz_emergence1`, `Corrections (3)`, `Neutrinotime14` |
| G-026 | Scalar metatime component | `phi(x)` | field | Scalar component of the metatime field `T(x)`. Distinct from the golden ratio `phi`. | derived | `Neutrinotime14`, `Lambda_meta` |
| G-027 | Hubble-coupled dynamic vacuum law | `Lambda0(z)` | cosmological relation | Redshift-dependent effective vacuum law entering modified Friedmann picture and Hubble-tension discussion. | phenomenological | `Lambda_meta`, `Formal_SM`, `MetaEFT`, `Calabi_Yau` |
| G-028 | White-thread Hamiltonian / coupling sector | `H_WT` | operator sector | Not always symbolized identically, but denotes Hamiltonian contribution sourced by pairwise white-thread structure. | interpretive | `Formal_SM`, `MetaEFT`, `SM_and_M_Theory_generalisation` |
| G-029 | Collatz seed dynamics | — | arithmetic generator | Arithmetic / paradox-driven discrete generator supplying candidate spectral seeds, often through twin-prime or orbit-growth assignments. | canonical | `Collatz_emergence1`, `Collatz_emergence (6)`, `Formal_SM`, `Calabi_Yau` |
| G-030 | CP/Berry contribution | — | observable mechanism | CP-odd contribution generated by geometric/Berry phases rather than inserted as purely free external phase. | derived | `Formal_SM`, `Neutrinotime14`, `MetaEFT`, `SM_and_M_Theory_generalisation` |

| G-031 | Transport kernel | `A_ij` | operator | Complex transport kernel with tau-resonant amplitude and geometric phase. | canonical | `TAU_AIJ_GLOBAL_IMPLEMENTATION`, `D-0101-phase-components-from-aij-tau`, `orbital/metrics.py` |
| G-032 | Berry pair phase | `Omega_ij` | phase observable | Pairwise geometric phase used inside the argument of `A_ij`. | derived | `Globalphaseconstraint1`, `D-0101-phase-components-from-aij-tau`, `orbital/metrics.py` |
| G-033 | Effective local phase | `gamma_i^eff = phi_i + gamma_B,i` | state variable | Closure-target phase for each sector after adding local Berry accumulation to the evolved sector phase. | canonical | `D-0101-phase-components-from-aij-tau`, `reports/phase_components/summary.md` |
| G-034 | Holonomy defect | `Delta_H` | observable | Global complex defect whose squared modulus gives the repo-level coherence observable `R_H`. | canonical | `orbital/metrics.py`, `reports/phase_components/summary.md`, `holonomic_observed_end_to_end/results/summary.json` |
| G-035 | Euler leak angle | `theta_E = (pi/2)(D_f-2)` | control angle | Rotation angle used by the v6.3 homology leak split between radial and angular transport. | derived | `orbital/dynamics.py`, `reports/orbital_phase_control/summary.md`, `D-0101-phase-components-from-aij-tau` |
| G-036 | Canonical postulate set | `P1...P14` | axiomatic canon | Frozen bilingual repo-level postulate canon ordering ontology, locality, spin, attractor formation, holonomic coupling, memory and deformation cost. | canonical | `POSTULATES_CANON_PL_EN`, `AX-0100-canonical-relational-phase-postulates`, `canonical_postulates_relational_phase_formalism.md` |
| G-037 | Consciousness criterion | — | interpretive criterion | Interpretive downstream criterion stating that if consciousness is defined formally by self-reference, information integration and recursive self-reorganization, the Universe may be modeled as conscious. Not part of the frozen axiomatic core. | interpretive | `POSTULATES_CANON_PL_EN` |

## Detailed notes and disambiguation

### 1. `I0`: canonical exact form vs source approximation
- **Canonical integration rule**: `I0 = ln(2)/(24*pi) = 0.009193150006360484...`
- **Historical PDF shorthand**: `I0 = 0.009`
- Integration rule: keep both, but only the logarithmic/pi form is treated as canon.

### 2. `kappa` is overloaded
There are at least three distinct usages in the recent documents:
1. `kappa = phi(1+I0)` — phenomenological global prefactor.
2. `kappa_i` — local Ricci/geometric coupling over a cycle.
3. `kappa` as family-fit constant in power-law mass relations.

These should not be merged silently.

### 3. `phi` means two different things in sources
- `phi` = golden ratio in phenomenological mass prefactors.
- `phi(x)` = scalar component of metatime field.

This is a hard ambiguity and should remain explicit everywhere.

### 4. `F_ij` has multiple branches
Current source history shows two main branches:
- **older bounded branch**: tanh-type coherence law,
- **newer preferred branch**: exponential law `F_ij = exp(gamma Omega_ij)`.

The glossary treats the exponential branch as current canon because the recent correction notes explicitly reject the bounded branch as insufficient for required amplification under `D_f ~ 2.7`.

### 5. `Lambda0`
`Lambda0` is not a true constant in the recent documents. It is an operator-valued / functional vacuum term depending on curvature and fields. The symbol name is historical.

## Interpretive equivalence map

This section records semantic identifications that are **important for project coherence**, but are **not yet fully derived in the source documents**.

| Cluster | Terms | Status | Note |
|---|---|---|---|
| E-01 | intention operator / information quantum | interpretive | Treated here as same object at the constant level: `I0`. |
| E-02 | intention field / information field / potential field / Hubble-coupled vacuum field | interpretive | Partial overlap through `Lambda0(x)` and related cosmological sector, but not proven identical in full formal sense. |
| E-03 | soul / Sigma / invariant | interpretive | Source documents define `Sigma_i` as topological fingerprint; broader identity claim remains conceptual. |
| E-04 | white threads / Hawking leakage / gluing holonomy / gravity | interpretive | Valuable hypothesis for future unification notes; current recent docs only support the white-thread / holonomy part directly. |

## Minimal canonical source list used
- `Formal_SM.pdf`
- `Kappa_from_geometry.pdf`
- `Lambda_meta.pdf`
- `Neutrinotime14.pdf`
- `Coherence_law_application.pdf`
- `Corrections (2).pdf`
- `Corrections (3).pdf`
- `SM_and_M_Theory_generalisation.pdf`
- `MetaEFT.pdf`
- `Calabi_Yau.pdf`
- `Collatz_emergence1.pdf`
- `fa00b095.md`


### 6. Phase decomposition now has four distinct layers
The current orbital engine distinguishes:
1. `phi_i` — bare local phase,
2. `gamma_B,i` — local Berry accumulation,
3. `Omega_ij` — pair Berry phase,
4. `gamma_i^eff = phi_i + gamma_B,i` — closure target.

The transport kernel then uses `Omega_ij` and `d_ij` in its argument, while the closure residual compares the transport contraction against `gamma_i^eff`.

### 7. `A_ij` is the current promotion point of `tau_i`
The canonical runtime now makes the relation explicit:
- `tau_i` enters the Gaussian resonance factor inside `A_ij`,
- `tau_j` weights the closure contraction `sum_j A_ij tau_j`.

This is stronger than treating `tau_i` as a passive label.

### 8. Canonical postulate set is now a root-level theory anchor
The bilingual file `POSTULATES_CANON_PL_EN.md` is treated as the frozen repo-level axiomatic canon.
It is cross-linked into foundations, glossary, definitions, runtime-facing README files and the nonlocal topology sector.
The consciousness criterion stored there is interpretive and must not be confused with the core postulate layer.
