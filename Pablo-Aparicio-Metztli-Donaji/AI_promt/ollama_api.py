import os
import re
import subprocess
import sys

import ollama

def clean_code_output(text: str) -> str:
    """Quita fences ``` y recorta explicaciones típicas al final."""
    text = text.strip()

    # Bloque markdown ```lang ... ``` o ``` ... ```
    m = re.search(r"^```(?:\w+)?\s*\n(.*)\n```\s*$", text, re.DOTALL)
    if m:
        return m.group(1).strip()

    m = re.search(r"```(?:\w+)?\s*\n(.*?)```", text, re.DOTALL)
    if m:
        text = m.group(1).strip()

    for marker in (
        "\n\nExplicación",
        "\n\nExplanation",
        "\n\nNota:",
        "\n\nNote:",
        "\n\nEste código",
        "\n\nThis code",
        "\n\nAquí",
        "\n\nHere ",
    ):
        if marker in text:
            text = text.split(marker, 1)[0].rstrip()

    return text.strip()


SYSTEM = (
    "Eres un compilador de código: tu salida es ÚNICAMENTE el código fuente pedido. "
    "Sin markdown, sin ```, sin texto antes o después, sin comentarios ni docstrings."
)

USER = (
    "Selection sort en Python 3. Solo el código (por ejemplo una función que ordene una lista de números)."
)

response = ollama.generate(
    model="deepseek-coder",
    system=SYSTEM,
    prompt=USER,
    options={
        "temperature": 0.15,
        # Corta si empieza a añadir explicación
        "stop": ["\n\nExplicación", "\n\nExplanation", "\n\nNota:", "\n\nNote:"],
    },
)

codigo = clean_code_output(response["response"])

print(codigo)

_script_dir = os.path.dirname(os.path.abspath(__file__))
_temp_path = os.path.join(_script_dir, "temp.py")

with open(_temp_path, "w", encoding="utf-8") as f:
    f.write(codigo)

resultado = subprocess.run(
    [sys.executable, _temp_path],
    capture_output=True,
    text=True,
    cwd=_script_dir,
)

print("Salida:")
print(resultado.stdout)

print("Errores:")
print(resultado.stderr)
