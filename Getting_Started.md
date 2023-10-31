# Fine-Tuning with ChatGPT

OpenAI's ChatGPT allows users to fine-tune certain NLP models for better alignment with specific tasks or datasets. Here's a step-by-step guide:

## Prerequisites:

- **OpenAI Installation**: Nothing will compile without OpenAI packages.
  
- **API Key**: To leverage fine-tuning, you need an OpenAI API key.

- **Billing Account**: Sign up with OpenAI and activate a billing account. Charges apply each time you use the API.

- **Training Data**: Ensure your dataset is sizable for effective fine-tuning. Data format varies based on the model chosen.

## Steps to Install OpenAI:

1. **Install pip and update it**:

    - **macOS and Linux**:

        ```bash
        sudo apt-get install python-pip
        # or
        sudo apt-get install python3-pip

        pip install --upgrade pip
        # or
        pip3 install --upgrade pip
        ```

    - **Windows**:

        ```bash
        python get-pip.py
        python -m pip install --upgrade pip
        ```

2. **Install OpenAI**:

    - **All platforms (macOS, Linux, Windows)**:

        ```bash
        pip3 install openai
        # or
        pip install openai

        pip3 install --upgrade openai
        # or
        pip install --upgrade openai
        ```

## Models Available for Fine-Tuning:

1. **gpt-3.5-turbo-0613** (Recommended)
2. **babbage-002**
3. **davinci-002** (Model used in this code)

## Data Formatting:

- **For gpt-3.5-turbo-0613**: Data should be in a conversational chat format.

    **Note** The example below is for human readablity. Before using the data make sure to remove all indentation. Navigate to tools/convert/remove_indents.py the file there should help out.

    **Example**:

    ```json
    {
        "messages": [
            {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
            {"role": "user", "content": "What's the capital of France?"},
            {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}
        ]
    }
    ```

- **For babbage-002 and davinci-002**: Data should be in a prompt-completion format.

    **Note** The example below is for human readablity. Before using the data make sure to remove all indentation. Navigate to tools/convert/remove_indents.py the file there should help out.

    **Example**:

    ```json
    {
        "prompt": "<prompt text>",
        "completion": "<ideal generated text>"
    }
    ```

## Fine-Tuning Procedure:

1. **Upload your training data**:

    ```python
    response = openai.File.create(
        file=open("Training_data_file_Name.jsonl", "rb"),
        purpose='fine-tune'
    )
    ```

2. **Initiate the fine-tuning job**:

    ```python
    file_id = response['id']
    result = openai.FineTuningJob.create(training_file=file_id, model="davinci-002")
    ```

3. **Note**: After initiation, the model won't be immediately available. Once processing is complete, OpenAI will send an email containing a link to your fine-tuned model. Click on the "Fine Tuning" hyperlink in the email to access your model ID.

## Using the Fine-Tuned Model:

Once you've retrieved your model ID, you can test and utilize your fine-tuned model:

Note: To find the ideal values for the numeric variables navigate to tools/parameter_values/value_finder.py

```python
user_input = input("Enter your prompt: ")
response = openai.Completion.create(
    model="ft:davinci-002:personal::YOUR_MODEL_ID", # Replace with your actual model ID
    prompt=user_input,
    temperature=None, #Controls the randomness of the model's output. A value closer to 1 makes the output more random, while a value closer to 0 makes it more deterministic.
    max_tokens=None, #The maximum length of the response.
    top_p=None, #Used for nucleus sampling, it specifies the cumulative probability of the top tokens to retain. This can help the model's output be more focused.
    frequency_penalty=None, #A penalty to apply to the frequency of tokens in the output. Can be positive (favor more frequent tokens) or negative (favor less frequent tokens).
    presence_penalty=None, #A penalty to add if certain tokens are present or absent in the output.
    n=None, #The number of completions to generate for each prompt.
    logprobs=None,#Number of log probabilities to include with the response, which can be used for examining or further processing the generated text.
    stop=None, #Tokens or sequences at which the model should stop generating further content. Ex: ["."]
    echo=False, #If set to True, the prompt will be included in the generated response.
    stream=False, #If set to True, allows the generated output to be streamed token by token rather than all at once.
    instruction=None, #Sometimes used to give high-level instructions to the model. Ex: "Make sure to keep the answer simple"
    return_prompt=None, #If True, the API response will include the given prompt.
    expand=None #Allows for use of role-based features, like giving instructions to the model as a particular character.

)
print(response.choices[0].text.strip())
