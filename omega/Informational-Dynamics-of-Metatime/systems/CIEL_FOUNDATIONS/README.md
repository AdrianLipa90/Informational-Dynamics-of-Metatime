# CIEL Foundations

CIEL Foundations is a fresh, standalone first-principles project. It is **not** the Omega runtime and it does **not** inherit source-of-truth status from prior tarballs. Its purpose is to derive the minimal ontology, geometry, closure law, coupling structure, constants, and sector maps that Omega may later consume **only through exported constants, operators, and constraints**.

## Primary rule
Every object in the project must have four synchronized representations:
1. ontology / role
2. mathematical definition or derivation
3. executable code
4. epistemic status and tests

No formula without code. No code without formula. No interpretation without an upstream formal object.

## Canonical workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Scope
Included now:
- axioms
- state-space definitions
- derivations
- constants registry
- solver modules
- simulations and artifact tracking
- whitepapers and LaTeX sections
- bibliography and cross-reference infrastructure
- operational modes (external formalisms mapped into CIEL operational roles)
- assumptions, decisions, falsification criteria, interfaces, provenance, benchmarks

Excluded for now:
- Omega runtime
- CQCL runtime integration
- memory/agent layers
- UI/persona/prompt infrastructure

## Source of truth
Source of truth is stored in:
- Markdown / TeX for formal and explanatory text
- YAML for registries, interfaces, assumptions, provenance, and cross-reference maps
- Python for executable realization

PDF files are generated artifacts, not source of truth.



## Canonical postulate anchor
- `../../POSTULATES_CANON_PL_EN.md` — root-level bilingual canonical postulate set.
- `axioms/AX-0100-canonical-relational-phase-postulates.md` — foundations-local bridge into the same canon.
- `glossary/entries/canonical_postulates_relational_phase_formalism.md` — glossary entry for repo-wide cross-linking.

## Recent promoted derivation
- `derivations/D-0101-phase-components-from-aij-tau.md` — canonical note linking `tau_i`, `A_ij`, `Omega_ij`, `gamma_i^eff`, `Delta_H`, and the observation check.
- `constants/tau/` now records the current orbital triad and the branch distinction versus historical neutrino seeds.
- `tests/numeric/test_tau_phase_components.py` provides a minimal numeric sanity check for the tau helpers.


## Navigation layer
- `INDEX.md` — canonical navigation across axioms, definitions, derivations, constants, sectors, tests, and provenance.
- `sectors/SECTOR_INDEX.md` — sector inheritance order and promotion requirements.
- `LaTeX/sections/FOUNDATIONAL_POSTULATES.tex` — publication-ready LaTeX seed for the postulate canon.
