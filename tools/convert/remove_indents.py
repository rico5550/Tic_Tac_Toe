import json


def format_json(input_data):
    formatted_output = []

    for record in input_data:
        formatted_output.append(json.dumps(record, separators=(',', ':')))

    return "\n".join(formatted_output)

# Read the input file
with open('Your_Data_File.jsonl', 'r') as input_file:
    data = json.load(input_file)

# Get the formatted data
formatted_data = format_json(data)

# Write the formatted data to the output file
with open('New_data.jsonl', 'w') as output_file:
    output_file.write(formatted_data)
