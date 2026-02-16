# Assignment 1 – AI Text Transformer (StrOutputParser)

## 📌 Objective
Build a text transformation pipeline using a language model, custom prompts, and StrOutputParser.

The application accepts a paragraph as input and returns:
1. A short summary (3–4 lines)
2. The detected tone (Formal / Casual / Technical)
3. An improved version of the paragraph

---

## 🛠 Technologies Used

- Python
- LangChain (LCEL)
- Ollama (Local LLM)
- Llama 3.1 model

---

## 🧠 How It Works

This project uses:

- `PromptTemplate` to structure the instructions
- `ChatOllama` to connect to the local Llama 3.1 model
- `StrOutputParser` to ensure the output is returned as a plain string
- LCEL chaining (`prompt | model | parser`) for clean pipeline execution

Pipeline Flow:

User Input → PromptTemplate → LLM (Llama 3.1) → StrOutputParser → Final Output

---

## 📦 Installation

### 1️⃣ Install Ollama
Download from:
https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.1
