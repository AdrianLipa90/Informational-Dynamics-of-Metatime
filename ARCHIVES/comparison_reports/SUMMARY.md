# Canon compare report

## Cleanliness
- removed cache/build junk entries: **53**
- original canonical zip contained `__pycache__` / `.pyc`: **yes**

## Inventories
- old aggregate files indexed: **739**
- cleaned canon files indexed: **582**

## Package-level missing from canon (copied into TODO)
- count: **0 meaningful code/doc files**
  - only `.pytest_cache` residue appeared missing; it was intentionally not kept

## Same-path text replacements or fuller candidates
- count: **0**

## Loose files not present in canon by basename (copied into TODO/loose_from_old)
  - `Analiza teoretyczna i implementacyjna systemu Informational Dynamics of Metatime z wykorzystaniem relacyjnej dynamiki fazowej.pdf`
  - `Contract _prompt.txt`
  - `Derivation of tau_i.pdf`
  - `G f.pdf`
  - `HOW_TO_RUN.md`
  - `Topological Phase Dynamics.pdf`
  - `generate_import_dependency_graph.py`
  - `relational_contract.py`
  - `relational_contract.yaml.txt`

## Important notes
- Automatic replacement was done only for text files at the same relative path inside matched package roots.
- Generic duplicate names like `__init__.py` were not auto-merged across unrelated folders.
- Full inventories with file size and character counts are in TSV reports.

Archived from source path: `comparison_reports/SUMMARY.md`
