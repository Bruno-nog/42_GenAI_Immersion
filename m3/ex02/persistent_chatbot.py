import os
import sys
from groq import Groq
from dotenv import load_dotenv
import sqlite3
load_dotenv()


def call_model(client, messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content


def database_storage(role, content):
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL)""")
    
    cursor.execute("""INSERT INTO messages
                    (role, content) VALUES 
                    (?, ?)
    """, (role, content))
    cursor.execute("""SELECT * FROM messages ORDER BY id DESC LIMIT 10""")
    rows = cursor.fetchall()
    connection.commit()
    return rows

def get_messages(rows):
    messages = []

    for row in rows:
        role = row[1]
        content = row[2]
        msg = {"role": role, "content": content}
        messages.append(msg)
    return messages


def get_all_messages():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()
    connection.close()
    messages = []
    for row in rows:
        messages.append({"role": row[1], "content": row[2]})
    return messages

def persistent_chatbot():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    while True:
        user_input = input("G: ")
        if user_input == "bye":
            print("bye bye")
            break
        rows = database_storage("user", user_input)
        messages = get_messages(rows)
        messages.reverse()
        all_messages = get_all_messages()
        total_messages = len(all_messages)
        interactions = total_messages // 2
        if interactions % 2 == 0 and interactions != 0:
            old_messages = all_messages[:-5]
            text = ""
            for msg in old_messages:
                text += f"{msg['role']}: {msg['content']}\n"
            summary_prompt = [
                {"role": "system", "content": "Você resume conversas de forma curta."},
                {"role": "user", "content": f"Resuma essa conversa :\n{text}"}
            ]
            summary = call_model(client, summary_prompt)
            print("\n[RESUMO GERADO]:", summary, "\n")
            continue
        answer = call_model(client, messages[-5:])
        print("A:", answer)
        database_storage("assistant", answer)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 persistent_chatbot.py")
        sys.exit(1)
    persistent_chatbot()