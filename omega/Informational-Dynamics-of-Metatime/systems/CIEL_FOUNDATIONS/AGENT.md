# AGENT.md

## Purpose

This file defines the operational rules for any agent, assistant, or automated process working inside `CIEL_FOUNDATIONS`.

The repository is the canonical source of truth for the project.

---

## Core Operating Rule

After **every prompt / task / change**, the agent must update the repository state so that the repository remains globally synchronized.

The agent must **never** treat a partial sector, fragment, temporary subset, isolated folder, or local scratch result as the project source of truth.

The agent must always work against the **full, current repository**.

---

## Mandatory Rules

### 1. Full-repository discipline
- Always use the full, up-to-date repository as the source of truth.
- Never work as if one module, sector, folder, or temporary extract were the whole project.
- Never perform project changes on detached fragments without propagating them back into the full repository structure.

### 2. Post-prompt synchronization
After every prompt, the agent must check whether the prompt changes:
- structure
- glossary
- derivations
- constants
- interfaces
- simulations
- verification
- bibliography
- operational modes
- artifact/provenance records
- roadmap / organization / methodology files

If yes, the repository must be updated accordingly.

### 3. Cross-reference integrity
Any new object or modification must be checked for impact on:
- `glossary/`
- `derivations/dependency_graph.yaml`
- `derivations/code_map.yaml`
- `constants/registry.yaml`
- `verification/diff_registry.yaml`
- `assumptions/`
- `decisions/`
- `falsification/`
- `Simulations/registry.yaml`
- bibliography and whitepaper links

### 4. No partial truth
A local derivation, test, code snippet, notebook, or temporary file is not canonical until:
- it is inserted into the repository,
- linked to the proper registries,
- assigned an epistemic status,
- cross-referenced to its dependencies.

### 5. Dual-track methodology must be preserved
The agent must preserve all three tracks:
- canon extraction
- raw re-derivation
- reconciliation

No major object is considered closed until reconciliation status is recorded.

### 6. Every stable object must be representable in repository form
Each stable project object should be reflected through repository artifacts such as:
- glossary row
- glossary entry
- derivation node
- code binding
- tests
- status / reconciliation entry
- artifact links where relevant

### 7. Repository-wide consistency over local convenience
If a local change is easy but would leave the rest of the repository inconsistent, the change is incomplete and must not be treated as finished.

### 8. PDFs and tarballs are downstream artifacts
Generated PDFs, tarballs, exports, and bundles are not the source of truth.
They must be regenerated from the repository after the source state is updated.

---

## Required Update Checklist

When relevant, after each task the agent should verify and update:

1. `README.md`
2. `PROJECT_CHARTER.md`
3. `ROADMAP.md`
4. `STRUCTURE.md`
5. `ORGANIZATION.md`
6. `glossary/registry.csv`
7. `glossary/registry.yaml`
8. `glossary/entries/*`
9. `axioms/registry.yaml`
10. `derivations/dependency_graph.yaml`
11. `derivations/code_map.yaml`
12. `constants/registry.yaml`
13. `verification/diff_registry.yaml`
14. `assumptions/registry.yaml`
15. `decisions/`
16. `falsification/matrix.yaml`
17. `interfaces/*.yaml`
18. `Simulations/registry.yaml`
19. `operational_modes/registry.yaml`
20. `reverse_operational_modes/registry.yaml`
21. `artifacts/registry.yaml`
22. `provenance/lineage.yaml`

Not every file must change after every prompt, but every prompt must be checked against the full repository impact surface.

---

## Epistemic Rule

The agent must not silently convert:
- hypothesis into derivation,
- fit into first-principles result,
- interpretation into formal definition,
- fragment into canonical whole.

All such transitions must be explicit in repository state.

---

## Completion Rule

A task is not complete until:
1. the relevant source files are updated,
2. the repository is internally consistent,
3. cross-references are not left stale,
4. downstream artifact packaging is refreshed if needed.

---

## Short Rule

**Always work on the full, current repository.  
Never treat a fragment as the whole project.  
After every prompt, synchronize the repository state.**
