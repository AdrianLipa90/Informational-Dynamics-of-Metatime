
# -*- coding: utf-8 -*-
"""
CIEL-Hutter Method v1 — deterministic context features
Returns a soft gating scalar gamma in [0,1] and a small set of binary flags.
No time/uuid/rng. Pure function of the input window.
"""

import re
from typing import Dict, Any

URL_RE = re.compile(r'https?://|www\.', re.IGNORECASE)
TPL_RE = re.compile(r'\{\{[^{}]{0,256}\}\}')
LINK_RE = re.compile(r'\[\[[^\[\]]{0,256}\]\]')
TAG_RE = re.compile(r'</?[A-Za-z0-9:_-]{1,32}[^>]{0,256}?>')
HEAD_RE = re.compile(r'^\s*={2,6}[^=].{0,200}?={2,6}\s*$', re.MULTILINE)
NUM_RE = re.compile(r'(?<![A-Za-z0-9])\d{2,}(?![A-Za-z0-9])')
DATE_RE = re.compile(r'\b(19|20)\d{2}[-/](0?[1-9]|1[0-2])[-/](0?[1-9]|[12]\d|3[01])\b')

def _clip01(x: float) -> float:
    return 0.0 if x < 0.0 else (1.0 if x > 1.0 else float(x))

def _sigmoid(x: float) -> float:
    # numerically stable for moderate ranges; sufficient here
    return 1.0/(1.0+pow(2.718281828, -x))

def analyze_window(text_window: str) -> Dict[str, Any]:
    """
    Deterministic features from a text window (e.g., last 2-8 KB of context).
    Returns:
      {
        "gamma": float in [0,1],
        "flags": {
          "is_url": 0/1,
          "is_template": 0/1,
          "is_link": 0/1,
          "is_heading": 0/1,
          "is_tag": 0/1,
          "is_numbery": 0/1,
          "is_datey": 0/1,
        }
      }
    """
    s = text_window
    # counts/booleans
    c_url = 1 if URL_RE.search(s) else 0
    c_tpl = 1 if TPL_RE.search(s) else 0
    c_lnk = 1 if LINK_RE.search(s) else 0
    c_tag = 1 if TAG_RE.search(s) else 0
    c_head = 1 if HEAD_RE.search(s) else 0
    c_num = 1 if NUM_RE.search(s) else 0
    c_dat = 1 if DATE_RE.search(s) else 0

    # crude character composition
    ascii_bytes = sum(1 for ch in s if ord(ch) < 128)
    ratio_ascii = ascii_bytes / max(1, len(s))
    ratio_digit = sum(ch.isdigit() for ch in s) / max(1, len(s))
    ratio_punct = sum(ch in ',.;:()[]{}<>=/_-+\'"@#&*%!' for ch in s) / max(1, len(s))

    # A light, deterministic score that maps "structured" → higher gamma
    # Weights tuned by hand for now (dev can later calibrate on enwik8)
    score = (
        1.4*c_url + 1.2*c_tpl + 1.0*c_lnk + 0.8*c_tag + 0.7*c_head
        + 0.9*ratio_digit + 0.4*ratio_punct - 0.3*(1.0 - ratio_ascii)
    )
    # compress score into [0,1] with a gentle sigmoid, center around 0.5
    gamma = _clip01(_sigmoid(1.0*score) * 0.9 + 0.05)

    flags = {
        "is_url": c_url, "is_template": c_tpl, "is_link": c_lnk,
        "is_heading": c_head, "is_tag": c_tag,
        "is_numbery": 1 if ratio_digit > 0.08 or c_num else 0,
        "is_datey": c_dat,
    }
    return {"gamma": gamma, "flags": flags}
