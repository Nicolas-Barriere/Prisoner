import os
import openai
import httpx
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def format_prompt(history):
    return (
        "Tu joues au dilemme du prisonnier et tu veux gagner un tournoi où tu vas affronter beaucoup d'autres personnes. Le gagnant est celui qui aura le plus de points. Historique des décisions précédentes (C = coopérer, D = trahir) : "
        + ", ".join(history)
        + "\nTa prochaine décision (C ou D) ? Réponds uniquemenet la lettre C ou D et rien d'autre"
    )

def gpt_decision(history):
    prompt = format_prompt(history)
    response = openai.chat.completions.create(
        model="o3-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip().upper()[0]

def mistral_decision(history):
    prompt = format_prompt(history)
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    payload = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 1,
    }
    with httpx.Client() as client:
        response = client.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers=headers,
            json=payload,
        )
        return response.json()["choices"][0]["message"]["content"].strip().upper()[0]
