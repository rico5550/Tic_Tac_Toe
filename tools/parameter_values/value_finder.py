from tools.parameter_values.value_generator import Value_Generator
from tools.parameter_values.eval_response import Evaluate_Response
from tqdm import tqdm
import openai


id = open('data/dav_model_ID.txt', 'r')
Model_ID = id.read().strip()
key = open('data/api_key.txt', 'r')
api_key = key.read().strip()
openai.api_key = api_key
all_combinations, chosen_params = Value_Generator()  # Modified to also return the chosen parameters for correct unpacking
best_score = float('-inf')
best_combo = None
best_response = ""

temperature = 0.5
max_tokens = 50
top_p = .5
frequency_penalty = 0
presence_penalty = 0
n = 1
logprobs = 1

user_input = input("Enter your prompt: ")
desired_output = input("Enter your desired output: ")

for combo in tqdm(all_combinations, desc="Testing Combinations", ncols=100):
    # This dynamically unpacks the values based on the chosen parameters
    param_values = dict(zip(chosen_params, combo))

        # Update the values of the parameters based on user selection
    if "temperature" in param_values:
        temperature = param_values["temperature"]
    if "max_tokens" in param_values:
        max_tokens = param_values["max_tokens"]
    if "top_p" in param_values:
        top_p = param_values["top_p"]
    if "frequency_penalty" in param_values:
        frequency_penalty = param_values["frequency_penalty"]
    if "presence_penalty" in param_values:
        presence_penalty = param_values["presence_penalty"]
    if "n" in param_values:
        n = param_values["n"]
    if "logprobs" in param_values:
        logprobs = param_values["logprobs"]
    
    # Make the API call
    response = openai.Completion.create(
        model=Model_ID,
        prompt=user_input,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        n=n,
        logprobs=logprobs,
        stop=['.']
    )

    # Assuming the first response (since n=1)
    generated_response = response.choices[0].text.strip()

    # Evaluate the response
    score = Evaluate_Response(generated_response, desired_output)

    # Check if this score is the best so far
    if score > best_score:
        best_score = score
        best_combo = combo
        best_response = generated_response

print("Best Score:", best_score)
print("Best Combination:", best_combo)
print("Best Response:", best_response)

