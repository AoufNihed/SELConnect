import csv
from pathlib import Path
import xml.etree.ElementTree as ET

# ---------- Helpers for SCL simple generation ----------
def make_scl_tree(relay_info):
    ns = {"scl": "http://www.iec.ch/61850/2003/SCL"}
    ET.register_namespace("", ns["scl"])

    SCL = ET.Element("{http://www.iec.ch/61850/2003/SCL}SCL", version="2007", revision="B")
    header = ET.SubElement(SCL, "Header", id=f"{relay_info['relay_id']}_header")
    ET.SubElement(header, "Revision").text = "1"

    ied = ET.SubElement(SCL, "IED", name=relay_info.get("relay_id"))
    manufacturer = ET.SubElement(ied, "Manufacturer")
    manufacturer.text = relay_info.get("device_model", "")

    ld = ET.SubElement(ied, "AccessPoint", name="AP1")
    ld2 = ET.SubElement(ld, "Server")
    ldevice = ET.SubElement(ld2, "LDevice", inst=relay_info.get("ln_name","LD1"))

    ln = ET.SubElement(ldevice, "LN", lnClass="PTOC", inst="1", lnType="PTOC")
    do1 = ET.SubElement(ln, "DO", name="Opn")
    ET.SubElement(do1, "DA", name="stVal").text = str(relay_info.get("oc_50p1t_pickup_A",""))

    return ET.ElementTree(SCL)

# ---------- TXT generator ----------
def generate_template_txt(row, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("; SEL QuickSet Import Template - generated\n")
        f.write(f"; Relay ID: {row['relay_id']}\n\n")
        f.write("[Device]\n")
        f.write(f"Model={row.get('device_model','')}\n")
        f.write(f"Serial={row.get('serial','')}\n\n")
        f.write("[CT/PT]\n")
        f.write(f"CT Primary={row.get('ct_primary_A','')}\n")
        f.write(f"CT Secondary={row.get('ct_secondary_A','')}\n")
        f.write(f"PT Primary={row.get('pt_primary_V','')}\n")
        f.write(f"PT Secondary={row.get('pt_secondary_V','')}\n\n")
        f.write("[Protection]\n")
        f.write(f"50P1T Pickup={row.get('oc_50p1t_pickup_A','')}\n")
        f.write(f"51P1T Time={row.get('oc_51p1t_time_s','')}\n\n")
        f.write("[Comm]\n")
        f.write(f"Baud={row.get('comm_baud','')}\n")
        f.write(f"Protocol={row.get('comm_protocol','')}\n")

# ---------- Main multi generator ----------
def generate_multi_from_master(csv_path, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        relay_id = row.get("relay_id")
        folder = out_dir / relay_id
        folder.mkdir(parents=True, exist_ok=True)

        # 1) TXT Template
        txt_path = folder / f"{relay_id}_template.txt"
        generate_template_txt(row, txt_path)

        # 2) SCL generation (simple)
        scl_tree = make_scl_tree(row)
        scl_path = folder / f"{relay_id}.scl.xml"
        scl_tree.write(scl_path, encoding="utf-8", xml_declaration=True)

        print(f"[OK] Generated for {relay_id}: {txt_path.name}, {scl_path.name}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Generate TXT templates and simple SCL per relay from master CSV")
    ap.add_argument("--csv", default="samples/Master.csv", help="Master CSV file path (default: samples/Master.csv)")
    ap.add_argument("--out", required=True, help="Output directory")
    args = ap.parse_args()
    generate_multi_from_master(args.csv, args.out)
