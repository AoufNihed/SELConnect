from compoundfiles import CompoundFileReader

def print_rdb_structure(rdb_path):
    print(f"Opening file: {rdb_path}")
    with CompoundFileReader(rdb_path) as cf:
        print("File opened. Recursing into root storage...")
        def recurse(entry, indent=0):
            prefix = "  " * indent
            if hasattr(entry, '_entry_type'):
                if entry._entry_type == "storage":
                    print(f"{prefix}[Storage] {entry.name}")
                    for subentry in entry:
                        recurse(subentry, indent + 1)
                elif entry._entry_type == "stream":
                    value = entry.open().read()
                    try:
                        value_str = value.decode('utf-8').strip()
                    except Exception:
                        value_str = str(value)
                    print(f"{prefix}[Stream] {entry.name}: {value_str}")
            else:
                print(f"{prefix}[Unknown] {getattr(entry, 'name', 'no name')}")
        recurse(cf.root)

if __name__ == "__main__":
    rdb_path = r"c:\\Users\\Dell\\AppData\\Roaming\\SEL\\AcSELerator\\QuickSet\\Relay.rdb"
    print_rdb_structure(rdb_path)