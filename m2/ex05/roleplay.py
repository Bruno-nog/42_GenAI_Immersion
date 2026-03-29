import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def country_locations(prompt):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": "Você é um consultor de viagens especializado. "
                "Sempre responda com as 5 melhores atrações do destino solicitado. "
                "Responda apenas com uma lista numerada, sem explicações.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 roleplay.py 'Country'")
        sys.exit(1)
    prompt = sys.argv[1]
    country_locations(prompt)