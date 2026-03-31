import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def call_model(client):
    response = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": "algo"
            },
            {
                "role": "user",
                "content": "algo 2"
            },
            {
                "role": "assistant",
                "content": "algo 3"
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content

def chatbot():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    history = [
        {"role": "system", "content": "Você é um assistente útil."}
    ]
    while True:
        user_input = input("Q: ")
    call_model(client)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 chatbot.py")
        sys.exit(1)
    chatbot()