from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import mochila, cambio_monedas, lcs, distancia_edicion, floyd_warshall

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

app.include_router(mochila.router, prefix="/mochila", tags=["Mochila 0/1"])
app.include_router(cambio_monedas.router, prefix="/cambio-monedas", tags=["Cambio de Monedas"])
app.include_router(lcs.router, prefix="/lcs", tags=["LCS"])
app.include_router(distancia_edicion.router, prefix="/distancia-edicion", tags=["Edit Distance"])
app.include_router(floyd_warshall.router, prefix="/floyd-warshall", tags=["Floyd-Warshall"])


@app.get("/health")
def health():
    return {"status": "ok"}
