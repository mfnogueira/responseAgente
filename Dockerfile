# Use uma imagem oficial do Python como a base
FROM python:3.12-slim

# Instale o Poetry
RUN pip install poetry==1.3.2

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock /app/

# Instale as dependências do Poetry sem criar um ambiente virtual
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copie o restante do código do aplicativo
COPY . /app

# Defina o comando padrão para iniciar o Streamlit
CMD ["streamlit", "run", "streamlit_app.py"]
