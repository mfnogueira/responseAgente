import os
from pymongo import MongoClient

def get_mongo_client():
    mongo_uri = os.getenv("MONGO_URI")
    return MongoClient(mongo_uri)

def get_mongo_db():
    client = get_mongo_client()
    db_name = os.getenv("MONGO_DB")
    return client[db_name]

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def vetorizar(file_path, specialty):
    ext = os.path.splitext(file_path)[-1].lower()
    vector_store_path = f"data/{specialty}/vectorstore"
    ensure_directory_exists(os.path.dirname(vector_store_path))
    if ext == ".csv":
        vetorizar_csv(file_path, vector_store_path)
    elif ext == ".pdf":
        vetorizar_pdf(file_path, vector_store_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def vetorizar_csv(file_path, vector_store_path):
    # Implementação da vetorização para CSV
    pass

def vetorizar_pdf(file_path, vector_store_path):
    # Implementação da vetorização para PDF
    pass
