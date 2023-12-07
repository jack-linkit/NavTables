import sys
import os


def create_file(template_file_path, district_id, output_folder_path):
    output_file_path = output_folder_path + '/Setup.sql'
    try:
        try:
            with open(template_file_path, 'r') as template_file:
                template_contents = template_file.read()
            sql_declaration = f"DECLARE @DistrictID varchar(10) = '{district_id}'\n"

        except FileNotFoundError:
            print(f"Error: File '{template_file_path}' not found.")

        try:
            with open(output_file_path, 'w+') as output_file:
                output_file.write(sql_declaration + template_contents)
            print(f'SQL declaration and template content written to {output_file_path}')

        except FileNotFoundError:
            print(f"Error: File '{output_file_path}' not found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <districtID> <input_file> <output_file>")
        sys.exit(1)

    input_folder_path = sys.argv[2]
    district_id = sys.argv[1] 
    output_folder_path = sys.argv[3]

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    template_file_path = input_folder_path + '/Setup.sql'
    create_file(template_file_path, district_id, output_folder_path)


