from fastapi import APIRouter
from pydantic import BaseModel
from solvers.mochila import resolver

router = APIRouter()


class MochilaInput(BaseModel):
    pesos: list[int]
    valores: list[int]
    capacidad: int


@router.post("/")
def mochila(data: MochilaInput):
    return resolver(data.pesos, data.valores, data.capacidad)
