import os
import sys 
import csv

from district_table_script import create_file

DISTRICTS_FILE_PATH = '/Users/jackoconnor/WorkRoot/utils/districts.txt'

MODE = 'PA'

generic_script_path = f'{MODE}NavTables.sql'

district_ids = set([3081, 6501, 4877])

# for every row in the districts.txt file, run the create_file function with the district id in col 2
# and the template file as the input file

def create_all_tables():
    try:
        with open(DISTRICTS_FILE_PATH, 'r') as districts_file:
            districts_reader = csv.reader(districts_file, delimiter='\t')
            for row in districts_reader:
                district_id = int(row[1])
                district_short = row[2]
                outfile_name = f"/Users/jackoconnor/WorkRoot/utils/table_scripts/{district_short}_tables.sql"
                if district_id in district_ids:
                    create_file(generic_script_path, district_id, outfile_name)
    except FileNotFoundError:
        print(f"Error: File '{DISTRICTS_FILE_PATH}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    create_all_tables()