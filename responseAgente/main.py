from response_agent.vetorizacao import vetorizar

def main():
    # Exemplo de uso da função vetorizar
    file_path = "caminho/para/seu/arquivo.csv"
    specialty = "reviews_intelligence"
    vetorizar(file_path, specialty)
    print("Vetorização concluída e dados salvos no MongoDB")

if __name__ == "__main__":
    main()
