import os
import argparse
import yaml
from pypdf import PdfReader

from langchain_community.llms import Ollama

def cargar_configuracion(ruta_config="config.yaml"):
    """Carga la configuración externa"""
    with open(ruta_config, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def extraer_texto_pdf(ruta_pdf):
    """Procesa y extrae el texto de un PDF de forma local."""
    if not os.path.exists(ruta_pdf):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_pdf}")
    
    reader = PdfReader(ruta_pdf)
    texto_completo = ""
    for pagina in reader.pages:
        texto_completo += pagina.extract_text() + "\n"
    return texto_completo

def main():
    #Parámetro único en consola para simplificar el comando Bash
    parser = argparse.ArgumentParser(description="Revisión científica individualizada por artículo con Ollama.")
    parser.add_argument("--modelo", type=str, required=True, help="Nombre del modelo en Ollama (ej: llama3)")
    
    args = parser.parse_args()
    config = cargar_configuracion()
    
    #1. Obtener la lista de PDFs desde la carpeta configurada
    carpeta = config["documentos"]["carpeta_pdfs"]
    archivos_pdf = [os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith('.pdf')]
    
    if len(archivos_pdf) < 4:
        print(f"Alerta: Se encontraron {len(archivos_pdf)} PDFs. El requerimiento de la tarea exige al menos 4.")
        if len(archivos_pdf) == 0:
            print("Error: No hay PDFs en la carpeta. Proceso abortado.")
            return

    print(f"Se encontraron {len(archivos_pdf)} documentos en '{carpeta}'. Iniciando análisis individual...")
    
    #2. Inicializar Ollama
    print(f"Inicializando Ollama con el modelo local '{args.modelo}'...")
    llm = Ollama(model=args.modelo)
    
    prompts_config = config["prompts"]
    reporte_final = []

    #Encabezado general del archivo de salida
    reporte_final.append(f"========================================================")
    reporte_final.append(f"REPORTE DETALLADO DE REVISIÓN CIENTÍFICA POR ARTÍCULO")
    reporte_final.append(f"Modelo utilizado: {args.modelo} (Plataforma: Ollama Local)")
    reporte_final.append(f"========================================================\n")

    #3. Bucle principal: Analizar cada artículo de forma independiente
    for i, ruta in enumerate(archivos_pdf, start=1):
        nombre_archivo = os.path.basename(ruta)
        print(f"\n [{i}/{len(archivos_pdf)}] Procesando: {nombre_archivo}...")
        
        try:
            #Extraer y recortar el texto del artículo actual 
            texto_articulo = extraer_texto_pdf(ruta)
            texto_recortado = texto_articulo[:10000] 
            
            #Encontrando el tema y planteamiento del artículo
            print(f"Detectando tema y planteamiento para {nombre_archivo}...")
            
            prompt_auto_tema = f"Analiza el siguiente texto de un artículo científico e identifica el tema principal de investigación en una frase muy corta (máximo 5 palabras):\n\n{texto_recortado}"
            tema_detectado = llm.invoke(prompt_auto_tema).strip().replace('"', '')
            
            prompt_auto_problema = f"Analiza el siguiente artículo y genera un planteamiento del problema (problem statement) conciso (un párrafo corto) que describa el desafío que intenta resolver:\n\n{texto_recortado}"
            planteamiento_detectado = llm.invoke(prompt_auto_problema).strip().replace('"', '')
            # -----------------------------------------------------------------

            #Separador por artículo en el reporte escrito
            reporte_final.append(f"--------------------------------------------------------")
            reporte_final.append(f"ARTÍCULO {i}: {nombre_archivo}")
            reporte_final.append(f"Tema detectado: {tema_detectado}")
            reporte_final.append(f"--------------------------------------------------------\n")

            #Actividad A
            print(" Ejecutando Actividad A: Problemas no resueltos...")
            p_a = prompts_config["actividad_a"].format(texto=texto_recortado)
            resp_a = llm.invoke(p_a)
            reporte_final.append(f"A) Problemas de investigación no resueltos:\n{resp_a}\n")

            #Actividad B
            print(" Ejecutando Actividad B: Validación del problema...")
            p_b = prompts_config["actividad_b"].format(planteamiento=planteamiento_detectado, texto=texto_recortado)
            resp_b = llm.invoke(p_b)
            reporte_final.append(f"B) Respuesta al problema planteado:\n{resp_b}\n")

            #Actividad C
            print(" Ejecutando Actividad C: Metodología utilizada...")
            p_c = prompts_config["actividad_c"].format(texto=texto_recortado)
            resp_c = llm.invoke(p_c)
            reporte_final.append(f"C) Metodología utilizada:\n{resp_c}\n")

            #Actividad D
            print(" Ejecutando Actividad D: Referencias fundamentales...")
            p_d = prompts_config["actividad_d"].format(tema=tema_detectado, texto=texto_recortado)
            resp_d = llm.invoke(p_d)
            reporte_final.append(f"D) Referencias fundamentales, autores recurrentes y trabajos considerados base o estado del arte:\n{resp_d}\n")

        except Exception as e:
            print(f" Error al procesar el artículo {nombre_archivo}: {e}")
            reporte_final.append(f" No se pudo analizar el artículo {nombre_archivo} debido a un error: {e}\n")

    #4. Guardar reporte en el archivo de texto .txt
    texto_final = "\n".join(reporte_final)
    
    # Lógica para generar el nombre dinámico con el modelo y el contador incremental
    contador = 1
    while True:
        nombre_dinamico = f"analisis_{args.modelo}_{contador}.txt"
        if not os.path.exists(nombre_dinamico):
            ruta_salida = nombre_dinamico
            break
        contador += 1
    
    try:
        with open(ruta_salida, "w", encoding="utf-8") as f_out:
            f_out.write(texto_final)
        print(f"\n Análisis finalizado con éxito. El reporte de todos los artículos se guardó en: '{ruta_salida}'")
    except Exception as e:
        print(f" Error al escribir el archivo de salida TXT: {e}")

if __name__ == "__main__":
    main()