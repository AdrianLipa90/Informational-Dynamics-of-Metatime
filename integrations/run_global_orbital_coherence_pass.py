from __future__ import annotations
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / "systems" / "CIEL_OMEGA_COMPLETE_SYSTEM"
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))

from ciel_omega.orbital.global_pass import run_global_pass  # type: ignore

if __name__ == "__main__":
    result = run_global_pass()
    print(json.dumps(result["final"], indent=2))
