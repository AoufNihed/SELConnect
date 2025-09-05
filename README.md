<p align="center">
  <img width="2500" height="857" alt="SEL Schweitzer Engineering Laboratories" src="Logo.png" />
</p>

# SELConnect - Enhanced with SEL_RDB Integration

## Project Summary

SELConnect is a Python-based automation toolkit that streamlines the configuration of SEL relays by automatically generating configuration files from centralized data sources. This enhanced version uses the official SEL_RDB library to create perfect RDB files that work directly with QuickSet.

## Key Features

1. **Perfect RDB Generation**: Automatically generates true compound RDB files using the SEL_RDB library
2. **Direct QuickSet Compatibility**: Generated files can be read directly by QuickSet without import
3. **Batch Processing**: Supports batch configuration for multiple relays (10-50 units)
4. **Multiple Output Formats**: Generates both perfect RDB files and SCL XML files for RTAC integration
5. **Error Reduction**: Eliminates manual programming errors by automating the configuration process
6. **Standardization**: Ensures consistent configuration across all relays through centralized data management

## Technical Architecture

### Core Components

- **Python Automation**: Core scripts parse a Master CSV containing all relay settings and generate individual configuration files for each relay
- **SEL_RDB Integration**: Uses the official SEL_RDB library (https://github.com/AoufNihed/SEL_RDB) for perfect RDB file generation
- **Relay Support**: Supports various SEL relay models including SEL-710, SEL-751, SEL-351, SEL-487E
- **Integration**: Generated files are compatible with SEL QuickSet for relay programming and can be imported into SEL Architect for RTAC integration (DNP3/IEC61850 protocols)
- **Data Organization**: All relay parameters (e.g., FLA, CTR, VNOM) are consolidated in a single CSV, with automated reporting for transparency and standardization

### Main Modules

1. **cli.py**: Command-line interface for running extraction and generation tasks
2. **multi_generator.py**: Generates configuration files for multiple relays based on the Master CSV
3. **rdb_parser.py**: Low-level parser for SEL RDB files (regex-based)
4. **extractor.py**: Extracts relay settings from RDB files using mapping definitions
5. **enhanced_rdb_generator.py**: Core implementation using SEL_RDB library for perfect RDB generation
6. **csv_report.py**: Generates summary reports and exports processed data to CSV

## Problems Solved

### A. Manual Configuration
- **Problem**: Manual relay setup in QuickSet is time-consuming and prone to human error
- **Solution**: Python scripts automatically generate perfect RDB files from the Master CSV, ensuring consistency and accuracy

### B. Managing Multiple Relays
- **Problem**: Manual management of dozens of relays is inefficient and error-prone
- **Solution**: The Master CSV and generator produce ready-to-use perfect RDB files for each relay, simplifying bulk operations

### C. RTAC Integration
- **Problem**: Manual setup of communication protocols (DNP3/IEC61850) in Architect is complex
- **Solution**: Pre-generated configuration files can be directly imported into Architect, allowing RTAC to distribute settings automatically

### D. Transparency & Standardization
- **Problem**: Tracking relay values (FLA, CTR, VNOM, etc.) is difficult when data is scattered
- **Solution**: All data is organized in a single CSV, with automated reports for easy auditing and standardization

## Usage

### 1. Prepare the Master CSV with all relay settings

### 2. Generate perfect RDB files:
```bash
# Generate a single perfect RDB file
python -m selprotopy.cli generate --csv config.csv --out relay.rdb --perfect

# Generate perfect RDB files for multiple relays
python -m selprotopy.multi_generator --csv Master.csv --out output_directory --perfect
```

### 3. Use generated files directly in QuickSet or import into Architect as needed

## Requirements

- Python 3.9+
- SEL QuickSet
- SEL Architect
- RTAC (for integration)
- SEL_RDB library

## Sample Output

### Perfect Compound RDB File:
- File size: ~55KB (vs ~300 bytes for text files)
- Format: OLE2 structured storage (compound document)
- Usage: Direct reading by QuickSet
- Structure: Proper internal directory with streams

### SCL XML File: For RTAC integration with IEC61850 protocol support

## Development Information

- Developed by AOUF Nihed during internship at Ateam Pro-tech
- Project uses setuptools for packaging
- Includes comprehensive unit tests for all major modules
- Command-line interface available via `selprotopy-extract` command
- Enhanced with official SEL_RDB library integration for perfect RDB generation

This enhanced project significantly reduces the time and effort required to configure multiple SEL relays while ensuring consistency and reducing human error in the process, using the official SEL_RDB library for perfect compatibility.
