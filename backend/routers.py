import os
import resend
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
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


# ---------------------------------------------------------------------------
# Contacto
# ---------------------------------------------------------------------------

class ContactoInput(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str


@router.post("/contacto", tags=["Contacto"])
def contacto(data: ContactoInput):
    api_key = os.environ.get("RESEND_API_KEY")
    dest = os.environ.get("CONTACT_EMAIL")
    if not api_key or not dest:
        raise HTTPException(status_code=503, detail="Servicio de contacto no configurado")
    resend.api_key = api_key
    resend.Emails.send({
        "from": "contacto@resend.dev",
        "reply_to": data.email,
        "to": dest,
        "subject": f"Mensaje de {data.nombre} — Operations Research ES",
        "text": f"Nombre: {data.nombre}\nEmail: {data.email}\n\n{data.mensaje}",
    })
    return {"ok": True}


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
