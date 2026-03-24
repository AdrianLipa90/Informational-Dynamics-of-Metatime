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
    v62 = run_global_pass(params={"use_euler_leak_rotation": False})
    v63 = run_global_pass(params={"use_euler_leak_rotation": True, "D_f": 2.57})
    out_dir = REPO_ROOT / "reports" / "global_orbital_coherence_pass"
    result = {"v62_relational": v62["final"], "v63_euler_df257": v63["final"]}
    (out_dir / "v63_compare.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    lines=["# v6.3 Euler D_f=2.57 Comparison", "", "## v6.2 (no Euler leak rotation)"]
    for k,v in v62['final'].items():
        lines.append(f"- {k}: {v}" if isinstance(v,bool) else f"- {k}: {v:.6f}")
    lines += ["", "## v6.3 (Euler leak rotation, D_f=2.57)"]
    for k,v in v63['final'].items():
        lines.append(f"- {k}: {v}" if isinstance(v,bool) else f"- {k}: {v:.6f}")
    (out_dir / "v63_compare.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
