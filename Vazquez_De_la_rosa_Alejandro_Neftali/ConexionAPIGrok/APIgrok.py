import requests
import os
import json
import datetime
from dotenv import load_dotenv

# 1. Cargamos las variables de entorno (API Key)
load_dotenv()
api_key = os.getenv("XAI_API_KEY")

# 2. Configuración del Endpoint y Headers
url = "https://api.x.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 3. Estructuramos el Diccionario de Datos (Payload)
data = {
    "model": "grok-4.20-0309-reasoning",
    "messages": [
        {
            "role": "system",
            "content": (
                "Eres un experto en algoritmos. Proporciona código en Python, "
                "explica la lógica del algoritmo y su complejidad Big O."
            )
        },
        {
            "role": "user",
            "content": "Implementa el algoritmo Comb Sort con un ejemplo de uso."
        }
    ],
    "temperature": 0.2  # Más determinista
}

# 4. Realizamos la petición POST
try:
    # Enviamos el diccionario 'data' convertido a JSON automáticamente
    response = requests.post(url, headers=headers, json=data)
    
    # Verificamos si la respuesta fue exitosa (Código 200)
    if response.status_code == 200:
        # Extraemos el texto de la respuesta de Grok
        resultado = response.json()
        contenido = resultado['choices'][0]['message']['content']
        contenido = resultado['choices'][0]['message']['content']
        
        #Guardar en respuesta en archivo 
        nombre_archivo = "respuesta_grok_combsort.txt"
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"--- EVIDENCIA DE CONSULTA A GROK ---\n")
            archivo.write(f"Fecha y Hora: {ahora}\n")
            archivo.write(f"Modelo usado: {data['model']}\n")
            archivo.write("-" * 40 + "\n\n")
            archivo.write(contenido)
            
        print(f"Respuesta guardada exitosamente en: {nombre_archivo}")
        print("--- RESPUESTA DE GROK ---")
        print(contenido)
    else:
        print(f"Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"Ocurrió un error en la conexión: {e}")
