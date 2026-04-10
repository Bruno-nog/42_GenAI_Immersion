import os
import sys
from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
load_dotenv()

def call_model():
    response = client.chat.completions.create(
        model="paraphrase-multilingual-MiniLM-L12-v2"
        messages=messages
    )
    return response.choices[0].message.content


def embeddings(semantic_word):


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 embeddins.py <semantic>")
        sys.exit(1)
    semantic_word = sys.argv[1]
    embeddings(semantic_word)