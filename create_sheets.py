import pyodbc
import pandas as pd
import sys

SERVER="10.252.36.127"
DATABASE="AdminReportingStage"
USER="jackostage"
PASSWORD="x!&f7QKDm(VZCtj3"

# Establish a connection
print('Establishing connecttion...')
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USER};PWD={PASSWORD}')
print('Connection established.')

# Create a cursor
cursor = conn.cursor()

parent_folder = sys.argv[1]
output_folder = sys.argv[2]
# List of script files
scripts = ['Class.sql', 'District.sql', 'School.sql', 'Historical.sql']

# Execute each script
for i, script_file in enumerate(scripts):
    print(f'Current file: {script_file}...')
    # setup file comes from output folder, others come from template folder
    if i == 0:
        script_path = output_folder + '/' + script_file
    else:
        script_path = parent_folder + '/' + script_file

    with open(script_file, 'r') as file:
        script = file.read()
    cursor.execute(script)

    # if it is not the setup file, output to csv
    if i > 0:
        df = pd.read_sql(script, conn)
        table_type = script_file.split('.')[0]
        df.to_csv(f'{output_folder}/{table_type}.csv', index=False)

# Close the connection
conn.close()

print('Connection closed.')