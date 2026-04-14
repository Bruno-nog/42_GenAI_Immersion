import os
import sys
import pickle
from groq import Groq
from dotenv import load_dotenv
load_dotenv()



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 rag.py <orbit family>")
        sys.exit(1)
    rag = sys.argv[1]
