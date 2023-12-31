import json

# Load the original JSON data
# Make sure to replace the file names with your own
with open("Your_data_file.json", "r") as json_file:
    data = json.load(json_file)

# Convert to prompt-completion format
converted_data = [{"prompt": item["prompt"], "completion": item["response"]} for item in data]

# Write to a JSONL file
with open("data/converted_PR_PC.jsonl", "w") as jsonl_file:
    for item in converted_data:
        jsonl_file.write(json.dumps(item) + "\n")
