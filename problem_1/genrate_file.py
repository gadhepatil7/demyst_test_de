import json
import csv
import random
import string
import argparse

def read_spec_json(spec_file):
    """
    Reads the JSON specification file and processes the data.
    Args:
        spec_file (str): The path to the JSON file containing specifications.
    Returns:
        dict: A dictionary containing the processed specification details.
    """
    with open(spec_file, 'r', encoding='utf-8') as file:
        spec = json.load(file)
    # Convert string offsets to integers
    spec['Offsets'] = [int(offset) for offset in spec['Offsets']]
    # Convert the IncludeHeader value to a boolean
    spec['IncludeHeader'] = spec['IncludeHeader'].lower() == 'true'
    return spec

def generate_random_data_as_fixed_width(spec, num_records=10):
    """
    Generates random data in a fixed-width format based on the provided specification.
    Args:
        spec (dict): The specification dictionary containing details like column names, offsets, etc.
        num_records (int): The number of random records to generate.
    Returns:
        list: A list of strings, each representing a line in the fixed-width format.
    """
    column_names = spec['ColumnNames']
    offsets = spec['Offsets']
    include_header = spec['IncludeHeader']
    fixed_width_encoding = spec['FixedWidthEncoding']
    lines = []
    # Generate header line if required
    if include_header:
        header = ''.join([name.ljust(offset) for name, offset in zip(column_names, offsets)])
        # Encode and decode the header line with the specified encoding
        lines.append(header.encode(fixed_width_encoding).decode(fixed_width_encoding))  
    # Generate random data lines
    for _ in range(num_records):
        line = ''.join(
            ''.join(random.choices(string.ascii_letters + string.digits, k=offset)).ljust(offset)
            for offset in offsets
        )
        # Encode and decode the data line with the specified encoding
        lines.append(line.encode(fixed_width_encoding).decode(fixed_width_encoding))   
    return lines

def fixed_width_to_csv(spec_file, output_csv_file, num_records=10):
    """
    Converts the generated fixed-width data into a CSV file.
    Args:
        spec_file (str): The path to the JSON specification file.
        output_csv_file (str): The path where the CSV file will be saved.
        num_records (int): The number of random records to generate.
    """
    # Read the specification from the JSON file
    spec = read_spec_json(spec_file)
    # Generate fixed-width formatted data
    fixed_width_lines = generate_random_data_as_fixed_width(spec, num_records=num_records)
    # Write the fixed-width data to a CSV file
    with open(output_csv_file, 'w', newline='', encoding=spec['DelimitedEncoding']) as csv_file:
        writer = csv.writer(csv_file)
        # Write header row if specified
        if spec['IncludeHeader']:
            writer.writerow(spec['ColumnNames'])
        # Write the data rows
        for line in fixed_width_lines[1:] if spec['IncludeHeader'] else fixed_width_lines:
            start = 0
            row = []
            for offset in spec['Offsets']:
                # Extract and trim each field based on the offset
                field = line[start:start + offset].strip()
                row.append(field)
                start += offset
            writer.writerow(row)

#python3 genrate_file.py --spec_file spec.json --output_csv_file sample_data.csv
if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Generate a CSV file from random fixed-width data based on a JSON specification.")
    parser.add_argument("--spec_file", type=str, required=True,
                        help="Path to the spec.json file with formatting details.")
    parser.add_argument("--output_csv_file", type=str, required=True,
                        help="Output CSV file name.")
    parser.add_argument("--num_records", type=int, default=10,
                        help="Optional: Number of records to process. If not provided, all records will be processed.")
    args = parser.parse_args() 
    # Extract arguments
    spec_file = str(args.spec_file)
    output_csv_file = str(args.output_csv_file)
    num_records = int(args.num_records)

    # Generate the CSV file based on the specifications
    fixed_width_to_csv(spec_file, output_csv_file,num_records)
