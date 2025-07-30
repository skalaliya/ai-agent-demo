### What is smolagents - smolagents is a lightweight Python library that provides basic building blocks—like tools, agents, memory, and output parsers—to help you easily orchestrate LLM‑driven multi‑step workflows and tool‑calling logic.

## What is An agent## - An agent is any system (often powered by an LLM) that decides, acts, and possibly loops or calls tools to solve a task, whereas smolagents is a specific minimal Python library that gives you the building blocks (tools, memory, output parsers, prompts, etc.) to actually implement those agents without writing all the plumbing yourself.

**Why smolagents ?**
For some low-level agentic use cases, like chains or routers, you can write all the code yourself. You’ll be much better that way, since it will let you control and understand your system better.

But once you start going for more complicated behaviours like letting an LLM call a function (that’s “tool calling”) or letting an LLM run a while loop (“multi-step agent”), some abstractions become necessary:

For tool calling, you need to parse the agent’s output, so this output needs a predefined format like “Thought: I should call tool ‘get_weather’. Action: get_weather(Paris).”, that you parse with a predefined function, and system prompt given to the LLM should notify it about this format.
For a multi-step agent where the LLM output determines the loop, you need to give a different prompt to the LLM based on what happened in the last loop iteration: so you need some kind of memory.
See? With these two examples, we already found the need for a few items to help us:

Of course, an LLM that acts as the engine powering the system
A list of tools that the agent can access
A system prompt guiding the LLM on the agent logic: ReAct loop of Reflection -> Action -> Observation, available tools, tool calling format to use…
A parser that extracts tool calls from the LLM output, in the format indicated by system prompt above.
A memory
But wait, since we give room to LLMs in decisions, surely they will make mistakes: so we need error logging and retry mechanisms.

All these elements need tight coupling to make a well-functioning system. That’s why we decided we needed to make basic building blocks to make all this stuff work together


# AI Agent Demo

A minimal Python project showing how to chat with local Ollama LLMs via the [🤗 smolagents](https://github.com/huggingface/smolagents) library.  
Pick from several Ollama‑hosted models, send a prompt, and get a response back in the console (or a Jupyter notebook).

---

## 🌟 Features

- 🎛️ **Model Selection**  
  Choose from Qwen-2, Deepseek‑R1, Mistral, LLaMA 2/3, and more via a simple menu.

- 💬 **Chat Interface**  
  One‑line call to `model([ChatMessage(...)])` returns a rich response object.

- 🔧 **Easy Configuration**  
  Point at any Ollama API endpoint (e.g. `http://127.0.0.1:11434`) via `run_agent.py` or `main.py`.

- 📓 **Jupyter Notebook Example**  
  See `app.ipynb` for an interactive demo and playground.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+  
- [Ollama](https://ollama.com/) running locally or remote  
- (Optional) Virtual environment tool of your choice

### Installation

1. **Clone the repo**  
   ```bash
   git clone git@github.com:skalaliya/ai-agent-demo.git
   cd ai-agent-demo

2. Create and activate a venv
# AI LLM Tokenizer Playground

This project compares tokenization behavior between OpenAI models (like GPT-3.5, GPT-4) using `tiktoken`, and Hugging Face models (like Mistral, LLaMA) using `transformers`.

3. Install dependencies
## 🔧 Setup

⚙️ Configuration
Create a .env in the project root to point at your Ollama server:

OLLAMA_API_BASE=http://127.0.0.1:11434
Note: .env is already in .gitignore, so your secrets stay local.

💻 Usage
1. Interactive Script
Run the menu‑driven agent:

python run_agent.py
You’ll see a list of models. Pick one (1–6), enter your prompt, and get the response:

Choose a model:
 1. ollama_chat/qwen2:7b
 2. ollama_chat/deepseek-r1:latest

Pick model number (1–6): 3
Enter your prompt: Hello, AI!
🧠 Response: “Hi there! How can I help…”
2. Import in Your Code
python
Copy
Edit
from smolagents import LiteLLMModel, ChatMessage
import os

model = LiteLLMModel(
    model_id="ollama_chat/mistral:latest",
    api_base=os.environ["OLLAMA_API_BASE"]
)

msg = ChatMessage(role="user", content=[{"type": "text", "text": "Tell me a joke"}])
response = model([msg])
print(response.content)
3. Jupyter Notebook
Open app.ipynb and run each cell to experiment with tokenization, model calls, and plotting.

🧪 Tests
A simple smoke test lives in test.py. Run:

python test.py
It will invoke the default model on a fixed prompt and exit cleanly.

🤝 Contributing
Fork the repo

Create a branch: git checkout -b feat/your-feature

Commit your changes: git commit -am "Add <feature>"

Push to your branch: git push origin feat/your-feature

Open a Pull Request

📄 License
This project is released under the MIT License. See LICENSE for details.

© 2025 Sam (skalaliya) · GitHub
