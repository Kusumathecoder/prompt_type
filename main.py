from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.1",
    temperature=0.3
)

prompt = PromptTemplate(
    input_variables=["input_text"],
    template="""
You are an AI text transformation assistant.

Given the paragraph below, complete all tasks.

Paragraph:
{input_text}

Tasks:
1. Write a short summary (3-4 lines).
2. Identify the tone (Formal / Casual / Technical).
3. Rewrite the paragraph with improved clarity and structure.

Important:
- Do NOT add extra explanations.
- Do NOT use bold text or markdown.
- Do NOT say "Here is the output".
- Return only the structured result exactly as shown below.

Summary:
<summary>

Tone:
<formal / casual / technical>

Improved Version:
<improved paragraph>
"""
)


parser = StrOutputParser()

chain = prompt | model | parser

if __name__ == "__main__":
    user_input = input("Enter a paragraph:\n\n")
    result = chain.invoke({"input_text": user_input})

    print("\n--- AI Text Transformer Output ---\n")
    print(result)
