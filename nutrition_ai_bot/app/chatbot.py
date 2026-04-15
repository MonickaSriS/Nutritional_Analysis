from app.retriever import retrieve_context
from app.perplexity_client import ask_perplexity
from app.safety import apply_safety_filters

def nutrition_chatbot(query: str):
    if not apply_safety_filters(query):
        return "⚠️ I cannot provide medical prescriptions."

    context = retrieve_context(query)

    prompt = f"""
Use the following VERIFIED nutrition data to answer the question.

DATA:
{context}

QUESTION:
{query}

RULES:
- Answer only using the provided data
- If data is missing, say you don't know
- Do NOT give medical treatment advice
"""

    return ask_perplexity(prompt)
