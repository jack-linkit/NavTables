import os
import sys


# Directory containing SQL output files
file_path = sys.argv[1]

# Read the file and filter out lines containing "(x rows affected)"
with open(file_path, 'r') as file:
    lines = file.readlines()

lines = [line for line in lines if (len(line) == 1) or (not line.strip().endswith(' row affected)') and not line.strip().endswith(' rows affected)') and not all(c == ',' or c =='-' for c in line.strip()))]

# Write the cleaned data back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)

print(f"Cleaned file: {file_path}")
