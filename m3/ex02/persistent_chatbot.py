import os
import sys
from groq import Groq
from dotenv import load_dotenv
import sqlite3
load_dotenv()



# def call_model(client, messages):
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=messages
#     )
#     return response.choices[0].message.content


def database_summaries(user_input):
    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS bank_accounts (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL)""")
    
    # cursor.execute("""UPDATE bank_accounts
    #                     SET role = {client}
    #                     SET content = {user_input}""")
    cursor.execute("""INSERT INTO bank_accounts
                    (role, content) VALUES 
                    (?, ?)
    """, ('user', user_input))
    cursor.execute("""SELECT * FROM bank_accounts""")
    accounts = cursor.fetchall()
    print(accounts)
    connection.commit()

def persistent_chatbot():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    while True:
        user_input = input("G: ")
        if user_input == "bye":
            print("bye bye")
            break
        database_summaries(user_input)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 persistent_chatbot.py")
        sys.exit(1)
    persistent_chatbot()