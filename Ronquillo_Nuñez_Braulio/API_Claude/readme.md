# API_Claude

API local desarrollada con **FastAPI** para consumir **Claude** desde Python y exponer un endpoint HTTP similar a la idea de una API de modelos LLM.

---

## Objetivo

Construir una API propia que reciba un prompt por HTTP, consulte Claude mediante la API oficial de Anthropic y devuelva la respuesta en formato JSON.

---

## Arquitectura

```text
Cliente → FastAPI → Claude (Anthropic) → Respuesta JSON
```

### Componentes

| Componente | Descripción |
|---|---|
| **Cliente** | Swagger, curl, Postman, script Python o cualquier app HTTP |
| **FastAPI** | Recibe la petición, valida el body JSON y ejecuta la llamada a Claude |
| **Claude / Anthropic SDK** | Envía el prompt al modelo y devuelve la respuesta |
| **Archivo `.env`** | Guarda la `ANTHROPIC_API_KEY` para autenticar las solicitudes |

---

## Estructura del proyecto

```
API_Claude/
├─ .venv/
├─ .env
├─ api.py
├─ body.json
├─ README.md
└─ .gitignore
```

---

## Requisitos

- Windows
- Python 3.10 o superior
- Git Bash o PowerShell
- API key de Anthropic

---

## Instalación

**1. Ubícate en la carpeta del proyecto:**

```bash
cd ~/Desktop/Proyectos\ primer\ semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/API_Claude
```

**2. Crea el entorno virtual:**

```bash
python -m venv .venv
```

**3. Activa el entorno virtual (Git Bash):**

```bash
source .venv/Scripts/activate
```

**4. Instala las dependencias:**

```bash
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn anthropic python-dotenv requests
```

---

## Configuración de variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
ANTHROPIC_API_KEY=TU_API_KEY
```

---

## Archivo principal `api.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import anthropic
import os
import traceback

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("No se encontró ANTHROPIC_API_KEY en el archivo .env")

client = anthropic.Anthropic(api_key=api_key)

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str
    model: str = "claude-sonnet-4-5"
    max_tokens: int = 300


@app.get("/health")
def health():
    return {"ok": True, "servicio": "API Claude"}


@app.post("/api/chat")
def chat(req: ChatRequest):
    try:
        message = client.messages.create(
            model=req.model,
            max_tokens=req.max_tokens,
            messages=[
                {"role": "user", "content": req.prompt}
            ],
        )

        texto = ""
        for block in message.content:
            if getattr(block, "type", None) == "text":
                texto += block.text

        return {
            "model": req.model,
            "response": texto
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")
```

---

## Cómo ejecutar la API

Levanta el servidor con:

```bash
python -m uvicorn api:app --reload
```

> **`api:app`** — `api` es el nombre del archivo `api.py` y `app` es la instancia de `FastAPI()`.

La API quedará disponible en:

```
http://127.0.0.1:8000
```

---

## Endpoints disponibles

### `GET /health` — Health check

Verifica que el servicio está corriendo.

**Respuesta esperada:**

```json
{
  "ok": true,
  "servicio": "API Claude"
}
```

---

### `POST /api/chat` — Chat con Claude

Envía un prompt y recibe la respuesta generada por Claude.

**Body esperado:**

```json
{
  "prompt": "Explica qué es una API REST en 3 líneas",
  "model": "claude-sonnet-4-5",
  "max_tokens": 200
}
```

**Respuesta esperada:**

```json
{
  "model": "claude-sonnet-4-5",
  "response": "..."
}
```

---

## Uso desde Swagger

FastAPI genera documentación interactiva automáticamente en:

```
http://127.0.0.1:8000/docs
```

Desde ahí puedes:

1. Abrir `POST /api/chat`
2. Seleccionar **Try it out**
3. Enviar un JSON de prueba
4. Ver la respuesta generada por Claude

**Ejemplo de body:**

```json
{
  "prompt": "Hola Claude, dame una definición corta de API",
  "model": "claude-sonnet-4-5",
  "max_tokens": 200
}
```

---

## Uso desde consola

**`body.json`:**

```json
{
  "prompt": "Hola Claude, dame una definición corta de API",
  "model": "claude-sonnet-4-5",
  "max_tokens": 200
}
```

**Comando curl:**

```bash
curl -X POST "http://127.0.0.1:8000/api/chat" \
  -H "Content-Type: application/json" \
  --data-binary @body.json
```

---

## Flujo de operación

```
1. Cliente envía POST a /api/chat
2. FastAPI valida el JSON recibido
3. Se extraen: prompt, model y max_tokens
4. Se realiza la llamada a Claude con el SDK de Anthropic
5. Claude genera la respuesta
6. La API devuelve un JSON con el modelo usado y el texto generado
```

---

## Ejemplo de uso completo

```bash
# 1. Activar entorno virtual
source .venv/Scripts/activate

# 2. Levantar el servidor
python -m uvicorn api:app --reload

# 3. Abrir Swagger en el navegador
#    http://127.0.0.1:8000/docs

# 4. Probar POST /api/chat con el body:
# {
#   "prompt": "Explica qué es una API REST en 3 líneas",
#   "model": "claude-sonnet-4-5",
#   "max_tokens": 200
# }

# 5. Respuesta obtenida:
# {
#   "model": "claude-sonnet-4-5",
#   "response": "..."
# }
```

---

## Archivos de soporte recomendados

**`.gitignore`:**

```
.env
.venv/
__pycache__/
```

---

## Autor

**Braulio Ronquillo Núñez**
