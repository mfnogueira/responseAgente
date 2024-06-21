# Response Agent

## Descrição

Este projeto utiliza agentes especializados para processar dados em diferentes domínios e gerar relatórios.

## Como usar

1. Configure suas variáveis de ambiente no arquivo `.env`.
2. Construa e inicie o contêiner Docker:

   ```bash
   docker-compose build
   docker-compose up

response_agent/
├── __init__.py
├── agente.py
├── gerente.py
├── main.py
├── utils.py
├── vetorizacao.py
data/
tests/
.venv/
.env
.gitignore
.python-version
poetry.lock
pyproject.toml
README.md
# responseAgente
