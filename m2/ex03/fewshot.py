import sys
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def generate_response(prompt):
    examples = """
    Traduza termos técnicos de informática.
    Responda apenas com a tradução, sem explicações.

    SQL → linguagem de consulta estruturada
    HTML → linguagem de marcação de hipertexto
    CPU → unidade central de processamento
    CSS → folhas de estilo em cascata
    """
    prompt_final = examples + "\n" + prompt + " →"
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": prompt_final,
        }
    ],
    model="llama-3.3-70b-versatile",
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fewshot.py <prompt>")
        sys.exit(1)
    prompt = sys.argv[1]
    generate_response(prompt)