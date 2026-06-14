# OLLAMA_HOST="127.0.0.1:8080" 
# gpt-oss:120b-cloud requiere una cuenta en ollama y configurar la API key del servicio (o usar "ollama signin" en la terminal,acceder con tu cuenta de ollama y autorizar el dispositivo)
# por ultimo agregar el modelo con "ollama run  gpt-oss:120b-cloud" para poder hacer solicitudes en la nube 
# todo esto devido a que el modelo gpt-oss (el modelo libre de open AI) solo cuenta con versiones de 20B y 120B  parametros y requieren equipos con  >16Gb y >80Gb respectivamente
import requests
import json

local  = "localhost"

urls = [ "http://"+ local  +":11434/api/generate",
       ]

models = [ "gpt-oss:120b-cloud"
         ]

prompt = [ "Genera una funcion en python que realize el algoritmo bubble sort, sin comentarios y que tenga la siguiente estructura Bubble_sort(lista)"
         ]

url = urls[0]
payload = {
    "model":  models[0],
    "prompt": prompt[0],
    "stream": False
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data["response"])
    file_path = "./sort.py"
    with open(file_path, "w") as text_file:
        text_file.write(data["response"][10:len(data["response"])-3])
    
    from sort import Bubble_sort
    #se realizaran 10 casos de prueba con el algoritmo generado con IA
    test_cases = [
    [34, -2, 10, -9, 0, 5, 2],          # Caso 1: Mezcla de positivos, negativos y cero
    [1, 2, 3, 4, 5, 6, 7],              # Caso 2: Ya ordenada
    [7, 6, 5, 4, 3, 2, 1],              # Caso 3: Orden inverso
    [4, 2, 4, 3, 1, 2, 4],              # Caso 4: Muchos duplicados
    [42],                               # Caso 5: Un solo elemento
    [],                                 # Caso 6: Lista vacía
    [5, 5, 5, 5],                       # Caso 7: Todos iguales
    [1000, 10, 100000, 1],              # Caso 8: Diferentes magnitudes
    [2, 1],                             # Caso 9: Dos elementos desordenados
    [3.5, 1.2, 4.8, 2.1]                # Caso 10: Números decimales
    ]

    expected_responses = [
    [-9, -2, 0, 2, 5, 10, 34],          # Respuesta 1
    [1, 2, 3, 4, 5, 6, 7],              # Respuesta 2
    [1, 2, 3, 4, 5, 6, 7],              # Respuesta 3
    [1, 2, 2, 3, 4, 4, 4],              # Respuesta 4
    [42],                               # Respuesta 5
    [],                                 # Respuesta 6
    [5, 5, 5, 5],                       # Respuesta 7
    [1, 10, 1000, 100000],              # Respuesta 8
    [1, 2],                             # Respuesta 9
    [1.2, 2.1, 3.5, 4.8]                # Respuesta 10
    ]

    puntaje = 0
    for i in range(len(test_cases)):
        print(f"Test case {i}: \n{test_cases[i]}")
        print(f"Resutlado esperado: {expected_responses[i]}")
        sort = Bubble_sort(test_cases[i])
        print(f"Resultado obtenido: {sort}")
        if sort == expected_responses[i]:
            print("Test Case Passed \n")
            puntaje +=1
        else:
            print("Test case Failed")
    
    print(f"Respuestas correctas: {puntaje}")
        

else:
    print("Error:", response.status_code, response.text)
