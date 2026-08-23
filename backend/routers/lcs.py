from fastapi import APIRouter
from pydantic import BaseModel
from solvers.lcs import resolver

router = APIRouter()


class LCSInput(BaseModel):
    cadena_a: str
    cadena_b: str


@router.post("/")
def lcs(data: LCSInput):
    return resolver(data.cadena_a, data.cadena_b)
