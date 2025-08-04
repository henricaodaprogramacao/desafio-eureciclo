# Desafio 2

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado na máquina.

---

## Como executar com Docker

1. Construa a imagem:

   ```bash
   docker build -t desafio-galao .
   ```

2. Execute o container:

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
