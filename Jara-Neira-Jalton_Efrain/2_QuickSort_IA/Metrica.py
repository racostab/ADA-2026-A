import importlib.util
import os
import random

def limpiar_nombre_funcion(modulo):
    """Busca una función de ordenamiento dentro del módulo cargado."""
    for nombre in ['quicksort', 'quick_sort', 'qsort']:
        func = getattr(modulo, nombre, None)
        if callable(func):
            return func
    funciones = [getattr(modulo, f) for f in dir(modulo) 
                 if callable(getattr(modulo, f)) and not f.startswith("__")]
    return funciones[0] if funciones else None

def evaluar_algoritmos():
    # 1. Generar vectores de prueba fijos para todos los programas
    pruebas = []
    for i in range(5):
        longitud = random.randint(5, 12)
        vector = [random.randint(0, 50) for _ in range(longitud)]
        pruebas.append({
            "entrada": vector.copy(),
            "esperado": sorted(vector.copy())
        })

    archivos = [f for f in os.listdir('.') if f.startswith('quicksort_') and f.endswith('.py')]
    
    if not archivos:
        print("No se encontraron archivos para evaluar.")
        return

    reporte = "==================================================\n"
    reporte += "       REPORTE DE EVALUACIÓN\n"
    reporte += "==================================================\n\n"

    resumen_final = []
    programas_perfectos = 0

    for nombre_archivo in archivos:
        reporte += f"ARCHIVO: {nombre_archivo}\n"
        reporte += "-" * 40 + "\n"
        exitos_programa = 0
        
        try:
            spec = importlib.util.spec_from_file_location("modulo_temp", nombre_archivo)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)
            func_ordenar = limpiar_nombre_funcion(modulo)
            
            if func_ordenar:
                for i, test in enumerate(pruebas):
                    v_entrada = test["entrada"].copy()
                    v_esperado = test["esperado"]
                    
                    try:
                        v_salida = func_ordenar(v_entrada.copy())
                        if v_salida is None: # Manejo de in-place
                            v_salida = v_entrada 
                        
                        paso = (v_salida == v_esperado)
                        if paso: exitos_programa += 1
                        
                        reporte += f"Test {i+1}: {'[OK]' if paso else '[FALLO]'}\n"
                        reporte += f"   Entrada:  {test['entrada']}\n"
                        reporte += f"   Esperado: {v_esperado}\n"
                        reporte += f"   Obtenido: {v_salida}\n\n"
                    except Exception as e_exec:
                        reporte += f"Test {i+1}: [ERROR DE EJECUCIÓN] -> {e_exec}\n\n"
                
                reporte += f"SUBTOTAL: {exitos_programa}/5 pruebas correctas.\n"
                if exitos_programa == 5: programas_perfectos += 1
                resumen_final.append((nombre_archivo, exitos_programa))
            else:
                reporte += "ERROR: No se encontró función ejecutable.\n"
                resumen_final.append((nombre_archivo, 0))

        except Exception as e:
            reporte += f"ERROR CRÍTICO AL CARGAR ARCHIVO: {e}\n"
            resumen_final.append((nombre_archivo, "Error de carga"))
        
        reporte += "\n" + "="*40 + "\n\n"

    # --- ANÁLISIS FINAL ---
    reporte += "\n" + "===============================================\n"
    reporte += "                ANÁLISIS FINAL\n"
    reporte += "===============================================\n"
    reporte += f"Total de programas evaluados: {len(archivos)}\n"
    reporte += f"Programas con 100% de éxito: {programas_perfectos}\n\n"
    reporte += "{:<30} | {:<15}\n".format("Nombre del Programa", "Tests Correctos")
    reporte += "-" * 50 + "\n"
    
    for nombre, score in resumen_final:
        reporte += "{:<30} | {:<15}\n".format(nombre, f"{score}/5")
    
    reporte += "===============================================\n"

    with open("resultado_evaluacion.txt", "w", encoding="utf-8") as f:
        f.write(reporte)
    
    print(f" Proceso finalizado. Se evaluaron {len(archivos)} programas.")

if __name__ == "__main__":
    evaluar_algoritmos()