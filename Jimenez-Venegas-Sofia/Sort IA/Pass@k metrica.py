import importlib.util
import random
import math

NUM_PROGRAMAS = 5
NUM_PRUEBAS = 10
archivo_resultados = "resultados_pruebas.txt"

def cargar_modulo(nombre_archivo, nombre_modulo):
    spec = importlib.util.spec_from_file_location(nombre_modulo, nombre_archivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

def generar_arreglo():
    tamaño = random.randint(5, 15)
    return [random.randint(0, 100) for _ in range(tamaño)]

programas_correctos = 0

with open(archivo_resultados, "w", encoding="utf-8") as f:

    for i in range(1, NUM_PROGRAMAS + 1):

        nombre_archivo = f"radix_sort_{i}.py"
        modulo = cargar_modulo(nombre_archivo, f"mod{i}")

        f.write(f"\n===== CODIGO {i} =====\n")

        paso_todas = True

        for j in range(1, NUM_PRUEBAS + 1):

            arr = generar_arreglo()
            esperado = sorted(arr)

            try:
                salida = modulo.radix_sort(arr.copy())
            except Exception as e:
                salida = f"ERROR: {e}"
                paso_todas = False

            correcto = salida == esperado

            if not correcto:
                paso_todas = False

            f.write(f"\nPrueba {j}\n")
            f.write(f"Input: {arr}\n")
            f.write(f"Output: {salida}\n")
            f.write(f"Esperado: {esperado}\n")
            f.write(f"Correcto: {correcto}\n")

        if paso_todas:
            programas_correctos += 1

        f.write("\n")

# cálculo Pass@k
n = NUM_PROGRAMAS
c = programas_correctos

with open(archivo_resultados, "a", encoding="utf-8") as f:
    f.write("\n===== RESULTADO FINAL =====\n")
    f.write(f"Programas correctos: {c}/{n}\n\n")

    for k in range(1, n + 1):

        if n - c < k:
            pass_at_k = 1.0
        else:
            pass_at_k = 1 - (math.comb(n - c, k) / math.comb(n, k))

        f.write(f"Pass@{k}: {pass_at_k}\n")

print("Pruebas terminadas. Ver resultados_pruebas.txt")