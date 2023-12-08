import pyodbc
import pandas as pd
import sys

SERVER="10.252.36.127"
DATABASE="AdminReportingStage"
USER="jackostage"
PASSWORD="x!&f7QKDm(VZCtj3"

# Establish a connection
print('Establishing connecttion...')
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USER};PWD={PASSWORD};TrustServerCertificate=yes')
print('Connection established.')

parent_folder = sys.argv[1]
output_folder = sys.argv[2]
scripts_folder = parent_folder + '/Tables'

scripts = [f'{output_folder}/Setup.sql', f'{scripts_folder}/District.sql']
try:
    # Create a cursor
    cursor = conn.cursor()

    # Execute each script
    for i, script_path in enumerate(scripts):
        # setup file comes from output folder, others come from template folder
        print(f'Current file: {script_path}...')

        with open(script_path, 'r') as file:
            script = file.read()
        cursor.execute(script)

    # if it is not the setup file, output to csv
    if i == 0:
        conn.commit()
    else:
        rows = cursor.fetchall()
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cursor.description])
        table_type = script_path.split('.')[0].split('/')[-1]
        print(table_type)
        df.to_csv(f'{output_folder}/{table_type}.csv', index=False)

finally:
    # Close the connection
    cursor.close()
    conn.close()
    print('Connection closed.')