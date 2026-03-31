import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def call_model(client, prompt):
    response = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content

def prompt_chaining(prompt):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    # calls = call_model(client, "algum prompt")
    prompt1 = f"""
    Transforme a descrição abaixo em um texto mais detalhado e persuasivo:
    {prompt}
    """

    step1 = call_model(client, prompt1)

    prompt2 = f"""
    Com base no texto abaixo, crie um anúncio publicitário curto e criativo:
    {step1}
    """

    step2 = call_model(client, prompt2)

    prompt3 = f"""
    Traduza o texto abaixo para o inglês:
    {step2}
    """

    step3 = call_model(client, prompt3)

    print(step1)
    print("---")
    print(step2)
    print("---")
    print(step3)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 chaining.py ")
        sys.exit(1)
    prompt = sys.argv[1]
    prompt_chaining(prompt)