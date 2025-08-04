# Desafio 1

## Requisitos

- Python 3.13
- Docker
- RabbitMQ

## Como executar com Docker

1. Construa a imagem:

   ```bash
   docker build -t desafio-api .
   ```

2. Execute o container:

   ```bash
   docker run -p 8000:8000 desafio-api uvicorn desafio1.app.main:app --host 0.0.0.0 --port 8000
   ```

## Endpoints

- `POST /upload/` → Faz upload de arquivo ZIP e processa XMLs.
- `GET /publications/` → Lista publicações extraídas.

## Publicação em AMQP

Mensagens são publicadas na fila configurada por `AMQP_QUEUE`.
