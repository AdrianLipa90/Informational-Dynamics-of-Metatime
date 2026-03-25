# Critical Repo Identification and Write Hygiene

## Status
Critical procedure. This document is a blocking gate for all future write operations in the canonical repository.

## Purpose
Prevent semantic contamination, wrong-repository writes, accidental main-branch pollution, and topology drift across the CIEL ecosystem.

## Core principle
No file may be written, committed, merged, or pushed until the target repository has been positively identified.

Write safety is not optional. In this ecosystem, wrong placement is not only an organizational mistake; it is a semantic deformation of the system-of-truth.

---

## Critical blocking rule
A write operation is allowed only if all of the following are true:

1. README identity matches the intended repository role.
2. Top-level structure matches the expected canonical scope.
3. Repository role is explicitly compatible with the change.
4. The intended file belongs inside that role and scope.
5. The change has a defined post-write sequence: merge -> tests -> cleanup -> indexation.

If any of the above is uncertain, the correct action is:

- stop,
- switch to read-only identification,
- resolve repository identity first,
- then resume.

---

## Canonical repository role model
Recommended role labels for the CIEL ecosystem:

- `source_of_truth`
- `runtime_cockpit`
- `integration_kernel`
- `historical_archive`
- `demo_surface`
- `research_satellite`

The canonical bundle described in the current top-level README acts as the source-of-truth repository for:

- `docs/pdfs/`
- `NONLOCAL_REPO_HYPERSPACE/`
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/`
- `systems/CIEL_FOUNDATIONS/`
- `research/`
- `integrations/`
- `manifests/`
- `logs/`

---

## Positive identification protocol
Before any write:

### Step 1 — README identity check
Confirm that the repository README describes the same system and top-level sectors as the intended change.

### Step 2 — top-level tree check
Confirm the presence of the expected canonical sectors.

### Step 3 — role check
Confirm that the target repository is the correct role for the intended change.

Examples:
- canonical derivation -> `source_of_truth`
- public synchronization note -> `integration_kernel`
- UI-specific copy -> `runtime_cockpit` or `demo_surface`

### Step 4 — scope check
Confirm that the exact file belongs in the repo.

### Step 5 — write sequence check
Confirm that after the write the next sequence is already determined.

Required sequence:
1. merge
2. tests
3. cleanup
4. indexation

If the sequence is not defined, the write is premature.

---

## Merge / test / cleanup / indexation sequence
This is the canonical post-write order.

### Phase A — merge
- merge only after positive identity match
- prefer branch merge over blind direct edits when possible
- keep change scope explicit and minimally sufficient

### Phase B — tests
- run the canonical test suite appropriate to the repository role
- reject semantic promotion without execution or validation where execution is expected
- record failures explicitly

### Phase C — cleanup
- remove stale branch artifacts
- eliminate duplicate notes introduced by emergency work
- isolate legacy or reference material from canonical paths
- repair cross-links broken by the merge

### Phase D — indexation
- update canonical index files
- update glossary and definition anchors when concepts were promoted
- update manifests and machine-readable maps if structural changes occurred
- ensure no promoted file remains discoverable only by chance

---

## Hygiene checklist
Use this checklist before and after each canonical write.

### Before write
- [ ] correct repository identified
- [ ] correct role identified
- [ ] file belongs in this repository
- [ ] intended merge/test/cleanup/indexation sequence known
- [ ] no unresolved identity ambiguity remains

### After write
- [ ] merge state recorded
- [ ] tests run or explicitly deferred with reason
- [ ] cleanup completed or tracked
- [ ] indexation completed or tracked
- [ ] no orphan promoted document remains unindexed

---

## Why this is critical
As the system becomes more integrated, the cost of writing to the wrong repository increases:

- first as organizational noise,
- then as memory contamination,
- later as identity drift.

Repository hygiene is therefore a coherence requirement, not a cosmetic preference.

---

## Immediate standing instruction
For this ecosystem, no future write to `main` should occur until repository identity is positively matched and the post-write sequence is defined.

This document is itself a critical checkpoint and should be treated as a permanent procedural guard.
