from __future__ import annotations
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / "systems" / "CIEL_OMEGA_COMPLETE_SYSTEM"
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))

from ciel_omega.orbital.global_pass import run_global_pass  # type: ignore
from ciel_omega.orbital.phase_control import build_state_manifest, build_health_manifest, recommend_control  # type: ignore

def main() -> None:
    result = run_global_pass()
    final = result["final"]
    out = REPO_ROOT / "manifests" / "orbital"
    out.mkdir(parents=True, exist_ok=True)
    state = build_state_manifest(final)
    control = recommend_control(final)
    health = build_health_manifest(final)
    (out / "state.json").write_text(json.dumps(state, indent=2), encoding="utf-8")
    (out / "control.json").write_text(json.dumps(control, indent=2), encoding="utf-8")
    (out / "health.json").write_text(json.dumps(health, indent=2), encoding="utf-8")
    report_dir = REPO_ROOT / "reports" / "orbital_phase_control"
    report_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "global_pass_final": final,
        "state": state,
        "control": control,
        "health": health,
    }
    (report_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    md = []
    md.append("# Orbital Phase Control Pass")
    md.append("")
    md.append("Derived from HTRI-style phase control ideas at repository scale.")
    md.append("")
    md.append("## Final metrics")
    for k, v in final.items():
        if isinstance(v, (int, float)):
            md.append(f"- {k}: {v:.6f}")
    md.append("")
    md.append("## Control recommendation")
    for k, v in control.items():
        md.append(f"- {k}: {v}")
    md.append("")
    md.append("## Health")
    for k, v in health.items():
        md.append(f"- {k}: {v}")
    (report_dir / "summary.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
