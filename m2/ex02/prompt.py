import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def get_api_ai(prompt, temperature):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=temperature,
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python3 prompt.py <prompt> [temperature]")
        sys.exit(1)
    temperature = 0.5
    prompt = sys.argv[1]
    if len(sys.argv) == 3:
        try:
            temperature = float(sys.argv[2])
        except:
            print("temperature must be a number")
            sys.exit(1)
        if temperature > 2.0 or temperature < 0.0:
            print("temperature must be between 0.0 and 2.0")
            sys.exit(1)
    get_api_ai(prompt, temperature)