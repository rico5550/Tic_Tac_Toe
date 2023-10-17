import openai

# Try to read the API key from a file
try:
    with open("data/api_key.txt", "r") as f:
        api_key = f.read().strip()
    
    if not api_key:
        raise ValueError("API key is empty!")
    
    openai.api_key = api_key

except FileNotFoundError:
    print("Error: api_key.txt file not found. Please ensure you have the API key stored in this file.")
    exit(1)
except ValueError as ve:
    print(f"Error: {ve}")
    exit(1)
except Exception as e:
    print(f"Unexpected error occurred: {e}")
    exit(1)

# Continue with the rest of the code
response = openai.File.create(
  file=open("Your_Training_Date_file", "rb"),
  purpose='fine-tune'
)

file_id = response['id']
result = openai.FineTuningJob.create(training_file=file_id, model="davinci-002")






