from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router

app = FastAPI(
    title="Operations Research API",
    description="API de modelos de Investigación de Operaciones",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ninargue.github.io"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}
