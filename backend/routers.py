from fastapi import APIRouter
from pydantic import BaseModel
from solvers import balanceo_de_linea

router = APIRouter()


# ---------------------------------------------------------------------------
# Balanceo de Línea de Ensamblaje
# ---------------------------------------------------------------------------

class BalanceoInput(BaseModel):
    tiempos: list[int]
    nombres: list[str]
    num_estaciones: int
    precedencias: list[tuple[int, int]]
    incompatibilidades: list[tuple[int, int]] | None = None
    limite_espacio: list[int] | None = None
    espacio: list[int] | None = None


@router.post("/balanceo-linea", tags=["Balanceo de Línea"])
def balanceo_linea(data: BalanceoInput):
    return balanceo_de_linea.resolver(
        tiempos=data.tiempos,
        nombres=data.nombres,
        num_estaciones=data.num_estaciones,
        precedencias=data.precedencias,
        incompatibilidades=data.incompatibilidades,
        limite_espacio=data.limite_espacio,
        espacio=data.espacio,
    )
