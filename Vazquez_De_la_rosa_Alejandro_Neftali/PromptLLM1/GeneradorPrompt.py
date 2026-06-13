import requests
import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURACIÓN GENERAL ---
NUM_PROGRAMAS = 5
ALGORITMO = "Comb Sort"
FUNCION_NOMBRE = "comb_sort"

PROMPT = f"""
Proporciona solamente el código de una función en Python para el algoritmo {ALGORITMO}.
La función debe llamarse estrictamente "{FUNCION_NOMBRE}(arr)" y recibir una lista de números.
No incluyas explicaciones, no incluyas comentarios, ni marcas de markdown.
Devuelve unicamente el código ejecutable.
"""

def generar_grok_api(prompt):
    api_key = os.getenv("XAI_API_KEY")
    url = "https://api.x.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "grok-4.20-0309-reasoning",
        "messages": [
            {"role": "system", "content": "Eres un compilador. Devuelve solo código puro en Python sin markdown."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7 
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            contenido = response.json()['choices'][0]['message']['content']
            return contenido.replace("```python", "").replace("```", "").strip()
        else:
            print(f"Error HTTP Grok: {response.status_code}")
    except Exception as e:
        print(f"Error de conexión con Grok API: {e}")
    return None

def generar_qwen_tailscale(prompt):
    # Apuntando al servidor del profesor
    url = "http://100.113.158.78:11434/api/generate"
    payload = {
        "model": "qwen3:4B", # No se tiene Grok se usa qwen en su lugar
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.7}
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            contenido = response.json()["response"]
            return contenido.replace("```python", "").replace("```", "").strip()
        else:
            print(f"Error HTTP Ollama: {response.status_code}")
    except Exception as e:
        print(f"Error de red (¿Tailscale activo?): {e}")
    return None

# --- EJECUCIÓN ---
print("Iniciando generación masiva de código...")

for i in range(1, NUM_PROGRAMAS + 1):
    # 1. Generación Grok vía API
    print(f"Generando con Grok API - Intento {i} de {NUM_PROGRAMAS}...")
    codigo_grok = generar_grok_api(PROMPT)
    if codigo_grok:
        with open(f"combsort_grok_{i}.py", "w", encoding="utf-8") as f:
            f.write(codigo_grok)
            
    # 2. Generación Remota (Qwen vía Tailscale)
    print(f"Generando con Qwen (Tailscale) - Intento {i} de {NUM_PROGRAMAS}...")
    codigo_qwen = generar_qwen_tailscale(PROMPT)
    if codigo_qwen:
        with open(f"combsort_qwen_{i}.py", "w", encoding="utf-8") as f:
            f.write(codigo_qwen)

print("Generación termianda. Los 10 archivos han sido guardados.")