from fastapi import APIRouter
from pydantic import BaseModel
from solvers.cambio_monedas import resolver

router = APIRouter()


class CambioInput(BaseModel):
    monedas: list[int]
    monto: int


@router.post("/")
def cambio_monedas(data: CambioInput):
    return resolver(data.monedas, data.monto)
