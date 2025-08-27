# SELConnect - Project Overview

## Project Summary

SELConnect is a Python-based automation toolkit designed to streamline the configuration and protection settings of SEL relays (such as SEL-710, SEL-751) using Python, QuickSet, and RTAC. The system automates the generation of relay configuration files from a centralized Master CSV, eliminating manual programming and reducing human error.

## Key Features

1. **Automated Configuration Generation**: Automatically generates relay configuration files from a centralized Master CSV
2. **Batch Processing**: Supports batch configuration for multiple relays (10-50 units), enabling scalable deployment
3. **Multiple Output Formats**: Generates both QuickSet template files (.txt) and SCL XML files for RTAC integration
4. **Error Reduction**: Eliminates manual programming errors by automating the configuration process
5. **Standardization**: Ensures consistent configuration across all relays through centralized data management

## Technical Architecture

### Core Components

- **Python Automation**: Core scripts parse a Master CSV containing all relay settings and generate individual configuration files for each relay
- **Relay Support**: Supports various SEL relay models including SEL-710, SEL-751, SEL-351, SEL-487E
- **Integration**: Generated files are compatible with SEL QuickSet for relay programming and can be imported into SEL Architect for RTAC integration (DNP3/IEC61850 protocols)
- **Data Organization**: All relay parameters (e.g., FLA, CTR, VNOM) are consolidated in a single CSV, with automated reporting for transparency and standardization

### Main Modules

1. **cli.py**: Command-line interface for running extraction and generation tasks
2. **multi_generator.py**: Generates configuration files for multiple relays based on the Master CSV
3. **rdb_parser.py**: Low-level parser for SEL RDB files (regex-based)
4. **extractor.py**: Extracts relay settings from RDB files using mapping definitions
5. **template_generator.py**: Produces relay-specific templates for configuration
6. **csv_report.py**: Generates summary reports and exports processed data to CSV

## Problems Solved

### A. Manual Configuration
- **Problem**: Manual relay setup in QuickSet is time-consuming and prone to human error
- **Solution**: Python scripts automatically generate configuration files from the Master CSV, ensuring consistency and accuracy

### B. Managing Multiple Relays
- **Problem**: Manual management of dozens of relays is inefficient and error-prone
- **Solution**: The Master CSV and generator produce ready-to-use configuration files for each relay, simplifying bulk operations

### C. RTAC Integration
- **Problem**: Manual setup of communication protocols (DNP3/IEC61850) in Architect is complex
- **Solution**: Pre-generated configuration files can be directly imported into Architect, allowing RTAC to distribute settings automatically

### D. Transparency & Standardization
- **Problem**: Tracking relay values (FLA, CTR, VNOM, etc.) is difficult when data is scattered
- **Solution**: All data is organized in a single CSV, with automated reports for easy auditing and standardization

## Project Structure

```
├── selprotopy/                 # Main Python package containing all automation logic
│   ├── cli.py                  # Command-line interface
│   ├── extractor.py            # Extracts relay settings from RDB files
│   ├── multi_generator.py      # Generates configuration files for multiple relays
│   ├── rdb_parser.py           # Low-level parser for SEL RDB files
│   ├── template_generator.py   # Produces relay-specific templates
│   ├── csv_report.py           # Generates summary reports
│   └── __init__.py             # Package initialization
├── samples/                    # Sample input files for testing and demonstration
│   ├── Master.csv              # Centralized relay settings for batch generation
│   ├── config_input.csv        # Example configuration input for relays
│   ├── mapping_710.json        # Field mapping definitions for extraction logic
│   └── sample_710.rdb          # Example SEL-710 relay database file
├── out_relays/                 # Output directory for generated relay configuration files
│   ├── Relay01/                # Each relay has its own subfolder
│   │   ├── Relay01_template.txt # Generated template for the relay
│   │   └── Relay01.scl.xml     # SCL XML file for integration with Architect/RTAC
│   └── ...                     # Additional relay folders
├── tests/                      # Unit tests for all major modules
│   ├── test_csv_report.py
│   ├── test_extractor.py
│   ├── test_rdb_generator.py
│   └── test_rdb_parser.py
├── README.md                   # Project documentation and technical overview
├── pyproject.toml              # Python project configuration and dependencies
└── Other files                 # Generated or log files (extracted.csv, relay_settings.csv, etc.)
```

## Usage

1. Prepare the Master CSV with all relay settings
2. Run the generator script:
   ```bash
   python -m selprotopy.multi_generator --out out_relays
   ```
3. Import generated files into QuickSet or Architect as needed

## Requirements

- Python 3.9+
- SEL QuickSet
- SEL Architect
- RTAC (for integration)

## Sample Output

The tool generates two types of files for each relay:

1. **QuickSet Template (.txt)**:
   ```
   ; SEL QuickSet Import Template - generated
   ; Relay ID: Relay01

   [Device]
   Model=SEL-710
   Serial=710-0001

   [CT/PT]
   CT Primary=400
   CT Secondary=5
   PT Primary=11000
   PT Secondary=110

   [Protection]
   50P1T Pickup=500
   51P1T Time=0.5

   [Comm]
   Baud=9600
   Protocol=DNP3
   ```

2. **SCL XML File**: For RTAC integration with IEC61850 protocol support

## Development Information

- Developed by AOUF Nihed during internship at Ateam Pro-tech
- Project uses setuptools for packaging
- Includes comprehensive unit tests for all major modules
- Command-line interface available via `selprotopy-extract` command

This project significantly reduces the time and effort required to configure multiple SEL relays while ensuring consistency and reducing human error in the process.
