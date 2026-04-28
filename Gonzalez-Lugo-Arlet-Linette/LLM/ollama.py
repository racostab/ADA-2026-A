import os
import re
import ast
import subprocess
import requests
from typing import List

URL: str = "http://localhost:11434/api/generate"
URL2 = "http://100.113.158.78:11434/api/generate"
CARPETA_CASOS: str = "test_cases"
NOMBRE_PY: str = "quicksort.py"


def generate_code() -> str:
    data = {
        "model": "llama3.2",
        "prompt": (
            "#Rol: Eres un ingeniero de software senior especializado en algoritmos y Python idiomático.\n"
            " Tarea\n"
            "Implementa Quicksort en Python.\n"
            
            "#Entrada de datos\n"
            "- Es obligatorio usar sys.argv[1] como única fuente de datos.\n"
            "- Está prohibido usar ejemplos hardcodeados.\n"
            "- El programa debe fallar si no se proporciona argumento.\n"
            
            "#Salida\n"
            "- Imprimir lista ordenada separada por coma y espacio.\n"
            
            "#Restricciones\n"
            "- No usar sort() ni sorted()\n"
            "- Código listo para producción\n"
            
            "### Entregable\n"
            "- Solo código Python sin markdown"
        ),
        "stream": False
    }

    response = requests.post(URL2, json=data)
    response.raise_for_status()

    return response.json()["response"]

#Para que pueda ejecutar el programa con archivos externos quitamos los ''' cuando genera el codigo el modelo
def clean_code(code: str) -> str:
    match = re.search(r"```python(.*?)```", code, re.DOTALL)
    if match:
        return match.group(1).strip()
    return code.strip()


def save_code(code: str, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)


def get_test_files(directory: str) -> List[str]:
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith(".txt")
    ]


def normalize_output(output: str) -> List[int]:

    output = output.strip()

    if output.startswith("[") and output.endswith("]"):
        return list(ast.literal_eval(output))

    return list(map(int, output.split(",")))


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
    print("Generando código...")
    code = generate_code()

    print("Limpiando código...")
    cleaned_code = clean_code(code)

    print("Guardando código...")
    save_code(cleaned_code, NOMBRE_PY)

    print("Código generado:\n")
    print(cleaned_code[:500])

    print("\nEjecutando pruebas...\n")
    test_files = get_test_files(CARPETA_CASOS)

    for test_file in test_files:
        run_test(test_file, NOMBRE_PY)


if __name__ == "__main__":
    main()