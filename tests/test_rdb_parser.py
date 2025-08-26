
from selprotopy.rdb_parser import split_lines, detect_simple_kv, load_rdb_file

def test_detect_simple_kv():
    text = load_rdb_file("samples/sample_710.rdb")
    kv = detect_simple_kv(split_lines(text))
    assert kv["CT_PRIMARY"].startswith("300")
    assert kv["COMM.PORT1.BAUD"] == "19200"
