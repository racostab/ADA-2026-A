from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import anthropic
import os

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
            messages=[{"role": "user", "content": req.prompt}],
        )

        texto = ""
        for block in message.content:
            if getattr(block, "type", None) == "text":
                texto += block.text

        return {"model": req.model, "response": texto}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
