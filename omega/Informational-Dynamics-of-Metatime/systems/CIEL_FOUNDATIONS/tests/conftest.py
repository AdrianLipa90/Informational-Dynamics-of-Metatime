from __future__ import annotations

import sys
from pathlib import Path

_TESTS_DIR = Path(__file__).resolve().parent
_FOUNDATIONS_ROOT = _TESTS_DIR.parent
_REPO_ROOT = _FOUNDATIONS_ROOT.parent.parent

for candidate in (_REPO_ROOT, _FOUNDATIONS_ROOT):
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)
