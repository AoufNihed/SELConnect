import os
from selprotopy.rdb_generator import RDBGenerator

def test_rdb_generation(tmp_path):
    input_csv = "samples/config_input.csv"
    output_rdb = tmp_path / "generated.rdb"

    gen = RDBGenerator(input_csv, output_rdb)
    result = gen.generate()

    assert os.path.exists(result)
    content = result.read_text()
    assert "DEVICE=SEL-710-5" in content
    assert "CT_PRIMARY=400" in content
    assert "COMM1_PROTOCOL=DNP3" in content
