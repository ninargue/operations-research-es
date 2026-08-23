from fastapi import APIRouter
from pydantic import BaseModel
from solvers.distancia_edicion import resolver

router = APIRouter()


class DistanciaInput(BaseModel):
    cadena_origen: str
    cadena_destino: str


@router.post("/")
def distancia_edicion(data: DistanciaInput):
    return resolver(data.cadena_origen, data.cadena_destino)
