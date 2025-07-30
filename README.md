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

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
