import os
import random
from get_ollama import generar_codigo
from get_ollama import modelos
from utilidades import limpiar_codigo
from utilidades import guardar_codigo
from pruebas import obtener_casos
from pruebas import ejecutar_prueba


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CARPETA_CASOS = os.path.join(
    BASE_DIR,
    "casos"
)

CARPETA_GENERADOS = os.path.join(
    BASE_DIR,
    "generados"
)

os.makedirs(
    CARPETA_CASOS,
    exist_ok=True
)

os.makedirs(
    CARPETA_GENERADOS,
    exist_ok=True
)


def generar_casos(n):
    for i in range(1, n + 1):
        datos = [
            random.randint(-100, 100)
            for _ in range(
                random.randint(5, 20)
            )
        ]

        archivo = os.path.join(
            CARPETA_CASOS,
            f"caso_{i}.txt"
        )

        with open(
            archivo,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                ",".join(
                    map(str, datos)
                )
            )


def entrada():
    print("Lista de modelos:")

    for i in range(len(modelos)):
        print(f"{i+1} - {modelos[i]}")

    mod = int(input("Seleccione modelo: "))
    n_codigos = int(input("Numero de codigos: "))
    n_casos = int(input("Numero de casos: "))

    return mod, n_codigos, n_casos


def main():
    mod, n_codigos, n_casos = entrada()
    generar_casos(n_casos)

    prompt = (
        """
        Genera SOLAMENTE codigo Python.

        Requisitos:

        1. Python 3.10+
        2. Sin markdown.
        3. Sin bloques ```python.
        4. Sin explicaciones.
        5. Sin comentarios.
        6. Debe leer una lista desde sys.argv[1].
        7. La entrada son enteros separados por comas.
        8. Debe imprimir la lista ordenada separada por comas.
        9. Implementa exclusivamente Bitonic Sort.
        10. El archivo generado debe ejecutarse directamente.
        11. No escribas nada fuera del codigo fuente.
        12. Sin bloques ```.
        """
    )

    for i in range(1, n_codigos + 1):
        codigo = generar_codigo(modelos[mod - 1],prompt)
        if codigo is None:
            print(f"Error generando "f"bit_{i}.py")
            continue

        codigo = limpiar_codigo(codigo)
        archivo = os.path.join(
            CARPETA_GENERADOS,
            f"bit_{i}.py"
        )

        guardar_codigo(codigo,archivo)

    casos = obtener_casos(
        CARPETA_CASOS
    )

    total_casos = len(casos)
    suma = 0
    print("\nResultados:")

    for i in range(1, n_codigos + 1):
        print(f"\nCodigo {i}")

        programa = os.path.join(
            CARPETA_GENERADOS,
            f"bit_{i}.py"
        )

        casos_ok = 0
        for archivo in casos:
            if ejecutar_prueba(archivo,programa):
                casos_ok += 1

        print(f"\nCasos correctos:"f" {casos_ok}/{total_casos}")

        prom_prog = (
            casos_ok /
            total_casos
        )
        suma += prom_prog

    pass_a = (
        suma /
        n_codigos
    ) * 10

    print(f"\nPass@ = "f"{pass_a:.2f}/10")

if __name__ == "__main__":
    main()