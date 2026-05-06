import os
import re
import ast
import subprocess
import requests
from typing import List

def generate_code(model: str, url: str, prompt: str) -> str:
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    response.raise_for_status()

    return response.json()["response"]


def save_code(code: str, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)


def run_test(file_path: str, script_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        input_data = f.read().strip()

    try:
        result = subprocess.run(
            ["python", script_path, input_data],
            capture_output=True,
            text=True,
            timeout=5
        )

        print(f"\nCaso: {file_path}")
        print(f"Entrada: {input_data}")
        print(f"Salida: {result.stdout.strip()}")

    except subprocess.TimeoutExpired:
        print(f"Timeout en {file_path}")


def main():
    setup = {
       "models": ["llama3.2", "mistral:latest", "deepseek-coder:1.3b"],
       "urls": [ "http://localhost:11434/api/generate",
                 "http://100.113.158.78:11434/api/generate"
               ],
    }
    print("1. Datos de inicio")
    model = setup["models"][0] 
    url = setup["urls"][0]
    prompt = "1+2"

    print(f"Modelo {model}.")
    print(f"URL {url}.")
    print(f"Prompt {prompt}.")

    print("2. Generando código...")
    programa = generate_code(model, url, prompt)
    print("Codigo")
    print(f"Programa {programa} generado.")

    print("3. Ejecutando pruebas")
    #  run_tests()
    #  for test_file in test_files:
    #      run_test(test_file, NOMBRE_PY)

    print("4. Evaluacion")

if __name__ == "__main__":
    main()