
import os, csv, json, tempfile
from selprotopy.rdb_parser import load_rdb_file
from selprotopy.extractor import extract_fields
from selprotopy.csv_report import write_single_csv

def test_write_single_csv(tmp_path):
    text = load_rdb_file("samples/sample_710.rdb")
    mapping = json.load(open("samples/mapping_710.json","r"))
    record = extract_fields(text, mapping)
    out = tmp_path / "out.csv"
    write_single_csv(record, str(out))
    assert out.exists()
    rows = list(csv.DictReader(open(out, "r", encoding="utf-8")))
    assert len(rows) == 1
    assert rows[0]["device"] == "SEL-710-5"
