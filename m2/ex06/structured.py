import os
import sys
import json
from pydantic import BaseModel, ValidationError
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class Person(BaseModel):
    nome: str
    idade: int
    profissão: str
    cidade: str

def validating_json(content):
    try:
        data = json.loads(content)
        person = Person.model_validate(data)
        print(person.model_dump_json(ensure_ascii=False))
    except json.JSONDecodeError:
        print("Error: response is not a valid JSON")
    except ValidationError as e:
        print("Validation error")
        print(e)

def formatting_json(prompt):
    examples = """
    Extraia nome, idade, profissão e cidade do texto e responda APENAS em JSON válido.
    Responda com apenas o JSON válido, sem explicações.

    exemplo → "João Silva, 35 anos, é engenheiro e mora em São Paulo"
    {"nome": "João Silva",
    "idade": 35,
    "profissão": "engenheiro",
    "cidade": "São Paulo"}
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
        model="llama-3.3-70b-versatile"
    )
    content = response.choices[0].message.content
    validating_json(content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 structured.py ")
        sys.exit(1)
    prompt = sys.argv[1]
    formatting_json(prompt)