import os
import subprocess
import sys

from utilidades import revisar_orden


def obtener_casos(carpeta):
    if not os.path.exists(carpeta):
        print(f"No existe la carpeta {carpeta}")
        return []

    return [
        os.path.join(carpeta, archivo)
        for archivo in os.listdir(carpeta)
        if archivo.endswith(".txt")
    ]


def ejecutar_prueba(archivo,programa):
    with open(archivo,"r",encoding="utf-8") as f:
        entrada = f.read().strip()

    resultado = subprocess.run(
    [
        sys.executable,
        programa,
        entrada
    ],
    capture_output=True,
    text=True,
    timeout=5
)

    salida = resultado.stdout.strip()

    print(f"\nCaso: {archivo}")
    print(f"Entrada: {entrada}")
    print(f"Salida: {salida}")

    if resultado.stderr.strip():
        print("Error de compilacion")
        print(resultado.stderr)
        return False
    correcto = revisar_orden(salida)

    if correcto:
        print("Resultado: CORRECTO")
    else:
        print("Resultado: INCORRECTO")
    return correcto