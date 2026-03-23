"""
    Conexion con API Remota IA
    Solicitud de algoritmo de ordenamiento 
    Bitonic sort y ejecucion

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    13/Marzo/2026 

"""
import requests
import json

local  = "localhost"
remote = "100.113.158.78"

urls = [ "http://"+ local  +":11434/api/generate",
         "http://"+ remote +":11434/api/generate",
         "http://"+ remote +":11434/api/chat",
       ]

models = [ "llama3.2",  # Remoto
           "qwen3:4B",
           "gemma3:1b"  # Local
         ]
prompt = [
    "1+2",
    "Dame el codigo del algoritmo Bitonic sort en python. " +
     "Sin explicaciones, sin comentarios.",
    "Dame el codigo del algoritmo Bitonic sort en python. " +
     "Sin explicaciones, sin comentarios. " +
     "Utiliza como variable: [9, 65, 32, 43, 2, 93, 0, 23, 10]. " +
     "Que el programa imprima el resultado de la variable ordenada.",
    
]

url = urls[1]
payload = {
    "model":  models[0],
    "prompt": prompt[2],
    "stream": False
}

response = requests.post(url, json=payload)

sin_pref = ""
codigo = ""

if response.status_code == 200:
    data = response.json()
    print(data["response"])
    print("-------------Ejecucion----------------")
    
    sin_pref = data["response"].removeprefix("```python\n")
    codigo = sin_pref.removesuffix("```")
    #print(codigo)
    exec(codigo)
else:
    print("Error:", response.status_code, response.text)