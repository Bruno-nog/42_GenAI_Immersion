import os
import sys
from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def call_model():
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content


def list_phrases():
    phrases = [
    "O cachorro correu pelo parque atrás da bola azul.",
    "Ontem a bolsa de valores fechou em queda após anúncio do governo.",
    "O vulcão entrou em erupção, iluminando o céu noturno com lava.",
    "Aprender programação em Python pode abrir muitas portas no mercado de trabalho.",
    "O café recém-moído tem um aroma que desperta memórias da infância.",
    "Cientistas descobriram uma nova espécie de peixe em águas profundas.",
    "A final da Copa foi decidida nos pênaltis, com muita emoção na torcida.",
    "O conceito de buracos negros desafia nossa compreensão do espaço-tempo.",
    "O artista usou realidade aumentada para criar uma exposição interativa.",
    "A meditação diária ajuda a reduzir o estresse e aumentar a concentração."
    ]
    return phrases

def embeddings(query):
    phrases = list_phrases()
    query_embedding = model.encode(query)
    print(query_embedding)
    embeddings_phrases = model.encode(phrases)
    i = 0
    while i < len(phrases):
        phrase = phrases[i]
        embedding = embeddings_phrases[i]
        score = cosine_similarity([query_embedding], [embedding])[0][0]
        print(phrase, score)
        i += 1
    
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 embeddins.py <semantic>")
        sys.exit(1)
    query = sys.argv[1]
    embeddings(query)