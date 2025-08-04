# Imagem base com Python
FROM python:3.13-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código para dentro da imagem
COPY . .

# Comando padrão para executar o desafio 2 (pode ser alterado conforme o projeto)
CMD ["python", "desafio2/app/main.py"]
