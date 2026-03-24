from __future__ import annotations
import json, sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / 'systems' / 'CIEL_OMEGA_COMPLETE_SYSTEM'
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))
from ciel_omega.orbital.global_pass import run_global_pass

if __name__ == '__main__':
    no_zeta = run_global_pass(params={'use_zeta_pole': False})
    with_zeta = run_global_pass(params={'use_zeta_pole': True})
    out = {
        'no_zeta_final': no_zeta['final'],
        'with_zeta_final': with_zeta['final'],
    }
    out_dir = REPO_ROOT / 'reports' / 'global_orbital_coherence_pass'
    (out_dir / 'zeta_compare.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(out, indent=2))
