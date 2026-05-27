# AGENTS.md

Guidance for future Codex work on this project.

## Project Intent

Build a small, clean FastAPI backend for a semantic notebook using PostgreSQL
and pgvector. Keep the MVP understandable and avoid premature complexity.

## Architecture Rules

- Keep business logic out of route handlers.
- Use services for workflows.
- Use repositories for database access.
- Keep embedding providers behind a small abstraction.
- Prefer async database access.
- Do not add microservices, Kubernetes, or background workers until the MVP is stable.

## Future Expansion Areas

- PDF ingestion
- OCR
- Chunking
- Hybrid keyword/vector search
- RAG chat
- Multi-user authentication
- Background workers
