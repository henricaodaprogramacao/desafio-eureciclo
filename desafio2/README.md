# Desafio 2

Este projeto resolve o problema de encontrar a melhor combinação de garrafas para preencher um galão de forma otimizada, com base no volume informado.  
A aplicação foi desenvolvida em Python e pode ser executada totalmente dentro de um container Docker.

---

## Estrutura do projeto

```
desafio-eureciclo/
│
├── desafio2/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── logic.py
│   ├── tests/
│   │   └── test_logic.py
│   └── README.md
│
├── .github/workflows/
│   └── pipeline.yml
│
├── Dockerfile
├── requirements.txt
└── .dockerignore
```

---

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado na máquina.

---

## Como construir a imagem

No diretório raiz do projeto, execute:

```bash
docker build -t desafio-galao .
```

---

## Como executar a aplicação

Para rodar a aplicação e calcular a melhor combinação de garrafas:

```bash
docker run --rm desafio-galao python -m desafio2.app.main --galao 7 --garrafa 4.5 --garrafa 1.5
```

### Exemplo de saída:

```
Melhor combinação: [4.5, 1.5]
Sobra: 1.0
```

> Os valores de `--galao` e `--garrafa` podem ser alterados conforme necessário.  
> É possível passar várias opções de `--garrafa`.

---

## Como executar os testes

Para rodar os testes unitários:

```bash
docker run --rm desafio-galao pytest
```

Isso executará todos os testes localizados na pasta `tests/`.

---

## Pipeline de Integração Contínua (CI)

O workflow no GitHub Actions (`.github/workflows/pipeline.yml`) realiza automaticamente:

1. Build da imagem Docker.
2. Execução dos testes unitários.

---

## Tecnologias utilizadas

- Python 3.13
- Docker
- Pytest

---

## Autor

Desenvolvido por Henrique
