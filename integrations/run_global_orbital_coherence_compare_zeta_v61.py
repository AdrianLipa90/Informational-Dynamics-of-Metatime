from __future__ import annotations
import json, sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / "systems" / "CIEL_OMEGA_COMPLETE_SYSTEM"
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))
from ciel_omega.orbital.global_pass import run_global_pass

if __name__ == "__main__":
    no_zeta = run_global_pass(params={"use_zeta_pole": False})
    zeta_v6 = run_global_pass(params={"use_zeta_pole": True, "zeta_heisenberg_alpha": 0.0, "zeta_i0_scale": 1e9})
    zeta_v61 = run_global_pass(params={"use_zeta_pole": True, "zeta_heisenberg_alpha": 8.0, "zeta_i0_scale": 1.0})
    out = {
        "no_zeta_final": no_zeta["final"],
        "zeta_v6_emulated_final": zeta_v6["final"],
        "zeta_v61_final": zeta_v61["final"],
    }
    out_dir = REPO_ROOT / "reports" / "global_orbital_coherence_pass"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "zeta_compare_v61.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    md=[]
    md.append("# Zeta Compare v6 vs v6.1\n")
    for label,key in [("No zeta","no_zeta_final"),("Zeta v6 emulated","zeta_v6_emulated_final"),("Zeta v6.1","zeta_v61_final")]:
        md.append(f"## {label}")
        for k,v in out[key].items():
            if isinstance(v,bool):
                md.append(f"- {k}: {v}")
            else:
                md.append(f"- {k}: {v:.6f}")
        md.append("")
    (out_dir / "zeta_compare_v61.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(out, indent=2))
