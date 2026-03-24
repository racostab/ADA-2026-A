#
# Usando indirectamente el protocolo HTTP para interactuar con el modelo LLaMA a través de la API de Ollama.
# Server 
# export OLLAMA_HOST="127.0.0.1:8080" 
# export OLLAMA_HOST="0.0.0.0:11434" 
# $ ollama serve
import requests
import json

local  = "localhost"
remote = "100.113.158.78"

urls = [ "http://"+ local  +":11434/api/generate",
         "http://"+ remote +":11434/api/generate",
         "http://"+ remote +":11434/api/chat",
       ]

models = [ "llama3.2",
           "qwen3:4B",
         ]
prompt = [ 
    # Elemento 0: Explicación + Código Comentado
    "Explica detalladamente cómo funciona el algoritmo Comb Sort " +
    "y luego comparte el código en Python 3 debidamente comentado.",
    
    # Elemento 1: Solo código, sin comentarios (ideal para exec())
    "Proporciona ÚNICAMENTE el código de una función en Python para Comb Sort. " +
    "No incluyas explicaciones, no incluyas comentarios, ni marcas de markdown. " +
    "Solo el código ejecutable."
]

url = urls[1]
payload = {
    "model":  models[0],
    "prompt": prompt[0],
    "stream": False
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data["response"])
else:
    print("Error:", response.status_code, response.text)
