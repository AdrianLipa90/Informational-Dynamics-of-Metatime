
# -*- coding: utf-8 -*-
"""
CIEL-Hutter Method v1 — reversible structural transform (RST)
Tokenize MediaWiki/XML-like structures into a stream of tokens.
Provide encode(tokens)->bytes and decode(bytes)->tokens that are *exact* inverses.
For the demo we also include roundtrip(text) using JSON-safe bytes (not final format).
"""

import json, re
from typing import List, Tuple, Dict, Any

# Simple token kinds
K_TEXT = "TEXT"
K_TAG  = "TAG"      # <tag ...> or </tag>
K_LINK = "LINK"     # [[...]]
K_TPL  = "TPL"      # {{...}}
K_HEAD = "HEAD"     # == heading ==
K_URL  = "URL"
K_NUM  = "NUM"
K_DATE = "DATE"

URL_RE  = re.compile(r'(https?://[^\s<>{}\[\]]+|www\.[^\s<>{}\[\]]+)', re.IGNORECASE)
LINK_RE = re.compile(r'\[\[[^\[\]]+\]\]')
TPL_RE  = re.compile(r'\{\{[^{}]+\}\}')
TAG_RE  = re.compile(r'</?[A-Za-z0-9:_-]{1,32}[^>]*>')
HEAD_RE = re.compile(r'^\s*={2,6}[^=].*?={2,6}\s*$', re.MULTILINE)
DATE_RE = re.compile(r'\b(19|20)\d{2}[-/](0?[1-9]|1[0-2])[-/](0?[1-9]|[12]\d|3[01])\b')
NUM_RE  = re.compile(r'(?<![A-Za-z0-9])\d{2,}(?![A-Za-z0-9])')

def tokenize(text: str) -> List[Dict[str, Any]]:
    """
    Greedy, non-overlapping tokenization by priority:
      URL > TPL > LINK > TAG > HEAD > DATE > NUM > TEXT
    Produces a list of {"k": kind, "v": value} covering the entire string in order.
    """
    L = []
    i, n = 0, len(text)
    while i < n:
        m = None
        # priority order
        for kind, rx in ( (K_URL, URL_RE), (K_TPL, TPL_RE), (K_LINK, LINK_RE),
                          (K_TAG, TAG_RE), (K_HEAD, HEAD_RE), (K_DATE, DATE_RE),
                          (K_NUM, NUM_RE) ):
            m = rx.match(text, i) if kind not in (K_HEAD,) else rx.search(text, i)
            if m and m.start() == i:
                L.append({"k": kind, "v": m.group(0)})
                i = m.end()
                break
            elif kind == K_HEAD and m and m.start() == i:
                L.append({"k": kind, "v": m.group(0)})
                i = m.end()
                m = None
                break
            else:
                m = None
        if m is None:
            # consume a single character as TEXT (merge with previous if same kind)
            ch = text[i]
            if L and L[-1]["k"] == K_TEXT:
                L[-1]["v"] += ch
            else:
                L.append({"k": K_TEXT, "v": ch})
            i += 1
    return L

def encode_tokens(tokens: List[Dict[str, Any]]) -> bytes:
    """
    Demo encoder: JSON with minimal escaping, then UTF-8 bytes.
    This is *not* the final bitstream format, but is fully reversible and deterministic.
    """
    return json.dumps(tokens, ensure_ascii=False, separators=(',', ':')).encode('utf-8')

def decode_tokens(data: bytes) -> List[Dict[str, Any]]:
    return json.loads(data.decode('utf-8'))

def roundtrip_text(text: str) -> str:
    toks = tokenize(text)
    bys = encode_tokens(toks)
    toks2 = decode_tokens(bys)
    # Reconstruct text (concatenate values in order)
    rec = ''.join(t["v"] for t in toks2)
    assert rec == text, "Roundtrip failed"
    return rec
