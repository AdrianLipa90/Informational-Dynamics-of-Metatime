from __future__ import annotations
import json
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / "systems" / "CIEL_OMEGA_COMPLETE_SYSTEM"
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))
from ciel_omega.orbital.global_pass import run_global_pass

def main():
    baseline = run_global_pass(params={"use_relational_lagrangian": False})
    v62 = run_global_pass(params={"use_relational_lagrangian": True})
    out_dir = REPO_ROOT / "reports" / "global_orbital_coherence_pass"
    result = {"baseline_v61_style": baseline["final"], "v62_relational": v62["final"]}
    (out_dir / "v62_compare.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    lines=["# v6.2 Relational Lagrangian Comparison", "", "## Baseline (legacy dynamics)"]
    for k,v in baseline['final'].items():
        lines.append(f"- {k}: {v}" if isinstance(v,bool) else f"- {k}: {v:.6f}")
    lines += ["", "## v6.2"]
    for k,v in v62['final'].items():
        lines.append(f"- {k}: {v}" if isinstance(v,bool) else f"- {k}: {v:.6f}")
    (out_dir / "v62_compare.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
