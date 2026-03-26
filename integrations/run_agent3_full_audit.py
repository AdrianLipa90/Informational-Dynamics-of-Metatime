#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path) -> int:
    print(f"\n=== RUNNING: {' '.join(cmd)} (cwd={cwd}) ===")
    return subprocess.run(cmd, cwd=str(cwd), check=False).returncode


def main() -> int:
    tasks = [
        ([sys.executable, 'integrations/validate_index_registry.py'], ROOT),
        ([sys.executable, 'integrations/validate_duplicate_decisions.py'], ROOT),
    ]
    rc = 0
    for cmd, cwd in tasks:
        code = run(cmd, cwd)
        rc = rc or code
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
