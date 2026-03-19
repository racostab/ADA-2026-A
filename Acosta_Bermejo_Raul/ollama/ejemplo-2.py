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
prompt = [ "3+4",
           "Explica como funciona un algoritmo que calcula el conjunto potencia.",
           "Implementa el algoritmo del Emparejamiento Estable."+
           "En lenguaje python version 3.10 o superior"+
           "Colocal el codigo en una funcion smp."+
           "No comentes el codigo y no agregues explicaciones"
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