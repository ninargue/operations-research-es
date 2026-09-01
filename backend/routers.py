import json
import os
import urllib.parse
import urllib.request

import anthropic
import resend
from fastapi import APIRouter, HTTPException
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


# ---------------------------------------------------------------------------
# Contacto
# ---------------------------------------------------------------------------

def _verify_recaptcha(token: str) -> bool:
    secret = os.environ.get("RECAPTCHA_SECRET_KEY", "")
    if not secret:
        return True
    data = urllib.parse.urlencode({"secret": secret, "response": token}).encode()
    req = urllib.request.Request("https://www.google.com/recaptcha/api/siteverify", data=data)
    with urllib.request.urlopen(req, timeout=5) as resp:
        result = json.loads(resp.read())
    return result.get("success", False) and result.get("score", 0) >= 0.5


def _es_ofensivo(mensaje: str) -> bool:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return False
    client = anthropic.Anthropic(api_key=api_key)
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=10,
        messages=[{
            "role": "user",
            "content": (
                "¿Es ofensivo, inapropiado o spam el siguiente mensaje? "
                "Responde solo 'sí' o 'no'.\n\n" + mensaje
            ),
        }],
    )
    return resp.content[0].text.strip().lower().startswith("sí")


class ContactoInput(BaseModel):
    nombre: str
    email: str
    mensaje: str
    recaptcha_token: str


@router.post("/contacto", tags=["Contacto"])
def contacto(data: ContactoInput):
    if not _verify_recaptcha(data.recaptcha_token):
        raise HTTPException(status_code=400, detail="Verificación de reCAPTCHA fallida")
    if _es_ofensivo(data.mensaje):
        raise HTTPException(status_code=400, detail="El mensaje no pudo ser enviado")
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
