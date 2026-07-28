from ollama import chat


def ask_llm(question, results):
    context = ""

    for result in results:
        context += f"(Page {result['page']})\n"
        context += result["text"] + "\n\n"

    prompt = f"""
You are answering questions ONLY using the provided PDF.

If the answer is not in the context, reply:
"I couldn't find that information in the document."

Context:
{context}

Question:
{question}
"""

    response = chat(
        model="qwen3:8b",
        think=False,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content