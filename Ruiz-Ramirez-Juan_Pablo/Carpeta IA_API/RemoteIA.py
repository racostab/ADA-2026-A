import requests
import json
import re
import os
import sys

# ==================================================
# 1. Selección del endpoint (local o remoto)
# ==================================================
def seleccionar_url():
    print("Selecciona el endpoint de Ollama:")
    print("1. Local (http://localhost:11434/api/generate)")
    print("2. Remoto (http://100.113.158.78:11434/api/generate)")  
    opcion = input("Opción (1/2): ").strip()
    if opcion == "1":
        return "http://localhost:11434/api/generate"
    elif opcion == "2":
        # Aquí puedes pedir la IP o tenerla fija
        ip = input("Ingresa la IP remota (ej. 100.113.45.12): ").strip()
        return f"http://{ip}:11434/api/generate"
    else:
        print("Opción no válida, usando local por defecto.")
        return "http://localhost:11434/api/generate"

# ==================================================
# 2. Función para consultar la IA y obtener código
# ==================================================
def validar_ordenamiento(lista_original, lista_ordenada):
    """
    Valida si la lista ordenada es correcta.
    Retorna:
        - 'correcto': True/False
        - 'puntaje': 1 si está correcta, 0 si no
        - 'esperado': la lista ordenada correctamente
        - 'errores': lista de elementos fuera de lugar (si aplica)
    """
    esperado = sorted(lista_original)
    
    if lista_ordenada == esperado:
        return {
            'correcto': True,
            'puntaje': 1,
            'esperado': esperado,
            'errores': None
        }
    else:
        # Identificar diferencias
        diferencias = []
        for i, (obtenido, esper) in enumerate(zip(lista_ordenada, esperado)):
            if obtenido != esper:
                diferencias.append({
                    'posicion': i,
                    'obtenido': obtenido,
                    'esperado': esper
                })
        return {
            'correcto': False,
            'puntaje': 0,
            'esperado': esperado,
            'errores': diferencias
        }
def obtener_codigo_sorting(modelo, url, prompt):
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.2   # para respuestas más deterministas
    }
    try:
        resp = requests.post(url, json=payload, timeout=60)
        if resp.status_code == 200:
            respuesta_texto = resp.json().get("response", "")
            return extraer_codigo(respuesta_texto)
        else:
            print(f"Error HTTP {resp.status_code}: {resp.text}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def extraer_codigo(texto):
    """
    Intenta extraer código Python de la respuesta de la IA.
    Busca bloques con ```python ... ``` o simplemente cualquier definición de función.
    """
    # Buscar bloque de código triple backticks
    patron = r"```python\n(.*?)\n```"
    match = re.search(patron, texto, re.DOTALL)
    if match:
        return match.group(1)
    # Si no, buscar cualquier bloque con triple backticks
    patron2 = r"```(.*?)```"
    match2 = re.search(patron2, texto, re.DOTALL)
    if match2:
        return match2.group(1)
    # Si no, asumir que todo el texto es código (peligroso pero a veces funciona)
    # Mejor buscar una definición de función 'def counting_sort'
    if "def counting_sort" in texto:
        return texto
    return None

# ==================================================
# 3. Lectura de archivos .txt
# ==================================================
def leer_casos(directorio="./casos"):
    casos = []
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe. Créalo y ponga archivos .txt")
        return casos
    for archivo in sorted(os.listdir(directorio)):
        if archivo.endswith(".txt"):
            ruta = os.path.join(directorio, archivo)
            with open(ruta, "r", encoding="utf-8") as f:
                for num_linea, linea in enumerate(f, 1):
                    linea = linea.strip()
                    if linea:
                        # Convertir a lista de enteros (separadores: espacios o comas)
                        numeros = [int(x) for x in linea.replace(',', ' ').split()]
                        casos.append((archivo, num_linea, numeros))
    return casos

# ==================================================
# 4. Ejecución segura del código generado
# ==================================================
def ejecutar_codigo_sorting(codigo_str, lista_numeros):
    """
    Define una función counting_sort a partir del código generado y la ejecuta.
    Retorna la lista ordenada o None si hay error.
    """
    # Prepara el entorno de ejecución restringido
    entorno = {}
    try:
        # Ejecutar el código para definir la función counting_sort
        exec(codigo_str, entorno)
        if "counting_sort" not in entorno:
            print("El código generado no contiene una función llamada 'counting_sort'")
            return None
        funcion_sort = entorno["counting_sort"]
        # Llamar a la función con la lista de números
        resultado = funcion_sort(lista_numeros)
        return resultado
    except Exception as e:
        print(f"Error al ejecutar el código generado: {e}")
        return None

# ==================================================
# 5. Función principal
# ==================================================
def main():
    print("=" * 60)
    print("SISTEMA DE EVALUACIÓN DE CÓDIGO IA - COUNTING SORT")
    print("=" * 60)
    
    # Seleccionar URL y modelo
    url = seleccionar_url()
    modelo = input("Modelo a usar (ej. llama3.2, qwen3:4B, gemma3:1b): ").strip() or "llama3.2"

    # Prompt para la IA
    prompt_ia = """Eres un asistente que solo genera código Python.  
Genera únicamente la función `counting_sort` que recibe una lista de enteros no negativos y devuelve la lista ordenada usando el algoritmo Counting Sort.  
No incluyas ejemplos de uso, ni explicaciones, solo la definición de la función con su lógica.  
Asegúrate de que el código sea correcto y eficiente.  
Respuesta en bloque de código Python."""
    print(prompt_ia)
    print("\n⏳ Consultando a la IA para generar el código...")
    codigo_generado = obtener_codigo_sorting(modelo, url, prompt_ia)

    if not codigo_generado:
        print("No se pudo obtener código válido. Abortando.")
        return

    # Guardar el código generado
    with open("codigo_generado.py", "w", encoding="utf-8") as f:
        f.write(codigo_generado)
    print("Código generado guardado en 'codigo_generado.py'")

    print("\n" + "=" * 60)
    print("CÓDIGO GENERADO POR LA IA:")
    print("=" * 60)
    print(codigo_generado)
    print("=" * 60)

    # Leer casos de prueba
    casos = leer_casos()
    if not casos:
        print("No se encontraron casos de prueba en ./casos/")
        return

    print(f"\nSe encontraron {len(casos)} casos de prueba")
    print("-" * 60)

    # Estadísticas globales
    resultados = []
    total_correctos = 0
    total_incorrectos = 0

    # Procesar cada caso
    for idx, (archivo, linea_num, datos) in enumerate(casos, 1):
        print(f"\nCASO {idx}: {archivo} (línea {linea_num})")
        print(f"   Lista original: {datos}")
        
        # Ejecutar el código de la IA
        resultado_ia = ejecutar_codigo_sorting(codigo_generado, datos)
        
        if resultado_ia is None:
            print(f"   Error al ejecutar el código de IA")
            resultados.append({
                'caso': idx,
                'archivo': archivo,
                'linea': linea_num,
                'original': datos,
                'obtenido': None,
                'valido': False,
                'puntaje': 0,
                'error_ejecucion': True
            })
            total_incorrectos += 1
            continue
        
        # Validar el resultado
        validacion = validar_ordenamiento(datos, resultado_ia)
        
        # Mostrar resultado
        if validacion['correcto']:
            print(f"   ✅ ORDENADO CORRECTAMENTE")
            print(f"   Lista ordenada: {resultado_ia}")
            print(f"   Puntaje: 1/1")
            total_correctos += 1
        else:
            print(f"   ❌ ORDENADO INCORRECTAMENTE")
            print(f"   Obtenido por IA: {resultado_ia}")
            print(f"   Esperado: {validacion['esperado']}")
            print(f"   Puntaje: 0/1")
            
            # Mostrar primeros 3 errores si existen
            if validacion['errores']:
                print(f"   Errores detectados:")
                for err in validacion['errores'][:3]:
                    print(f"     - Posición {err['posicion']}: esperaba {err['esperado']}, obtuvo {err['obtenido']}")
            total_incorrectos += 1
        
        # Guardar resultado
        resultados.append({
            'caso': idx,
            'archivo': archivo,
            'linea': linea_num,
            'original': datos,
            'obtenido': resultado_ia,
            'valido': validacion['correcto'],
            'puntaje': validacion['puntaje'],
            'esperado': validacion['esperado'] if not validacion['correcto'] else None,
            'error_ejecucion': False
        })
    
    # Mostrar estadísticas finales
    print("\n" + "=" * 60)
    print("RESUMEN DE RESULTADOS")
    print("=" * 60)
    print(f"Total casos procesados: {len(casos)}")
    print(f"Correctos: {total_correctos}")
    print(f"Incorrectos: {total_incorrectos}")
    print(f"Tasa de éxito: {(total_correctos/len(casos))*100:.1f}%")
    
    # Calcular puntaje total (suma de todos los puntajes)
    puntaje_total = sum(r['puntaje'] for r in resultados if not r.get('error_ejecucion', False))
    print(f"Puntaje total: {puntaje_total}/{len(casos)}")
    
    # Guardar resultados en archivo
    with open("resultados_evaluacion.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    print("\nResultados detallados guardados en 'resultados_evaluacion.json'")
    
    # Generar reporte simple en texto
    with open("reporte_evaluacion.txt", "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("REPORTE DE EVALUACIÓN DE CÓDIGO IA\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Modelo usado: {modelo}\n")
        f.write(f"Endpoint: {url}\n")
        f.write(f"Total casos: {len(casos)}\n")
        f.write(f"Correctos: {total_correctos}\n")
        f.write(f"Incorrectos: {total_incorrectos}\n")
        f.write(f"Tasa de éxito: {(total_correctos/len(casos))*100:.1f}%\n\n")
        
        for r in resultados:
            f.write(f"Caso {r['caso']} ({r['archivo']}, línea {r['linea']}): ")
            if r.get('error_ejecucion'):
                f.write("ERROR EJECUCIÓN\n")
            else:
                f.write(f"{'CORRECTO' if r['valido'] else 'INCORRECTO'} (puntaje: {r['puntaje']})\n")
    
    print("📝 Reporte guardado en 'reporte_evaluacion.txt'")
    print("=" * 60)

    # Opcional: preguntar si quiere ver el reporte completo
    ver_detalle = input("\n¿Ver detalles completos de resultados? (s/n): ").lower()
    if ver_detalle == 's':
        for r in resultados:
            print(f"\n--- Caso {r['caso']} ---")
            print(f"Archivo: {r['archivo']}")
            print(f"Original: {r['original']}")
            if r.get('error_ejecucion'):
                print("Error: No se pudo ejecutar el código")
            else:
                print(f"Obtenido: {r['obtenido']}")
                if not r['valido']:
                    print(f"Esperado: {r['esperado']}")

if __name__ == "__main__":
    main()