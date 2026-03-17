import os
import sys
from groq import Groq

def get_api_ai(prompt, temperature):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    mangoloko = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=temperature,
    )
    print(mangoloko.choices[0].message.content)

if __name__ == "__main__":
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Needs a prompt")
        sys.exit(1)
    # float(temperature) == 0.5
    prompt = sys.argv[1]
    if len(sys.argv) == 3:
        temperature = float(sys.argv[2])
    print(temperature)
    get_api_ai(prompt, temperature)
    print(temperature)
