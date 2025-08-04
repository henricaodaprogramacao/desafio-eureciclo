FROM python:3.12-slim

# Criar diretório da aplicação
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicação
COPY . .

# Comando padrão
CMD ["python", "app/main.py"]