import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and input prompt
model = "qwen3:4b"
prompt = "What is Github?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama: ")
print(response.response)
