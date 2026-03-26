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

ALLOWED_STATUS = {
    "canonical",
    "reference",
    "imported",
    "duplicate_candidate",
    "placeholder",
    "deprecated",
}

ALLOWED_LAYERS = {
    "root_navigation",
    "procedure",
    "topology",
    "formal_source_of_truth",
    "runtime_source_of_truth",
    "integration_runner",
    "report",
    "duplicate_candidate",
    "registry",
    "audit",
}


def load_registry(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate() -> int:
    data = load_registry(REGISTRY)
    objects = data.get("objects", []) or []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    errors: list[str] = []
    warnings: list[str] = []

    for obj in objects:
        oid = str(obj.get("id", "")).strip()
        name = str(obj.get("name", "")).strip()
        layer = str(obj.get("layer", "")).strip()
        status = str(obj.get("status", "")).strip()
        path = str(obj.get("path", "")).strip()
        upstream = obj.get("upstream", []) or []
        placeholder = bool(obj.get("placeholder", False))

        if not oid:
            errors.append("object missing id")
            continue
        if oid in seen_ids:
            errors.append(f"{oid}: duplicate id")
        seen_ids.add(oid)

        if not name:
            errors.append(f"{oid}: missing name")
        if layer not in ALLOWED_LAYERS:
            warnings.append(f"{oid}: nonstandard layer '{layer}'")
        if status not in ALLOWED_STATUS:
            errors.append(f"{oid}: invalid status '{status}'")
        if not path:
            errors.append(f"{oid}: missing path")
        else:
            if path in seen_paths:
                warnings.append(f"{oid}: duplicate path entry '{path}'")
            seen_paths.add(path)
            if not (ROOT / path).exists():
                errors.append(f"{oid}: path does not exist -> {path}")

        if status == "duplicate_candidate" and not path.startswith("omega/"):
            warnings.append(f"{oid}: duplicate_candidate not under omega/ mirror path")
        if placeholder and status != "placeholder":
            warnings.append(f"{oid}: placeholder flag true but status is '{status}'")
        if status == "placeholder" and not placeholder:
            errors.append(f"{oid}: status placeholder but placeholder flag false")

        if layer not in {"root_navigation", "procedure", "topology", "audit"} and not upstream:
            warnings.append(f"{oid}: missing upstream links")

        if layer == "integration_runner":
            if not any(str(u).startswith(("DOC-", "RPT-")) for u in upstream):
                errors.append(f"{oid}: integration runner has no documentary/report upstream")

    for item in errors:
        print(f"[error] {item}")
    for item in warnings:
        print(f"[warning] {item}")

    if not errors:
        print("[ok] index registry validation passed without errors")
        if warnings:
            print(f"[ok] warnings: {len(warnings)}")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(validate())
