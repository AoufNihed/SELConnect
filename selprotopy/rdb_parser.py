
"""
Lightweight parser for QuickSet .rdb-like text files.
We treat the file as *unstructured text* and offer helpers to:
- normalize lines
- extract key/value pairs when possible
- run regex searches for complex patterns
"""
from __future__ import annotations
import re
from typing import Dict, List, Tuple, Optional

LINE_KV = re.compile(r"^\s*([A-Za-z0-9_.:/-]+)\s*[:=]\s*(.+?)\s*$")

def normalize_text(text: str) -> str:
    # Unify newlines, strip trailing spaces
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]
    return "\n".join(lines)

def split_lines(text: str) -> List[str]:
    return normalize_text(text).split("\n")

def detect_simple_kv(lines: List[str]) -> Dict[str,str]:
    """
    Attempt to read simple KEY=VALUE or KEY: VALUE lines as a dict.
    Many .rdb exports contain mixed sections; this is best-effort.
    """
    out = {}
    for ln in lines:
        m = LINE_KV.match(ln)
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            out[key] = val
    return out

def regex_find(text: str, pattern: str, group: int = 1) -> Optional[str]:
    """
    Return first capturing group match or None.
    """
    m = re.search(pattern, text, flags=re.IGNORECASE|re.MULTILINE)
    if not m:
        return None
    try:
        return m.group(group).strip()
    except IndexError:
        return None

def load_rdb_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
