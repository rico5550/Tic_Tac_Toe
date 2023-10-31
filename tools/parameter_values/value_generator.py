import itertools

def Value_Generator():
    # Define ranges for each parameter
    parameter_ranges = {
        "temperature": [i * 0.1 for i in range(11)],
        "max_tokens": list(range(1, 51)),
        "top_p": [i * 0.1 for i in range(1, 11)],
        "frequency_penalty": [i * 0.1 for i in range(-20, 21)],
        "presence_penalty": [i * 0.1 for i in range(-20, 21)],
        "n": list(range(1, 3)),
        "logprobs": list(range(3))
    }
    
    # Ask user which parameters they want to generate combinations for
    print("Available parameters: temperature, max_tokens, top_p, frequency_penalty, presence_penalty, n, logprobs")
    chosen_params = input("Enter comma-separated parameters you want to use (e.g., 'temperature,max_tokens'): ").split(',')
    
    # Filter only chosen parameters
    chosen_ranges = [parameter_ranges[param.strip()] for param in chosen_params if param.strip() in parameter_ranges]
    
    # Generate combinations
    combinations = itertools.product(*chosen_ranges)

    return list(combinations), chosen_params




