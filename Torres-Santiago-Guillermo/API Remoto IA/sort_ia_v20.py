import os
import re
import ast
import subprocess
import requests
import requests
import json
from typing import List

#--------------------------- Limpiar comentarios -----------------------
def clean_code(code):
    match = re.search(r"```python(.*?)```", code, re.DOTALL)
    if match:
        return match.group(1).strip()
    return code.strip()

#---------------------------- Guardar codigo ---------------------------
def save_code(code, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

#---------------------- Cargar archivos de prueba ----------------------
def get_test_files(directory):
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith(".txt")
    ]

#------------------------- Revisar orden -------------------------------
def revisar_orden(output):
    try:
        nums = list(map(int, output.strip().split(",")))
        return nums == sorted(nums)
    except:
        return False

#---------------------- Ejecutar Pruebas -------------------------------
def run_test(file_path, script_path):

    with open(file_path, "r", encoding="utf-8") as f:
        input_data = f.read().strip()


    result = subprocess.run(
        ["python", script_path, input_data],
        capture_output=True,
        text=True,
        timeout=5
    )

    salida = result.stdout.strip()

    print(f"\nCaso: {file_path}")
    print(f"Entrada: {input_data}")
    print(f"Salida: {salida}")

    if result.stderr.strip():
        print("Error de Compilacion")
        return False

    std_orden = revisar_orden(salida)

    if std_orden:
        print("Resultado: CORRECTO")
    else:
        print("Resultado: INCORRECTO")

    return std_orden

#---------------------------- Main -------------------------------------

local  = "localhost"
remote = "100.113.158.78"

urls = [ "http://"+ local  +":11434/api/generate",
         "http://"+ remote +":11434/api/generate",
       ]

models = [ "llama3.2",  # Remoto
           "qwen3:8B",
           "qwen3:4B",
           "gemma3:1b",
           "gemma3:4b"  
         ]
prompt = [
    "Eres un experto en programacion en python, genera unicamente codigo Python valido del algoritmo Bitonic sort. " +
     "Sin explicaciones, sin comentarios. " +
     "Debe ser portable, utilizar como entrada de datos sys.argv[1]. " +
     "La entrada sera una lista de enteros positivos y negativos separados por comas. " +
     "La salida debe imprimirse usando print(). " +
     "La salida del programa seran la lista ordenada separada solo con comas."
    
]

url = urls[0]

casos = "pruebas_sort"

print("Lista de modelos: ")
n_mod = len(models)
for k in range(n_mod):
    print(f"{k+1} - {models[k]}")

sel_mod = int(input("Seleccione el numero de modelo: "))

payload = {
    "model":  models[sel_mod-1],
    "prompt": prompt[0],
    "stream": False
}

n_pruebas = int(input("Ingrese numero de codigos de prueba: "))

for i in range(1,n_pruebas+1):
    response = requests.post(url, json=payload)
    response.raise_for_status()
    code_res = response.json()["response"]
    
    codigo = clean_code(code_res)
    
    sort_code = f"bitonic_{i}.py"
    save_code(codigo, sort_code)

print("\n Resultados:")

datos = get_test_files(casos)
total_casos = len(datos)
suma = 0

for i in range(1,n_pruebas+1):

    print(f"\n\tCodigo {i}:")
    sort_code = f"bitonic_{i}.py"
    casos_ok = 0
    for archivo in datos:
        if run_test(archivo, sort_code):
            casos_ok += 1

    
    prom_prog = casos_ok / total_casos # Promediar programa
    suma += prom_prog
    print(f"\nCasos correctos: {casos_ok}/{total_casos}")

pass_a = (suma/n_pruebas) *10
print(f"\nPass@ = {pass_a}/10")