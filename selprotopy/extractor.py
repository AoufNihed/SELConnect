
"""
Mapping-driven extractor:
- mapping JSON defines fields to extract, with either:
  - "regex": a regex with a capturing group
  - "kv_key": a key to read from the simple key/value dictionary
  - optional "post": post-processing pipeline ["strip_units", "to_float", ...]
"""
from __future__ import annotations
from typing import Dict, Any, List
from .rdb_parser import split_lines, detect_simple_kv, regex_find

def apply_post(value: str, steps: List[str]) -> Any:
    v: Any = value
    for step in steps or []:
        s = step.lower()
        if s == "strip_units":
            # remove common units and extra spaces
            v = (
                v.replace("A","")
                 .replace("V","")
                 .replace("s","")
                 .replace("Hz","")
            )
            v = v.replace("  "," ").strip()
        elif s == "to_float":
            try:
                v = float(str(v).strip())
            except ValueError:
                pass
        elif s == "to_int":
            try:
                v = int(float(str(v).strip()))
            except ValueError:
                pass
        elif s == "upper":
            v = str(v).upper()
        elif s == "lower":
            v = str(v).lower()
        elif s == "strip":
            v = str(v).strip()
        # add more transforms if needed
    return v

def extract_fields(rdb_text: str, mapping: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    lines = split_lines(rdb_text)
    kv = detect_simple_kv(lines)
    out: Dict[str, Any] = {}
    for field, rule in mapping.items():
        val = None
        if "kv_key" in rule:
            key = rule["kv_key"]
            val = kv.get(key)
        if val is None and "regex" in rule:
            val = regex_find(rdb_text, rule["regex"], rule.get("group", 1))
        if val is None:
            out[field] = None
            continue
        out[field] = apply_post(val, rule.get("post", []))
    return out
