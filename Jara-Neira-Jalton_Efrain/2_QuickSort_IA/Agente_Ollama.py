import requests
import json
import os

def limpiar_codigo(texto_raw: str) -> str:
    """Elimina bloques de markdown y espacios innecesarios del modelo."""
    return texto_raw.replace("```python", "").replace("```", "").strip()

def guardar_codigo(codigo: str, indice: int):
    """Guarda el código automáticamente con un nombre incremental."""
    nombre_archivo = f"quicksort_{indice}.py"
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(codigo)
        print(f"Archivo creado: {os.path.abspath(nombre_archivo)}")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

def ejecutar_cliente():
    # Configuración de Red
    ip_local = "localhost"
    ip_remota = "100.113.158.78"
    puerto = "11434"

    print("--- CONFIGURACIÓN DE CONSULTA ---")
    opcion_srv = input("Seleccione Servidor [0: Local, 1: Remoto]: ")
    host = ip_remota if opcion_srv == "1" else ip_local
    url = f"http://{host}:{puerto}/api/generate"

    modelos = ["llama3.2", "qwen3:4B"]
    print("\nModelos disponibles:")
    for i, m in enumerate(modelos): print(f"{i}: {m}")
    
    try:
        idx_mod = int(input("Número de modelo a usar: "))
        modelo_elegido = modelos[idx_mod]
        
        # Cantidad de consultas
        num_consultas = int(input("\n¿Cuántas consultas (archivos) deseas generar?: "))
    except (ValueError, IndexError):
        print("Entrada inválida. Reinicia el programa.")
        return

    # Bucle de generación
    for n in range(1, num_consultas + 1):
        print(f"\n[Consulta {n}/{num_consultas}] Solicitando a {modelo_elegido}...")
        
        payload = {
            "model": modelo_elegido,
            "prompt": (
                "Implementa el algoritmo Quick Sort en Python 3.14. "
                "RESTRICCIONES: Devuelve estrictamente el código funcional. "
                "Sin comentarios, sin explicaciones, sin markdown. "
                f"Asegúrate de que sea la variante número {n}."
            ),
            "stream": False,
            "options": {"temperature": 0.8} # Un poco de variedad para cada archivo
        }

        try:
            response = requests.post(url, json=payload, timeout=50)
            if response.status_code == 200:
                codigo_sucio = response.json().get("response", "")
                codigo_final = limpiar_codigo(codigo_sucio)
                
                # Guardado automático
                guardar_codigo(codigo_final, n)
            else:
                print(f"Error API (Status {response.status_code}): {response.text}")
        except Exception as e:
            print(f"Error de conexión: {e}")

    print("\n--- Proceso Terminado ---")

if __name__ == "__main__":
    ejecutar_cliente()