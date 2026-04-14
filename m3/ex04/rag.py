import os
import sys
import pickle
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def rag(question):
    with open("orbit_motordrones.txt", 'r') as file:
        lines = file.readlines()
        i = 1
        for line in lines:
            print(f"index {i}: {line}")
            i += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 rag.py <orbit family>")
        sys.exit(1)
    question = sys.argv[1]
    rag(question)