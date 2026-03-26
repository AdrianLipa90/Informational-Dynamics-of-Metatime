# Verification

This layer runs in parallel to the main derivation tree.

It contains three synchronized tracks:

1. `canon_extraction/`
   - extracts what is already present in existing derivations, notes, and source material
   - produces canonical statements, dependency links, and registry entries

2. `raw_rederivation/`
   - re-derives the same object from the frozen axioms and minimal starting assumptions
   - ignores previous polished formulations whenever possible
   - serves as an independent control path

3. `reconciliation/`
   - compares canon and raw paths
   - classifies mismatches
   - identifies hidden assumptions, fit leaks, derivation gaps, and implementation bugs

Rule:
No major object is considered fully closed until it has passed reconciliation.
