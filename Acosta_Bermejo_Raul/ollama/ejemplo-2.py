#
# Usando indirectamente el protocolo HTTP para interactuar con el modelo LLaMA a través de la API de Ollama.
# 
import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    #"model": "llama3.2",
    "model":'qwen3:4B',
    "prompt": "Explica como funciona un algoritmo que calcule el conjunto potencia.",
    "stream": False
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data["response"])
else:
    print("Error:", response.status_code, response.text)