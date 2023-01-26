import openai

# Step 1: Sign up for an API key from OpenAI
openai.api_key = "YOUR_API_KEY"

# Step 2: Use the openai.Completion.create() method to generate a new completion model
model_engine = "text-davinci-002"

while True:
    prompt = input("You: ")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Step 3: Print the response from the model
    message = completions.choices[0].text
    print("ChatGPT: "+ message)
