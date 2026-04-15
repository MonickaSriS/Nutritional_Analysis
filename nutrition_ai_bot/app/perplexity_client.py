import os
import requests

API_KEY = os.getenv("PERPLEXITY_API_KEY")

URL = "https://api.perplexity.ai/chat/completions"

def ask_perplexity(prompt):
    if not API_KEY:
        raise RuntimeError("PERPLEXITY_API_KEY not set")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are a nutrition expert AI."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(URL, headers=headers, json=payload)

    # DEBUG LINE (temporary)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
