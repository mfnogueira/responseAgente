import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do NLTK se ainda não tiverem sido baixados
nltk.download('stopwords')
nltk.download('punkt')

# Função para limpar o texto
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\W', ' ', text)
    return text

# Função para vetorizar o texto
def vectorize_texts(texts):
    stop_words = set(stopwords.words('english'))
    cleaned_texts = [' '.join([word for word in word_tokenize(clean_text(text)) if word not in stop_words]) for text in texts]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(cleaned_texts)
    return vectors, vectorizer.get_feature_names_out()

# Função para carregar os dados do CSV
def load_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    return data['review_text'].tolist()

# Função para salvar os vetores no MongoDB
def save_vectors_to_mongodb(vectors, feature_names, mongo_uri, db_name, collection_name):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Transformando a matriz esparsa em uma lista de dicionários
    vector_data = []
    for vector in vectors:
        vector_dict = {feature_names[i]: vector[i] for i in range(len(vector)) if vector[i] != 0}
        vector_data.append(vector_dict)
    
    # Inserindo os vetores no MongoDB
    collection.insert_many(vector_data)

# Caminho para o arquivo CSV
csv_file_path = 'path/to/your/reviews.csv'

# Carregando os dados do CSV
texts = load_data_from_csv(csv_file_path)

# Vetorizando os textos
vectors, feature_names = vectorize_texts(texts)

# Salvando os vetores no MongoDB
mongo_uri = 'your_mongo_uri'
db_name = 'your_db_name'
collection_name = 'your_collection_name'
save_vectors_to_mongodb(vectors, feature_names, mongo_uri, db_name, collection_name)
