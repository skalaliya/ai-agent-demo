import litellm

# Define your model list
models = {
    1: "ollama_chat/qwen2:7b",
    2: "ollama_chat/deepseek-r1:latest",
    3: "ollama_chat/llama3:8b-instruct-q8_0",
    4: "ollama_chat/mistral:latest",
    5: "ollama_chat/llama2:latest",
    6: "ollama_chat/llama3:latest"
}

# 🔢 Select your model number here
model_number = 2  # ⬅️ change this number only

# ✅ Get the model from the dictionary
model_name = models.get(model_number)

# 🚫 Handle wrong input
if model_name is None:
    raise ValueError(f"Invalid model number: {model_number}. Choose from: {list(models.keys())}")

# ✅ Send message using selected model
response = litellm.completion(
    model=model_name,
    api_base="http://127.0.0.1:11434",
    messages=[
        {"role": "user", "content": "Tell me a fun fact about the ocean."}
    ]
)

# ✅ Print result
print(f"\n🤖 Using Model {model_number}: {model_name}")
print(response['choices'][0]['message']['content'])
