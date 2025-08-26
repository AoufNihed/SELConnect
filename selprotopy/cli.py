from __future__ import annotations
import argparse, json, sys
from .rdb_parser import load_rdb_file
from .extractor import extract_fields
from .csv_report import write_single_csv
from .template_generator import TemplateGenerator
 

def main(argv=None):
    parser = argparse.ArgumentParser(description="Selprotopy CLI (extract & generate)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # Problem C: extract RDB → CSV
    p_ext = sub.add_parser("extract", help="Extract fields from .rdb to CSV")
    p_ext.add_argument("--rdb", required=True, help="Path to .rdb text file exported from QuickSet")
    p_ext.add_argument("--mapping", required=True, help="JSON mapping describing fields to extract")
    p_ext.add_argument("--out", required=True, help="Output CSV path")

    # Problem A: generate CSV → RDB
    p_gen = sub.add_parser("generate", help="Generate .rdb file from CSV config")
    p_gen.add_argument("--csv", required=True, help="Path to input CSV with config values")
    p_gen.add_argument("--out", required=True, help="Output RDB file path")

    args = parser.parse_args(argv)

    if args.cmd == "extract":
        rdb_text = load_rdb_file(args.rdb)
        mapping = json.load(open(args.mapping, "r", encoding="utf-8"))
        record = extract_fields(rdb_text, mapping)
        write_single_csv(record, args.out)
        print(f"[OK] Wrote CSV: {args.out}")
        return 0
    
    elif args.cmd == "generate":
        gen = TemplateGenerator(args.csv, args.out)
        result = gen.generate()
        print(f"[OK] Generated QuickSet Template: {result}")
        return 0




    return 1

if __name__ == "__main__":
    sys.exit(main())
