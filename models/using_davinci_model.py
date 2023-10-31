import openai

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

try:
    with open("data/dav_model_ID.txt", "r") as f:
        modelid = f.read().strip()
    
    if not modelid:
        raise ValueError("Model ID is empty!")
    
    Model_ID = modelid

except FileNotFoundError:
    print("Error: model_ID.txt file not found. Please ensure you have the Model ID stored in this file.")
    exit(1)
except ValueError as ve:
    print(f"Error: {ve}")
    exit(1)
except Exception as e:
    print(f"Unexpected error occurred: {e}")
    exit(1)

user_input = input("Enter your prompt: ")




response = openai.Completion.create(
    model=Model_ID, # The ID of your fine-tuned model
    prompt=user_input, 
    temperature=0.2, # Determines the randomness of the model's output. The closer to 1.0 the more random
    top_p=0.2, # it specifies the cumulative probability of the top tokens to retain. Helps the model be more focused
    frequency_penalty=-0.2, # A penalty to apply to the frequency of tokens in the output. Can be positive (favor more frequent tokens) or negative (favor less frequent tokens).
    stop=['.'], # indicates where to stop generating
    max_tokens=50, # maxes out the size of the response to 50 tokens
    n=1, # number of responses generated
    # echo = True # the prompt is printed prior to the models response
)

print(response.choices[0].text.strip())
