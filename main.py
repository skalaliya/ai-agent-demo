
---

### ⚙️ 2. `main.py` – Clean script version of your notebook

```python
from dotenv import load_dotenv
import os
from huggingface_hub import login
from auto_tokenizer import auto_tokenize

load_dotenv()
token = os.getenv("HF_TOKEN")
if token:
    login(token=token)
    print("✅ Logged into Hugging Face")
else:
    print("⚠️ HF_TOKEN not found.")

text = "I love pizza"
models = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4o",
    "meta-llama/Meta-Llama-3-8B",
    "mistralai/Mistral-7B-Instruct",
    "tiiuae/falcon-7b-instruct",
    "google/gemma-7b-it",
]

for model in models:
    result = auto_tokenize(model, text)
    print(f"{result['model']:35} | {result['library']:12} | {result['n_tokens']:2} tokens | {result['tokens']}")
