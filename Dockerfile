# Utiliza uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala dependências (se houver requirements.txt, descomente a linha abaixo)
# RUN pip install -r requirements.txt

# Executa os testes automaticamente ao iniciar o container
CMD ["python", "-m", "unittest", "discover", "tests"] 