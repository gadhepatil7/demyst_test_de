import json
import argparse
from genrate_file import read_spec_json

def read_fixed_width_file(input_file, spec_file):
    """
    Reads a fixed-width formatted file according to the specifications provided in a JSON file.
    Args:
        input_file (str): The path to the input fixed-width file.
        spec_file (str): The path to the JSON file containing the specifications.
    Returns:
        list: A list of dictionaries, where each dictionary represents a record from the fixed-width file.
    """
    # Load the specification from the JSON file
    spec = read_spec_json(spec_file)
    # Extract relevant information from the spec
    column_names = spec['ColumnNames']
    offsets = spec['Offsets']
    fixed_width_encoding = spec['FixedWidthEncoding']
    include_header = spec['IncludeHeader']
    # Read the fixed-width file using the specified encoding
    with open(input_file, 'r', encoding=fixed_width_encoding) as fwf:
        lines = fwf.readlines()
    data = []
    # Determine if there is a header and where to start reading data
    data_start_index = 1 if include_header else 0
    # Process each line based on the offsets to extract the fields
    for line in lines[data_start_index:]:
        start = 0
        record = {}
        for name, offset in zip(column_names, offsets):
            field = line[start:start + offset].strip()
            record[name] = field
            start += offset
        data.append(record)
    return data

#python3 read_data.py --spec_file spec.json --input_file generated_data.txt --num_records 5
if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Read a fixed-width file and convert it to a structured format based on a given specification.")
    parser.add_argument("--spec_file", type=str, required=True,
                        help="Path to the JSON specification file (spec.json).")
    parser.add_argument("--input_file", type=str, required=True,
                        help="Path to the input fixed-width file.")
    parser.add_argument("--num_records", type=int, default=None,
                        help="Optional: Number of records to process. If not provided, all records will be processed.")
    args = parser.parse_args()

    # Extract arguments
    spec_file = str(args.spec_file)
    input_file = str(args.input_file)
    num_records = args.num_records

    # Read the fixed-width file according to the spec
    data = read_fixed_width_file(input_file, spec_file)
    
    # If num_records is specified, slice the data list to process only that many records
    if num_records is not None:
        data = data[:num_records]

    # Print out the parsed data for each record
    for record in data:
        print(record)
