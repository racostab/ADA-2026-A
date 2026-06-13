import importlib.util
import random
import math
import os

NUM_PROGRAMAS = 5
NUM_PRUEBAS = 10
FUNCION_NOMBRE = "comb_sort"

def cargar_modulo(nombre_archivo, nombre_modulo):
    spec = importlib.util.spec_from_file_location(nombre_modulo, nombre_archivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

def generar_arreglo():
    tamaño = random.randint(5, 20)
    return [random.randint(0, 100) for _ in range(tamaño)]

def evaluar_modelo(prefijo_archivos, archivo_resultados):
    programas_correctos = 0
    
    with open(archivo_resultados, "w", encoding="utf-8") as f:
        f.write(f"=== EVALUACIÓN PARA: {prefijo_archivos.upper()} ===\n")
        
        for i in range(1, NUM_PROGRAMAS + 1):
            nombre_archivo = f"{prefijo_archivos}_{i}.py"
            if not os.path.exists(nombre_archivo):
                f.write(f"\n[!] Archivo {nombre_archivo} no encontrado.\n")
                continue
                
            try:
                modulo = cargar_modulo(nombre_archivo, f"mod_{prefijo_archivos}_{i}")
            except SyntaxError as e:
                f.write(f"\n===== CODIGO {i} =====\n")
                f.write(f"ERROR DE SINTAXIS AL IMPORTAR: {e}\n")
                continue

            f.write(f"\n===== CODIGO {i} =====\n")
            paso_todas = True
            
            for j in range(1, NUM_PRUEBAS + 1):
                arr = generar_arreglo()
                esperado = sorted(arr)
                
                try:
                    # Validar que la función exista
                    if not hasattr(modulo, FUNCION_NOMBRE):
                        raise AttributeError(f"La función {FUNCION_NOMBRE} no existe en el código generado.")
                        
                    funcion_sort = getattr(modulo, FUNCION_NOMBRE)
                    arr_copia = arr.copy()
                    salida = funcion_sort(arr_copia)
                    
                    if salida is None:
                        salida = arr_copia
                        
                except Exception as e:
                    salida = f"ERROR: {e}"
                    paso_todas = False
                
                correcto = salida == esperado
                if not correcto:
                    paso_todas = False
                    
                f.write(f"Prueba {j} - Correcto: {correcto}\n")
            
            if paso_todas:
                programas_correctos += 1
                f.write(f"-> RESULTADO: ÉXITO.\n")
            else:
                f.write(f"-> RESULTADO: FALLO.\n")

        # Pass@k
        n = NUM_PROGRAMAS
        c = programas_correctos
        k = 1 
        
        if n - c >= k:
            pass_at_k = 1 - (math.comb(n - c, k) / math.comb(n, k))
        else:
            pass_at_k = 1.0
            
        f.write("\n===== RESULTADO FINAL =====\n")
        f.write(f"Programas correctos (c): {c} de {n}\n")
        f.write(f"Métrica Pass@{k}: {pass_at_k:.2f} ({pass_at_k * 100}%)\n")
        f.write("===========================\n\n")

print("Evaluando modelos y calculando Pass@k...")
# Evaluamos ambos bloques generados
evaluar_modelo("combsort_grok", "resultados_grok.txt")
evaluar_modelo("combsort_qwen", "resultados_qwen.txt")
print("Evaluación Terminada.")