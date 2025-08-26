# SELConnect

## Overview
SELConnect is a Python-based automation toolkit designed to streamline the configuration and protection settings of SEL relays (such as SEL-710, SEL-751) using Python, QuickSet, and RTAC. The system automates the generation of relay configuration files from a centralized Master CSV, eliminating manual programming and reducing human error.

## Technical Architecture
- **Python Automation**: Core scripts parse a Master CSV containing all relay settings and generate individual configuration files for each relay.
- **Relay Support**: Supports batch configuration for multiple relays (10–50 units), enabling scalable deployment.
- **Integration**: Generated files are compatible with SEL QuickSet for relay programming and can be imported into SEL Architect for RTAC integration (DNP3/IEC61850 protocols).
- **Data Organization**: All relay parameters (e.g., FLA, CTR, VNOM) are consolidated in a single CSV, with automated reporting for transparency and standardization.

## Problems Addressed & Solutions

### A. Manual Configuration
- Problem: Manual relay setup in QuickSet is time-consuming and prone to human error.
- Solution: Python scripts automatically generate configuration files from the Master CSV, ensuring consistency and accuracy.

### B. Managing Multiple Relays
- Problem: Manual management of dozens of relays is inefficient and error-prone.
- Solution: The Master CSV and generator produce ready-to-use configuration files for each relay, simplifying bulk operations.

### C. RTAC Integration
- Problem: Manual setup of communication protocols (DNP3/IEC61850) in Architect is complex.
- Solution: Pre-generated configuration files can be directly imported into Architect, allowing RTAC to distribute settings automatically.

### D. Transparency & Standardization
- Problem: Tracking relay values (FLA, CTR, VNOM, etc.) is difficult when data is scattered.
- Solution: All data is organized in a single CSV, with automated reports for easy auditing and standardization.


## Folder Structure & Technical Logic

- `selprotopy/`: Main Python package containing all automation logic.
	- `cli.py`: Command-line interface for running extraction and generation tasks.
	- `extractor.py`: Extracts relay settings from RDB files using mapping definitions.
	- `multi_generator.py`: Generates configuration files for multiple relays based on the Master CSV.
	- `rdb_parser.py`: Low-level parser for SEL RDB files (regex-based).
	- `template_generator.py`: Produces relay-specific templates for configuration.
	- `csv_report.py`: Generates summary reports and exports processed data to CSV.
	- `__init__.py`: Package initialization.

- `samples/`: Contains sample input files for testing and demonstration.
	- `config_input.csv`: Example configuration input for relays.
	- `mapping_710.json`: Field mapping definitions for extraction logic.
	- `Master.csv`: Centralized relay settings for batch generation.
	- `sample_710.rdb`: Example SEL-710 relay database file.

- `out_relays/`: Output directory for generated relay configuration files.
	- Each relay (Relay01, Relay02, ...) has its own subfolder containing:
		- `<RelayXX>_template.txt`: Generated template for the relay.
		- `<RelayXX>.scl.xml`: SCL XML file for integration with Architect/RTAC.

- `tests/`: Contains unit tests for all major modules to ensure reliability and correctness.
	- `test_csv_report.py`, `test_extractor.py`, `test_rdb_generator.py`, `test_rdb_parser.py`: Test scripts for respective modules.

- `README.md`: Project documentation and technical overview.

- `pyproject.toml`: Python project configuration and dependencies.

- Other files:
	- `extracted.csv`, `relay_settings.csv`, `run.txt`, `test_results.txt`: Generated or log files for tracking outputs and results.

## Usage
1. Prepare the Master CSV with all relay settings.
2. Run the generator script:
	 ```powershell
	 python -m selprotopy.multi_generator --out out_relays
	 ```
3. Import generated files into QuickSet or Architect as needed.

## Requirements
- Python 3.11+
- SEL QuickSet
- SEL Architect
- RTAC (for integration)

## Usage
1. Prepare the Master CSV with all relay settings.
2. Run the generator script:
	```powershell
	python -m selprotopy.multi_generator --out out_relays
	```
3. Import generated files into QuickSet or Architect as needed.

## Requirements
- Python 3.11+
- SEL QuickSet
- SEL Architect
- RTAC (for integration)


---

---
Developed by AOUF Nihed during internship at Ateam Pro-tech.

