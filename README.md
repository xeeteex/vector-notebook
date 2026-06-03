# Hybrid Notebook  
 uv run uvicorn app.main:app --reload

Hybrid Notebook is an AI-powered semantic notebook application.

The MVP goal is to let users save notes, generate vector embeddings for those
notes, and search them semantically using PostgreSQL with the pgvector
extension.

## Planned Stack

- Backend: Python, FastAPI
- Database: PostgreSQL
- Vector search: pgvector
- ORM: SQLAlchemy
- Migrations: Alembic
- Embeddings: OpenAI embeddings behind an abstraction layer
- Dependency management: uv
- Containers: Docker and Docker Compose
- Frontend: placeholder only for the MVP

## MVP Scope

- Notes CRUD API
- Store note embeddings in PostgreSQL
- Semantic similarity search with configurable `top_k`
- Clean service and repository layers
- Versioned API structure
- Docker-based local development

## Architecture Direction

This project should stay a modular monolith for the MVP. Routes should only
handle HTTP concerns, services should contain business workflows, repositories
should contain database access, and embedding providers should stay replaceable.

Future features may include document ingestion, chunking, OCR, hybrid search,
RAG chat, background workers, and multi-user authentication.
