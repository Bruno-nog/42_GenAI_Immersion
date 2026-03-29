import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def summarize_text(prompt):
    examples = """
    Resuma o texto em no máximo 20 palavras.

    responda com apenas o resumo do texto, sem explicações.

    texto → "Durante a Idade Média, as universidades europeias surgiram como centros de
    conhecimento, reunindo estudiosos de diversas áreas. Elas desempenharam papel essencial na
    preservação e transmissão de saberes clássicos, além de estimular debates filosóficos e
    científicos que moldaram o pensamento ocidental e prepararam terreno para o Renascimento."

    resumo → Universidades medievais preservaram saber clássico, promoveram debates e criaram base
    intelectual que impulsionou o Renascimento europeu
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
        print("Usage: python3 xml.py 'text'")
        sys.exit(1)
    prompt = sys.argv[1]
    summarize_text(prompt)