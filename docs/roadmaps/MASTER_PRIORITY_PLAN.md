# MASTER PRIORITY PLAN

Status: active canonical priority
Scope: whole consolidated repository
Priority owner: repository-level global coordination

## Mission
Transform the current consolidated bundle into a fully coherent, explicitly layered, reproducible system in which runtime, memory, topology, storage, inference, and documentation evolve under one canonical plan rather than ad hoc local edits.

## Standing rules
- Use the full current repository as the source of truth.
- Do not patch isolated sectors without checking their relations to the rest of the repository.
- Every structural change must update manifests, documentation, and nonlocal topology when relevant.
- Missing files, disappearing files, stale manifests, and packaging inconsistencies must be reported explicitly.
- Prefer reference correctness and reproducibility before performance work.

## Global architecture target

### Layer A — Canonical runtime
Path:
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/`

Role:
- execution facade
- bridge routing
- constraints and closure
- memory operators
- vocabulary and identity stabilization
- orbital and inference integration

### Layer B — Storage backends
Target paths:
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/storage/ledger/`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/storage/semantic/`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/storage/tensor/`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/storage/graph/`

Role:
- persistent ledger and provenance
- semantic/document memory
- tensor and wave archive
- dependency and relation graph persistence

### Layer C — Graph truth and nonlocal topology
Paths:
- `manifests/import_dependency_graph.*`
- `NONLOCAL_REPO_HYPERSPACE/`
- `manifests/orbital/`

Role:
- syntactic dependency truth
- semantic/nonlocal routing map
- orbital state/control/health manifests

### Layer D — Research and theory extensions
Paths:
- `research/`
- `docs/concepts/`
- `TODO/`

Role:
- incubate new theory and experiments without silently deforming canonical runtime
- promote only after explicit validation

### Layer E — Documentation and publication
Paths:
- `docs/`
- `LaTeX/` (to be normalized if missing)
- `glossary/` (to be normalized if missing)

Role:
- reproducible explanation
- cross-reference mesh
- equation and symbol registry

## Master workstreams

### P0 — Canonical integrity and hygiene
Goal:
- stabilize the repository as one auditable source of truth

Tasks:
- remove packaging residue (`__pycache__`, transient DB/cache artifacts, stale generated noise) from canonical deliverables
- verify archive inventories and compare against manifests
- keep runtime canon, references, TODO imports, and research sectors clearly separated
- re-run compile/test/demo smoke checks after structural changes

Deliverables:
- clean inventory
- updated manifests
- explicit discrepancy reports

Exit condition:
- canonical repo can be packed without hidden residue and with current manifests

### P1 — Memory/storage boundary formalization
Goal:
- separate logical memory from physical persistence

Tasks:
- keep `memory/` for episodic, semantic, procedural, identity, affective, and working memory logic
- move storage implementations out of memory monolith into explicit storage adapters
- define semantic roles of ledger, semantic store, tensor store, and graph store

Deliverables:
- storage architecture note
- refactored package layout
- migration map from existing storage files

Exit condition:
- runtime logic no longer depends directly on backend-specific libraries in core memory flows

### P2 — Storage ports and interface extraction
Goal:
- make runtime and bridge depend on interfaces, not concrete backends

Tasks:
- define `LedgerPort`, `SemanticStorePort`, `TensorStorePort`, `GraphStorePort`
- provide at least one reference backend per port
- add fallback-safe adapters where optional dependencies are absent

Deliverables:
- port interfaces
- backend adapters
- compatibility tests

Exit condition:
- memory, bridge, and constraints can operate through ports

### P3 — Graph truth layer and nonlocal topology
Goal:
- establish a hard syntactic and relational truth layer before adding more abstraction

Tasks:
- maintain `import_dependency_graph.json` and `import_dependency_graph.md`
- generate folder adjacency and sector relation graphs
- synchronize `NONLOCAL_REPO_HYPERSPACE` with current repo topology
- map runtime, research, docs, TODO, and reference sectors into one navigable structure

Deliverables:
- updated import graph
- sector relation graph
- nonlocal registry updates
- orbital navigation map

Exit condition:
- structural relations are machine-readable and human-readable

### P4 — Command quantization and admissibility rules
Goal:
- formalize repository and runtime actions as an explicit operator alphabet

Tasks:
- convert action semantics (`run`, `route`, `resolve`, `stabilize`, `link`, and future operators) into a canonical command alphabet
- define admissibility conditions per operator
- bind operators to sectors and manifests
- connect command semantics to AGENT files and orbital control manifests

Deliverables:
- command alphabet manifest
- admissibility policy note
- synchronized AGENT mesh

Exit condition:
- key actions are no longer implicit or only narrative

### P5 — Braid/knot closure layer
Goal:
- represent path-dependent meaningful loops with explicit topological invariants

Tasks:
- identify loops where order and closure defect matter
- keep ordinary control flow in graphs/state machines
- use braid/knot invariants only for nontrivial closure-sensitive loops
- add closure admissibility rules to constraints

Deliverables:
- loop specification format
- braid closure module extensions
- closure diagnostics

Exit condition:
- selected loops have explicit invariant-aware closure checks

### P6 — Observability, traces, and replay
Goal:
- make runtime evolution inspectable and replayable

Tasks:
- promote introspection/demo code into a stable `observability/` sector
- log input events, routing decisions, memory deltas, semantic matches, closure reports, rollback decisions, and tensor snapshot references
- attach traces to ledger provenance

Deliverables:
- trace schema
- replay/debug tools
- example trace outputs

Exit condition:
- important runs can be inspected and replayed coherently

### P7 — Optional native kernels and backend acceleration
Goal:
- accelerate only verified hot paths without destabilizing semantics

Tasks:
- keep Python as orchestration/reference layer
- add native kernels only behind stable interfaces
- start with closure scans, pairwise phase kernels, braid invariants, parsing/compression hotspots if benchmarks justify it
- require Python/NumPy fallback implementations

Candidate stack:
- Rust via PyO3 for deterministic performance-critical kernels

Deliverables:
- benchmark suite
- optional native backend bridge
- fallback parity tests

Exit condition:
- performance gains are measured and semantics remain stable with fallback paths

### P8 — Inference/runtime integration hardening
Goal:
- stabilize GGUF/orbital/inference pathways as first-class but bounded integrations

Tasks:
- normalize inference configuration and manifests
- document three-prompt/orbital runner assumptions and limits
- isolate backend-specific runtime dependencies from canonical memory/constraint logic
- add reproducible smoke tests for inference paths

Deliverables:
- inference integration note
- stable configs
- smoke-test reports

Exit condition:
- inference integrations are reproducible and do not silently deform core architecture

### P9 — Documentation, glossary, LaTeX, and cross-reference completion
Goal:
- make the whole project readable, navigable, and publication-ready

Tasks:
- normalize or create `glossary/` with symbol/equation/function/derivation registry
- normalize or create `LaTeX/` with section-based publication workflow
- cross-link docs, code, manifests, and research artifacts
- keep README and local AGENT files synchronized with structural truth

Deliverables:
- glossary registry
- publication scaffold
- cross-reference matrix

Exit condition:
- symbols, equations, code sectors, and documents can be traced coherently

### P10 — Packaging, release validation, and regression control
Goal:
- ensure the whole repo can be released cleanly and revalidated repeatedly

Tasks:
- produce clean release inventories
- preserve comparison reports and forensic evidence where needed
- standardize pack/unpack validation
- maintain compile/test/demo validation summary after major changes

Deliverables:
- release checklist
- validation scripts and summaries
- updated release note

Exit condition:
- canonical release can be rebuilt, validated, and audited without ambiguity

## Recommended execution order
1. P0 — canonical integrity and hygiene
2. P1 — memory/storage boundary formalization
3. P2 — storage ports and interface extraction
4. P3 — graph truth layer and nonlocal topology
5. P4 — command quantization and admissibility rules
6. P5 — braid/knot closure layer
7. P6 — observability, traces, and replay
8. P7 — optional native kernels and backend acceleration
9. P8 — inference/runtime integration hardening
10. P9 — documentation, glossary, LaTeX, and cross-reference completion
11. P10 — packaging, release validation, and regression control

## Immediate next actions
- create root-level global governance file for the repo
- pin this plan in README and manifests
- begin with P0/P1/P2 before adding new mathematical structure
- update topology/manifests whenever structure changes

## Promotion rule for postponed ideas
A postponed idea from `TODO/` or research sectors may be promoted into canonical runtime only if all conditions hold:
- explicit problem statement
- explicit target sector
- manifest/documentation impact identified
- validation path defined
- no hidden contradiction with current canonical runtime

## Active priority statement
Until superseded by an explicit newer canonical plan, this document is the active repository-wide priority.


## P0 closeout status

P0 is complete. The canonical runtime is executable, volatile residue policy is explicit, manifest scope is synchronized, and the divergent packaged data-layer artifacts have been formally handed forward to P1 for structural resolution.
