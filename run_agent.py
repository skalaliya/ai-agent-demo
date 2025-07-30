from smolagents import LiteLLMModel, ChatMessage

MODEL_MAP = {
    1: "ollama_chat/qwen2:7b",
    2: "ollama_chat/deepseek-r1:latest",
    3: "ollama_chat/llama3:8b-instruct-q8_0",
    4: "ollama_chat/mistral:latest",
    5: "ollama_chat/llama2:latest",
    6: "ollama_chat/llama3:latest"
}

def choose_model():
    print("\nChoose a model:")
    for idx, name in MODEL_MAP.items():
        print(f" {idx}. {name}")
    sel = int(input("\nPick model number (1–6): ").strip())
    return MODEL_MAP.get(sel)

def main():
    model_id = choose_model()
    if not model_id:
        print("❌ Invalid choice. Exiting.")
        return

    model = LiteLLMModel(
        model_id=model_id,
        api_base="http://127.0.0.1:11434"
    )

    prompt = input("\nEnter your prompt: ").strip()
    if not prompt:
        print("❌ No prompt given. Exiting.")
        return

    # create a ChatMessage instead of a dict
    user_msg = ChatMessage(role="user", content=[{"type": "text", "text": prompt}])

    # pass a list of ChatMessage into the model
    response = model([user_msg])

    # print out the .content of the returned ChatMessage
    print("\n🧠 Response:", response.content)


# ← this makes Python run main() when you do `python run_agent.py`
if __name__ == "__main__":
    main()