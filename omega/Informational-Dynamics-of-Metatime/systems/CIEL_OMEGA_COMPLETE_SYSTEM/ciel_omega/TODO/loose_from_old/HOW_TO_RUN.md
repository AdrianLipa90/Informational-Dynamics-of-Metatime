# HOW_TO_RUN

Example for the canonical runtime tree:

```bash
python generate_import_dependency_graph.py systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega manifests/
```

This writes:
- `manifests/import_dependency_graph.json`
- `manifests/import_dependency_graph.md`

Recommended pairing:
- keep this raw import graph next to `EXPLICIT_DEPENDENCIES.yaml`
- treat the raw graph as syntactic truth
- treat `EXPLICIT_DEPENDENCIES.yaml` as architectural truth

Suggested naming in your repo:
- `manifests/RAW_IMPORT_DEPENDENCY_GRAPH.json`
- `manifests/RAW_IMPORT_DEPENDENCY_GRAPH.md`

If you want that naming directly, rename the outputs after generation.
