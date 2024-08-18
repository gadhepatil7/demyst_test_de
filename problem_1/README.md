# Fixed-Width to CSV Generator and Reader

## Overview

This project provides scripts for generating random fixed-width formatted data based on a given JSON specification, converting that data into a CSV file, and reading fixed-width formatted files back into a structured format.

### Key Features

- **Customizable Specifications**: Define column names, field widths, and encoding in a JSON specification file.
- **Random Data Generation**: Generate random alphanumeric data for each column according to the specified widths.
- **CSV Output**: Convert the generated fixed-width data into a CSV file.
- **Fixed-Width File Reading**: Convert a fixed-width formatted file back into a structured format using the same specification.
- **Command-Line Interface**: Easy-to-use command-line arguments for all operations.

## Prerequisites

- Python 3.x

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/fixed-width-to-csv.git
cd fixed-width-to-csv
```

## Usage

### 1. Generating CSV from Fixed-Width Data

To generate a CSV file from random fixed-width data, use the following command:

```bash
python3 genrate_file.py --spec_file spec.json --output_csv_file sample_data.csv --num_records 10
```

#### Command-Line Arguments

- `--spec_file`: (Required) Path to the JSON file containing the specifications (e.g., column names, offsets, encodings).
- `--output_csv_file`: (Required) Path where the output CSV file will be saved.
- `--num_records`: (Optional) Number of records to generate. Defaults to 10.

### 2. Reading a Fixed-Width File

To read a fixed-width formatted file and convert it to a structured format, use the following command:

```bash
python3 read_data.py --spec_file spec.json --input_file generated_data.txt --num_records 5
```

#### Command-Line Arguments

- `--spec_file`: (Required) Path to the JSON specification file (e.g., `spec.json`).
- `--input_file`: (Required) Path to the input fixed-width file.
- `--num_records`: (Optional) Number of records to process. If not provided, all records will be processed.

### Example

Assume you have the following `spec.json`:

```json
{
    "ColumnNames": ["FirstName", "LastName", "Age"],
    "Offsets": ["10", "10", "3"],
    "IncludeHeader": "true",
    "FixedWidthEncoding": "utf-8",
    "DelimitedEncoding": "utf-8"
}
```

**Step 1: Generate CSV**

You can generate a CSV file with 10 random records by running:

```bash
python3 genrate_file.py --spec_file spec.json --output_csv_file sample_data.csv --num_records 10
```

**Step 2: Read Fixed-Width File**

To read a fixed-width formatted file (e.g., `generated_data.txt`) and convert it to a structured format, run:

```bash
python3 read_data.py --spec_file spec.json --input_file generated_data.txt --num_records 5
```

This will print out the structured data

## JSON Specification Details

The `spec.json` file should include the following fields:

- `ColumnNames`: An array of strings representing the column names.
- `Offsets`: An array of strings representing the width of each column in the fixed-width format.
- `IncludeHeader`: A boolean-like string ("true" or "false") indicating whether to include a header row in the output.
- `FixedWidthEncoding`: The character encoding for the fixed-width format.
- `DelimitedEncoding`: The character encoding for the output CSV file.
