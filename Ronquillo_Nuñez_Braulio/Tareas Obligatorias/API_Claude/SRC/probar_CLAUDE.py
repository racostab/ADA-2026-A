# API Para conectarse de forma remota a LLM (CLAUDE)
import os
import sys

import anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("No se encontro ANTHROPIC_API_KEY en el archivo .env")

prompt = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "Explica Gnome Sort y da un ejemplo corto en Python."
)

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=500,
    messages=[{"role": "user", "content": prompt}],
)

for block in message.content:
    if getattr(block, "type", None) == "text":
        print(block.text)
