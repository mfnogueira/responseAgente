# Use a imagem base oficial do Python
FROM python:3.12-slim

# Instale o Poetry
RUN pip install poetry==1.3.2

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de definição do Poetry
COPY pyproject.toml poetry.lock /app/

# Instale as dependências do Poetry
RUN poetry install --no-root

# Copie todo o código-fonte da aplicação
COPY . /app

# Execute a aplicação
CMD ["poetry", "run", "python", "responseagente/main.py"]
