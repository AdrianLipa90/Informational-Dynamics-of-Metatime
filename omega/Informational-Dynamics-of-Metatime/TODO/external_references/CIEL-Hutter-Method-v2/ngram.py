
# -*- coding: utf-8 -*-
"""
Lightweight byte-level n-gram language models (order 0..N).
Deterministic online updates; returns categorical distributions over 256 bytes.
"""

from typing import Dict, List
from collections import defaultdict

class NGramByteLM:
    def __init__(self, order: int, alpha: float = 0.5):
        assert 0 <= order <= 3, "Keep it small for demo"
        self.order = order
        self.alpha = float(alpha)
        self.counts: Dict[bytes, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
        self.totals: Dict[bytes, int] = defaultdict(int)

    def _ctx(self, hist: bytes) -> bytes:
        return hist[-self.order:] if self.order > 0 else b''

    def predict(self, hist: bytes) -> List[float]:
        """Return a 256-long list of probabilities for next byte."""
        ctx = self._ctx(hist)
        cdict = self.counts[ctx]
        total = self.totals[ctx]
        vocab = 256
        # Additive smoothing (alpha): P = (c + alpha) / (total + alpha*vocab)
        denom = total + self.alpha * vocab
        return [ (cdict.get(b, 0) + self.alpha) / denom for b in range(256) ]

    def update(self, hist: bytes, byte_val: int):
        ctx = self._ctx(hist)
        self.counts[ctx][byte_val] += 1
        self.totals[ctx] += 1
