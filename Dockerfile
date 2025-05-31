# Utiliza uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install -r requirements.txt

# Comando para executar os testes com cobertura
CMD ["pytest", "tests/", "-v", "--cov=src", "--cov-report=term-missing"] 