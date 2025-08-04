from fastapi import FastAPI
from desafio1.app.routers import upload, publications

app = FastAPI(
    title="Desafio 1 - API de Extração de Publicações do DOU",
    description="API para upload de arquivos ZIP contendo XMLs do DOU e publicação em AMQP",
    version="1.0.0"
)

# Rotas
app.include_router(upload.router)
app.include_router(publications.router)

@app.get("/")
def root():
    return {"message": "API do Desafio 1 está funcionando!"}
