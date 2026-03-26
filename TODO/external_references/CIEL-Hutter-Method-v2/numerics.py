
# -*- coding: utf-8 -*-
"""
Deterministic numeric/date aware byte model.
Boosts probability mass on '0'..'9' and separators when in numeric runs,
and uses light heuristics for dates (YYYY-MM-DD / YYYY/MM/DD).
No randomness, pure online counts.
"""

from typing import List
from collections import defaultdict

DIGITS = [ord(c) for c in "0123456789"]
SEPS   = [ord(c) for c in "-/:,. "]
YEAR_PREFIX = [b"19", b"20"]

class NumericsModel:
    def __init__(self, alpha: float = 0.01):
        self.alpha = float(alpha)
        # counts for digit transitions and separator frequencies
        self.count_digit = defaultdict(int)   # digit -> count
        self.count_pair  = defaultdict(int)   # (prev_digit, digit) -> count
        self.count_sep   = defaultdict(int)   # sep -> count
        self.total_digit = 0
        self.total_sep   = 0

    def _tail_digits(self, hist: bytes, k: int = 6) -> bytes:
        i = len(hist)
        j = i
        while j > 0 and hist[j-1] in DIGITS and (i - j) < k:
            j -= 1
        return hist[j:i]

    def _is_datey(self, hist: bytes) -> bool:
        # detect patterns like b'YYYY-' or 'YYYY/' at the tail
        tail = hist[-10:]
        for pref in YEAR_PREFIX:
            pos = tail.rfind(pref)
            if pos != -1 and len(tail) - pos >= 5:
                # example: '20' + '23-'  (at least 5 bytes: '2','0','3','4','-')
                y4 = tail[pos:pos+4] if len(tail) >= pos+4 else b''
                if len(y4) == 4 and all(c in DIGITS for c in y4):
                    if len(tail) > pos+4 and tail[pos+4] in (ord('-'), ord('/')):
                        return True
        return False

    def predict(self, hist: bytes) -> List[float]:
        # base distribution (uniform with small smoothing)
        P = [1.0/256.0]*256

        # if we're in a digit run, push mass to digits (and to separators as potential end)
        tail = self._tail_digits(hist)
        if tail:
            # digit continuation
            denom = self.total_digit + 10*self.alpha
            for d in DIGITS:
                cnt = self.count_pair[(tail[-1], d)] if len(tail) >= 1 else self.count_digit[d]
                P[d] += (cnt + self.alpha) / max(1.0, denom)

            # likely separators after a short run
            sden = self.total_sep + len(SEPS)*self.alpha
            for s in SEPS:
                P[s] += 0.25 * (self.count_sep[s] + self.alpha) / max(1.0, sden)

        # if it's date-like context, prefer digits and '-' or '/'
        if self._is_datey(hist):
            for d in DIGITS:
                P[d] += 0.02
            for s in (ord('-'), ord('/')):
                P[s] += 0.03

        # normalize
        s = sum(P)
        P = [p/s for p in P]
        return P

    def update(self, hist: bytes, byte_val: int):
        if byte_val in DIGITS:
            self.count_digit[byte_val] += 1
            self.total_digit += 1
            if hist and hist[-1] in DIGITS:
                self.count_pair[(hist[-1], byte_val)] += 1
        elif byte_val in SEPS:
            self.count_sep[byte_val] += 1
            self.total_sep += 1
