#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"[error] failed to import yaml: {exc}")
    raise

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "manifests" / "index_registry.yaml"
DECISIONS = ROOT / "manifests" / "duplicate_decisions.yaml"

ALLOWED_DECISIONS = {
    "keep_canonical_root",
    "keep_nested_only",
    "merge_then_prune",
    "needs_manual_review",
    "reference_copy_only",
}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    registry = load_yaml(REGISTRY)
    decisions = load_yaml(DECISIONS)

    objects = {str(obj.get("id")): obj for obj in (registry.get("objects", []) or [])}
    records = decisions.get("records", []) or []

    errors: list[str] = []
    warnings: list[str] = []

    for rec in records:
        rid = str(rec.get("id", "")).strip()
        decision = str(rec.get("decision", "")).strip()
        canonical_path = str(rec.get("canonical_candidate_path", "")).strip()
        duplicate_path = str(rec.get("duplicate_candidate_path", "")).strip()

        if rid not in objects:
            errors.append(f"{rid}: decision record not found in index_registry")
            continue

        obj = objects[rid]
        if str(obj.get("status", "")).strip() != "duplicate_candidate":
            errors.append(f"{rid}: registry object is not marked duplicate_candidate")
        if str(obj.get("path", "")).strip() != duplicate_path:
            errors.append(f"{rid}: duplicate path mismatch between registry and duplicate_decisions")
        if decision not in ALLOWED_DECISIONS:
            errors.append(f"{rid}: invalid decision '{decision}'")
        if not canonical_path:
            errors.append(f"{rid}: missing canonical_candidate_path")
        if not duplicate_path:
            errors.append(f"{rid}: missing duplicate_candidate_path")
        if decision == "keep_canonical_root" and not canonical_path.startswith(("reports/", "comparison_reports/", "comparison_reports_forensic/", "README.md")):
            warnings.append(f"{rid}: keep_canonical_root applied to a non-obvious root canonical path")

    for oid, obj in objects.items():
        if str(obj.get("status", "")).strip() == "duplicate_candidate":
            if oid not in {str(r.get("id", "")).strip() for r in records}:
                warnings.append(f"{oid}: duplicate_candidate in registry has no decision record")

    for item in errors:
        print(f"[error] {item}")
    for item in warnings:
        print(f"[warning] {item}")

    if not errors:
        print("[ok] duplicate decision validation passed without errors")
        if warnings:
            print(f"[ok] warnings: {len(warnings)}")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
