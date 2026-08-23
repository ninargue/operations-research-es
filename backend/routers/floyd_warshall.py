from fastapi import APIRouter
from pydantic import BaseModel
from solvers.floyd_warshall import resolver

router = APIRouter()


class FloydInput(BaseModel):
    matriz: list[list[float]]


@router.post("/")
def floyd_warshall(data: FloydInput):
    return resolver(data.matriz)
