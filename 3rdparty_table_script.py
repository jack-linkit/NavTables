import sys


def create_file(input_file_path, district_id, output_file_path):
    try:
        with open(input_file_path, 'r') as template_file:
            template_contents = template_file.read()

        sql_declaration = f"DECLARE @DistrictID VARCHAR(5) = '{district_id}'\n"

        with open(output_file_path, 'w') as output_file:
            output_file.write(sql_declaration + template_contents)

        print(f'SQL declaration and template content written to {output_file_path}')

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' or 'template.sql' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <districtID> <input_file> <output_file>")
        sys.exit(1)

    input_file_path = sys.argv[2]
    district_id = sys.argv[1] 
    output_file_path = sys.argv[3]
    create_file(input_file_path, district_id, output_file_path)


