import os
import sys
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def call_model(client, messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content

def chatbot():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    history = [
        {"role": "system", "content": "Você é um assistente útil."}
    ]
    while True:
        user_input = input("Q: ")
        if user_input == "bye":
            break
        history.append({"role": "user", "content": user_input})
        MAX_MESSAGES = 11
        messages = history[-MAX_MESSAGES:]
        answer = call_model(client, messages)

        print("A:", answer)
        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 chatbot.py")
        sys.exit(1)
    chatbot()