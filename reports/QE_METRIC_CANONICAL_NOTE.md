# QE_METRIC_CANONICAL_NOTE

Canonical note for layered quality/energy reporting.

Use:
- `docs/concepts/HARDWARE_AND_QE_METRIC.md` for definitions
- `manifests/orbital/qe_metric_schema.json` for schema

Rule:
- do not double-count `Theta` and `H` if `Theta` is already defined from `H`.
- report quality and energy per execution layer.
