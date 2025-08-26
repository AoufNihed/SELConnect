
from __future__ import annotations
import csv
from typing import Dict, Any, List

def write_single_csv(record: Dict[str, Any], out_path: str) -> None:
    # Write a one-row CSV with stable column order
    cols = list(record.keys())
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerow(record)

def write_many_csv(records: List[Dict[str, Any]], out_path: str) -> None:
    # Determine superset of keys
    cols = []
    for r in records:
        for k in r.keys():
            if k not in cols:
                cols.append(k)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in records:
            w.writerow({k: r.get(k) for k in cols})
