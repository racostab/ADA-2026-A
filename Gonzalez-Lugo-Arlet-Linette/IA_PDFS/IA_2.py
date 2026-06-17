import os
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
URL2 = "http://100.113.158.78:11434/api/generate"
MODEL = "llama3.2"

def query_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def leer_articulo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def construir_prompt(texto):
    prompt = f"""
Eres un investigador experto en revisión de artículos científicos.

Analiza el siguiente artículo:

========================
ARTÍCULO:
========================

{texto}

========================
TAREAS:
========================

1. Resume el artículo
2. Identifica problemas no resueltos
3. Extrae la metodología (nombre y pasos)
4. Sugiere referencias adicionales

Sé claro, estructurado y académico.
"""
    return prompt

def main():
    carpeta = "TXT"
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".txt")]

    if len(archivos) == 0:
        print("No hay archivos .txt en la carpeta TXT")
        return

    print("\nAnalizando archivos automáticamente...\n")

    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)

        print(f"\n🔍 Procesando: {archivo}\n")

        texto = leer_articulo(ruta)
        prompt = construir_prompt(texto)

        resultado = query_ollama(prompt)

        print(f"\nRESULTADO PARA {archivo}:\n")
        print(resultado)
        print("\n" + "="*60)

if __name__ == "__main__":
    main()
