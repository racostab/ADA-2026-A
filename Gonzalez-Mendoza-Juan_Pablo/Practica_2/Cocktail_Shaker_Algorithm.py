
"""
Created on wed Apr 15 08:28:51 2026

@author: jp
"""

import ollama
import os

client = ollama.Client(host='http://localhost:11434')

prompt = """
Escribe una implementación en Python del algoritmo Cocktail Shaker Sort.
El código debe incluir:
1. Una función `cocktail_shaker_sort(arr)` que ordene una lista in-place y retorne la lista ordenada.
2. Una función `cocktail_shaker_sort_verbose(arr)` que retorne un diccionario con:
   - 'sorted': la lista ordenada
   - 'comparisons': número total de comparaciones
   - 'swaps': número total de intercambios
   - 'passes': número de pasadas realizadas
3. Comentarios explicando cada parte del algoritmo.
4. NO incluyas código de prueba, solo las funciones.

Responde ÚNICAMENTE con el código Python, sin texto adicional ni bloques markdown.
"""

print("Generando código Cocktail Shaker Sort con Ollama...")
print("-" * 50)

response = client.generate(
    model='mistral:latest',
    prompt=prompt,
    options={
        'temperature': 0.2,
        'top_p': 0.9,
    }
)

code = response.response.strip()

if code.startswith("```"):
    lines = code.split("\n")
    code = "\n".join(lines[1:-1]) if lines[-1] == "```" else "\n".join(lines[1:])

output_path = "cocktail_sort.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(code)

print(code)
print("-" * 50)
print(f"\nCódigo guardado en: {os.path.abspath(output_path)}")
