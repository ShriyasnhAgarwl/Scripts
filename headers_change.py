import csv
import os

def replace_header(input_files, output_files, new_header):
    for i, input_file in enumerate(input_files):
        with open(input_file, 'r', encoding='utf-8') as csv_in:
            reader = csv.reader(csv_in)
            data = list(reader)

        data[0] = new_header

        with open(output_files[i], 'w', newline='', encoding='utf-8') as csv_out:
            writer = csv.writer(csv_out)
            writer.writerows(data)
# Example usage
input_files = ['','']  # Replace with your input file paths
output_files = ['','']  # Replace with desired output file paths
new_header = ['xyz','abc']  # Replace with your new header

replace_header(input_files, output_files, new_header)
