# Fine-Tuning with ChatGPT

OpenAI's ChatGPT allows users to fine-tune certain NLP models for better alignment with specific tasks or datasets. Here's a step-by-step guide:

Prerequisites:
    1. Must have OpenAi installed:
        Nothing will compile with out OpenAI packages
    
    2. API Key: 
        To leverage fine-tuning, you need an OpenAI API key.

    3. Billing Account: 
        Sign up with OpenAI and activate a billing account. Charges apply each time you use the API.
    4. Training Data:
        Ensure your dataset is sizable for effective fine-tuning.
        Data format varies based on the model chosen.

Steps to install OpenAI:
    1. Install pip and make sure its up to date
        macOS and Linux:
            sudo apt-get install python-pip
                        or
            sudo apt-get install python3-pip

            pip install --upgrade pip
                        or
            pip3 install --upgrade pip
        
        windows:
            python get-pip.py
            python -m pip install --upgrade pip
    
    2. Install OpenAI:
        All platforms (macOS, Linux, Windows):
            pip3 install openai
                    or
            pip install openai

            pip3 install --upgrade openai
                    or
            pip install --upgrade openai


Models Available for Fine-Tuning:
    1. gpt-3.5-turbo-0613 (Recommended)
    2. babbage-002
    3. davinci-002 (Model used in this code)

Data Formatting:
    For gpt-3.5-turbo-0613:
        Data should be in a conversational chat format.

        Example:
        {"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}

    For babbage-002 and davinci-002:
        Data should be in a prompt-completion format.

        Example:   
        {"prompt": "<prompt text>", "completion": "<ideal generated text>"}

Fine-Tuning Procedure:
    1. Upload your training data:

       response = openai.File.create(
        file=open("Training_data_file_Name.jsonl", "rb"),purpose='fine-tune'
        )
 
    2. Initiate the fine-tuning job:
       file_id = response['id']
       result = openai.FineTuningJob.create(training_file=file_id, model="davinci-002")

    3. Note:
        After initiation, the model won't be immediately available. Once processing is complete, OpenAI will send an email containing a link to your fine-tuned model. Click on the "Fine Tuning" hyperlink in the email to access your model ID.

Using the Fine-Tuned Model:
    Once you've retrieved your model ID, you can test and utilize your fine-tuned model:

    user_input = input("Enter your prompt: ")
    response = openai.Completion.create(
        model="ft:davinci-002:personal::YOUR_MODEL_ID", # Replace with your actual model ID
        prompt=user_input
    )
    print(response.choices[0].text.strip())


If any erros occur please look at the "common_errors.md" for solutions to common issues.