#!/bin/bash

# Create root folder
mkdir -p rag-app/app

# Create main files
touch requirements.txt .env

# Create app-level files
touch app/main.py
touch app/config.py
touch .gitignore
touch setup.py

# Create ingestion module
mkdir -p app/ingestion
touch app/ingestion/loader.py
touch app/ingestion/chunker.py
touch app/ingestion/embedder.py
touch app/ingestion/upsert.py

# Create retrieval module
mkdir -p app/retrieval
touch app/retrieval/query_embed.py
touch app/retrieval/search.py
touch app/retrieval/prompt.py

# Create services module
mkdir -p app/services
touch app/services/llm.py

# Create API module
mkdir -p app/api
touch app/api/routes.py

# Optional: create __init__.py files (important for Python imports)
touch app/__init__.py
touch app/ingestion/__init__.py
touch app/retrieval/__init__.py
touch app/services/__init__.py
touch app/api/__init__.py

echo "✅ RAG project structure created successfully!"