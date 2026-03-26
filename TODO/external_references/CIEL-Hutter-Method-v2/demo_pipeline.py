
# -*- coding: utf-8 -*-
"""
Demo pipeline: compute bits/byte on a text file using
  - RST tokenization (for roundtrip check)
  - CIEL features (gamma & flags) on sliding windows
  - 3 n-gram models (order 0,1,2)
  - gated mixture trained online
This is NOT a full compressor. It's a method probe to validate the idea.
Usage:
  python3 demo_pipeline.py path/to/some_text.txt
"""

import sys, math
from pathlib import Path
from typing import List
from cielfeat import analyze_window
from rst_fsm import roundtrip_text
from ngram import NGramByteLM
from numerics import NumericsModel
from mixer import GatedMixture

def bits_per_byte(logloss: float, nbytes: int) -> float:
    return (logloss / max(1, nbytes)) / math.log(2.0)

def run_file(p: Path):
    data = p.read_bytes()
    # Sanity: RST roundtrip on a small prefix of UTF-8 text decode (for illustration)
    try:
        txt_sample = data[:20000].decode('utf-8', 'ignore')
        assert roundtrip_text(txt_sample) == txt_sample
    except AssertionError:
        print("RST roundtrip failed on sample — check tokenizer assumptions.")
    except Exception:
        pass

    # init models and mixture
    ms = [NGramByteLM(0, 0.5), NGramByteLM(1, 0.5), NGramByteLM(2, 0.5), NumericsModel()]
    mix = GatedMixture(K=len(ms), F=8, lr=0.03, l2=1e-6)

    hist = b''
    win = 4096
    logloss = 0.0

    for i, b in enumerate(data):
        # build feature vector from last window decoded as UTF-8 (ignore errors)
        ws = data[max(0, i-win):i].decode('utf-8', 'ignore')
        feats = []
        feat = analyze_window(ws)
        gamma = float(feat['gamma'])
        flags = feat['flags']
        feats.append(gamma)
        feats.extend([float(flags[k]) for k in ("is_url","is_template","is_link","is_heading","is_tag","is_numbery","is_datey")])

        # model predictions
        probs = [m.predict(hist) for m in ms]
        P, g = mix.mix(probs, feats)

        pb = max(P[b], 1e-12)
        logloss += -math.log(pb)

        # online updates
        mix.update(probs, feats, b)
        for m in ms:
            m.update(hist, b)

        # extend history
        hist = (hist + bytes([b]))[-2:]  # keep small for demo

        if (i+1) % 100000 == 0:
            print(f"{i+1} bytes processed... current bpb={bits_per_byte(logloss, i+1):.4f}")

    bpb = bits_per_byte(logloss, len(data))
    print(f"File: {p.name}  size={len(data)} bytes  -> estimated bpb={bpb:.4f}")
    return bpb

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    path = Path(sys.argv[1])
    if not path.exists():
        print("File not found:", path)
        sys.exit(1)
    run_file(path)
