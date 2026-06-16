import os
import fitz  
import ollama

def obtener_pdfs_de_carpeta(nombre_carpeta="articulos"):

    ruta_base = os.path.join(os.getcwd(), nombre_carpeta)
    if not os.path.exists(ruta_base):
        print(f"Creando la carpeta '{nombre_carpeta}'... Coloca tus PDFs ahí y vuelve a ejecutar.")
        os.makedirs(ruta_base, exist_ok=True)
        return []
    
    archivos = [os.path.join(ruta_base, f) for f in os.listdir(ruta_base) if f.endswith('.pdf')]
    return archivos

def extraer_texto_fitz(ruta_pdf, limite_paginas=4):

    texto_extraido = ""
    try:
        pdf = fitz.open(ruta_pdf)
        texto_extraido += f"\n\n===== INICIO DEL ARTÍCULO: {os.path.basename(ruta_pdf)} =====\n\n"
        

        paginas_a_leer = min(len(pdf), limite_paginas)
        for i in range(paginas_a_leer):
            texto_extraido += pdf[i].get_text()
            
        texto_extraido += f"\n\n===== FIN DEL ARTÍCULO: {os.path.basename(ruta_pdf)} =====\n"
        pdf.close()
        return texto_extraido
    except Exception as e:
        return f"Error leyendo {ruta_pdf}: {e}"

def main():
    print("=== REVISIÓN AUTOMATIZADA CON LLAMA, QWEN Y PHI (VERSIONES LIGERAS) ===")
    
    carpeta_articulos = "articulos"
    carpeta_resultados = "Resultados"
    
    pdfs = obtener_pdfs_de_carpeta(carpeta_articulos)
    if not pdfs:
        return
    
    print(f"\nSe encontraron {len(pdfs)} artículos. Extrayendo texto esencial...")
    texto_total = ""
    for pdf_file in pdfs:
        print(f" - Procesando: {os.path.basename(pdf_file)}")
        texto_total += extraer_texto_fitz(pdf_file, limite_paginas=4)


    print("\n--- Configuración de la Evaluación ---")
    print("Introduce tu 'Problem Statement' para el inciso B.")
    print("(Deja en blanco y presiona Enter para usar el texto por defecto relacionado a la deteccion de incendios forestales)")
    problema_usuario = input("> ")
    
    if not problema_usuario.strip():
        problema_usuario = "Carencia de sistemas de detección temprana automatizado basado en sensores,Dependencia del factor humano para la detección de incendios.."


    modelos = [
        "llama3.2:3b",  
        "qwen2.5:1.5b",   
        "phi"        
    ]


    preguntas = f"""
    a. De estos artículos, ¿qué problemas de investigación no están resueltos?

    b. Dado el planteamiento del problema siguiente:
    "{problema_usuario}"
    y considerando los artículos analizados:
    - ¿El problema es real?
    - ¿Es pertinente?
    - ¿Es factible resolverlo en un periodo de 18 meses?
    - Justifica cada respuesta apoyándote en los textos.

    c. Para cada artículo:
    - Identifica la metodología utilizada.
    - Indica el nombre de la metodología.
    - Resume los pasos principales empleados por los autores.

    d. Si se realizara una revisión sistemática de literatura sobre este tema:
    - ¿Qué referencias fundamentales deberían incluirse?
    - ¿Qué autores aparecen como recurrentes?
    - ¿Qué trabajos son considerados base o estado del arte según los artículos analizados?

    Organiza tu respuesta utilizando estrictamente los encabezados:
    A)
    B)
    C)
    D)
    """

    prompts = [
        f"Eres un investigador experto analizando el estado del arte.\nAnaliza exclusivamente la información contenida en los artículos proporcionados.\n\nCONTEXTO:\n{texto_total}\n\nPREGUNTAS:\n{preguntas}",
        
        f"Actúa como un revisor crítico de metodologías de investigación.\nRealiza un análisis crítico identificando vacíos y limitaciones.\n\nCONTEXTO:\n{texto_total}\n\nPREGUNTAS:\n{preguntas}",
        
        f"Actúa como un ingeniero e investigador experto en sistemas de tiempo real y redes de sensores.\nAnaliza los artículos proporcionados desde una perspectiva técnica rigurosa, evaluando la viabilidad temporal, la eficiencia en el procesamiento de datos de los sensores, restricciones de hardware y la arquitectura de red.\nCONTEXTO:\n{texto_total}\n\nPREGUNTAS:\n{preguntas}"
    ]


    os.makedirs(carpeta_resultados, exist_ok=True)
    
    print("\nComenzando el análisis multi-modelo...")
    
    for modelo in modelos:
        print(f"\n================ MODELO: {modelo} ================")
        
        for i, prompt in enumerate(prompts, start=1):
            print(f" Ejecutando Prompt {i} (Enfoque {i})...")
            
            try:
                respuesta = ollama.generate(
                    model=modelo,
                    prompt=prompt
                )
                
                modelo_archivo = modelo.replace(":", "_").replace("/", "_").replace("\\", "_")
                nombre_archivo = os.path.join(carpeta_resultados, f"{modelo_archivo}_prompt{i}.txt")
                
                with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                    archivo.write(f"MODELO: {modelo}\n")
                    archivo.write(f"PROMPT VERSIÓN: {i}\n")
                    archivo.write("=" * 80 + "\n\n")
                    archivo.write(respuesta["response"])
                    
                print(f" [OK] Guardado en: {nombre_archivo}")
                
            except Exception as e:
                print(f" [ERROR] Falló la ejecución con {modelo} en el Prompt {i}")
                print(f" Detalle: {e}")

    print("\n¡Proceso terminado exitosamente! Revisa los archivos guardados en la carpeta 'Resultados'.")

if __name__ == "__main__":
    main()