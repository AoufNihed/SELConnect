
import json, os
from selprotopy.rdb_parser import load_rdb_file
from selprotopy.extractor import extract_fields

def test_extract_fields():
    text = load_rdb_file("samples/sample_710.rdb")
    mapping = json.load(open("samples/mapping_710.json","r"))
    record = extract_fields(text, mapping)
    assert record["device"] == "SEL-710-5"
    assert record["ct_primary_A"] == 300.0
    assert record["oc_51p1t_time_s"] == 0.40
    assert record["comm_port1_protocol"] == "SEL"
