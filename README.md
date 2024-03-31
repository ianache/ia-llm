# IA con LLM (LangChain y ollama)


## Instalar ollama

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

## Instalar Librerias Python

```sh
python3 -m pip install -r requirements.txt
```

## Generar BD PostgreSQL + pgvector

```sh
docker compose up -d
```

## Generar Base de Conocimientos (embeddings)

> El conocimiento se debe ubicar en archivos en el folder `kb`

```sh
python3 01-embedding.py
```

## Consultas al LLM

```sh
python3 02-question.py
```

> Autor: Ilver Anache (IA)
