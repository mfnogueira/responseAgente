import os
import pandas as pd
from .utils import get_mongo_db

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def vetorizar_csv(file_path):
    # Lê o CSV e converte para vetores
    df = pd.read_csv(file_path)
    vectors = df.to_dict(orient="records")
    return vectors

def vetorizar_pdf(file_path):
    # Implementação fictícia de leitura de PDF e vetorização
    # Substitua com a lógica real de leitura e vetorização de PDFs
    vectors = [{"content": "Example PDF content"}]  # Exemplo fictício
    return vectors

def vetorizar(file_path, specialty):
    ext = os.path.splitext(file_path)[-1].lower()
    db = get_mongo_db()
    collection = db[specialty]
    
    if ext == ".csv":
        vectors = vetorizar_csv(file_path)
    elif ext == ".pdf":
        vectors = vetorizar_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
    # Salva os vetores no MongoDB
    collection.insert_many(vectors)
