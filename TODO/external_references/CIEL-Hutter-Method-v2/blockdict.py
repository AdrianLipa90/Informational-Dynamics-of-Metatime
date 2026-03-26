
# -*- coding: utf-8 -*-
"""
Block dictionary estimator (demo). Deterministic, rolling-hash substrings.
Finds frequent substrings of length 4..12 and estimates net savings
when replaced by dictionary codes. Outputs a header (JSON) as a demo.
This is *not* used by the demo pipeline yet; it's a planning tool.
"""

from typing import Dict, List, Tuple
from collections import defaultdict, Counter

def rolling_chunks(data: bytes, k: int) -> List[bytes]:
    out = []
    for i in range(0, len(data)-k+1):
        out.append(data[i:i+k])
    return out

def top_substrings(data: bytes, k: int, topk: int = 256) -> List[Tuple[bytes, int]]:
    cnt = Counter(rolling_chunks(data, k))
    # filter trivial whitespace-only and extremely low counts
    items = [(s, c) for s, c in cnt.items() if c > 3 and any(b > 32 for b in s)]
    # deterministic tie-break: sort by (-count, bytes)
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:topk]

def estimate_savings(data: bytes, entries: List[Tuple[bytes,int]], code_bits: int) -> int:
    savings = 0
    for s, c in entries:
        raw_bits = len(s)*8*c
        coded_bits = (code_bits)*c
        # naive: assume no escape cost (final scheme will include it)
        savings += raw_bits - coded_bits
    return savings

def build_block_header(data: bytes, max_entries: int = 512) -> Dict:
    # Try k from 12 down to 4 to prefer longer substrings first
    selected = []
    used = set()
    for k in range(12, 3, -1):
        tops = top_substrings(data, k, topk=256)
        for s, c in tops:
            if s in used:
                continue
            selected.append((s, c))
            used.add(s)
            if len(selected) >= max_entries:
                break
        if len(selected) >= max_entries:
            break
    # Assume we encode with fixed code width = ceil(log2(n))
    n = max(1, len(selected))
    import math, base64
    code_bits = max(1, math.ceil(math.log2(n)))
    est = estimate_savings(data, selected, code_bits)

    # header demo: base64 substrings for JSON-friendliness
    hdr = {
        "n_entries": n,
        "code_bits": code_bits,
        "entries": [ { "b64": __import__("base64").b64encode(s).decode("ascii"), "cnt": c }
                     for s, c in selected ]
    }
    hdr["est_savings_bits"] = est
    return hdr
