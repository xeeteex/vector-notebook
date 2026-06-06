from fastapi import FastAPI
from sqlalchemy import text

app = FastAPI(title= "Hybrid Notebook API")

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}