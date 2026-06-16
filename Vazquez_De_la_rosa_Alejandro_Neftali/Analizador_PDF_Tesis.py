import os
import requests
import PyPDF2
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL")
MODELOS = os.getenv("MODELOS_DISPONIBLES", "").split(",")
DIR_PDFS = os.getenv("DIRECTORIO_PDFS", "./articulos_tesis")
TEMA_TESIS = os.getenv("TEMA_TESIS", "Mi Tema de Tesis")
PROBLEM_STATEMENT = os.getenv("PROBLEM_STATEMENT", "Mi problema de investigación")
DIR_RESULTADOS = "./resultados" # Nueva carpeta para guardar los reportes

# --- FUNCIONES DE PROCESAMIENTO LOCAL ---
def extraer_texto_pdf(ruta_archivo):
    texto = ""
    try:
        with open(ruta_archivo, 'rb') as archivo:
            lector = PyPDF2.PdfReader(archivo)
            paginas = min(3, len(lector.pages)) 
            for i in range(paginas):
                texto += lector.pages[i].extract_text() + "\n"
    except Exception as e:
        print(f"Error procesando {ruta_archivo}: {e}")
    return texto

def obtener_pdfs(directorio):
    if not os.path.exists(directorio):
        os.makedirs(directorio)
        print(f"Por favor, coloca tus artículos en la carpeta: {directorio}")
        return []
    return [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.pdf')]

# --- CONEXIONES A LOS MODELOS ---
def consultar_grok_api(modelo, prompt, contexto=""):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}", 
        "Content-Type": "application/json"
    }
    mensaje_usuario = f"Contexto del artículo:\n{contexto}\n\nPregunta:\n{prompt}" if contexto else prompt
    data = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Eres un asistente académico experto en revisión de literatura científica."},
            {"role": "user", "content": mensaje_usuario}
        ],
        "temperature": 0.3 
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            return f"Error HTTP Grok: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error de conexión con Grok API: {e}"

def consultar_ollama_tailscale(modelo, prompt, contexto=""):
    prompt_completo = f"Contexto del artículo:\n{contexto}\n\nPregunta:\n{prompt}" if contexto else prompt
    payload = {
        "model": modelo,
        "prompt": prompt_completo,
        "stream": False,
        "options": {"temperature": 0.3}
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return f"Error HTTP Ollama: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error de red con Tailscale: {e}"

def consultar_llm(modelo, prompt, contexto=""):
    if "grok" in modelo.lower():
        return consultar_grok_api(modelo, prompt, contexto)
    else:
        return consultar_ollama_tailscale(modelo, prompt, contexto)

# --- DEFINICIÓN DE PROMPTS ---
PROMPTS = {
    "problemas_no_resueltos": [
        "Versión A: De este artículo científico, ¿qué problemas de investigación se mencionan explícitamente como no resueltos o como trabajo futuro?",
        "Versión B: Analiza el texto e identifica las brechas de conocimiento (research gaps) o limitaciones que los autores proponen para investigaciones futuras."
    ],
    "factibilidad_problema": [
        f"Versión A: Dado este planteamiento del problema: '{PROBLEM_STATEMENT}' y el contexto del artículo ingresado, evalúa: ¿el problema es real, pertinente y factible de resolver en 18 meses para una maestría?",
        f"Versión B: Actúa como un sinodal de tesis. Considerando la literatura adjunta y mi problema de investigación ('{PROBLEM_STATEMENT}'), emite un juicio crítico sobre su viabilidad para ser completado en 18 meses."
    ],
    "metodologia": [
        "Versión A: De este artículo, ¿qué metodología se usó? Dame el nombre de la metodología y una lista resumida de los pasos en formato de viñetas.",
        "Versión B: Extrae la arquitectura o diseño metodológico del documento. Proporciona el nombre técnico de la metodología y un resumen secuencial."
    ],
    "revision_sistematica": [
        f"Versión A: Para realizar una revisión sistemática del tema '{TEMA_TESIS}', ¿qué referencias bibliográficas citadas en este documento se deben considerar indispensables?",
        f"Versión B: Revisa las citas de este documento. Si fueras a hacer un 'Survey' sobre '{TEMA_TESIS}', ¿cuáles 3 referencias clave de este texto usarías?"
    ]
}

# --- FUNCIONES DE ESCRITURA ---
def guardar_reporte(archivo, contenido):
    """Guarda el contenido en un archivo (modo append para ir agregando)."""
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(contenido + "\n\n")

# --- EJECUCIÓN PRINCIPAL ---
def main():
    pdfs = obtener_pdfs(DIR_PDFS)
    if len(pdfs) < 4:
        print(f"Atención: Se encontraron {len(pdfs)} PDFs. La tarea requiere al menos 4.")
    if not pdfs:
        return

    # Crear carpeta de resultados si no existe
    if not os.path.exists(DIR_RESULTADOS):
        os.makedirs(DIR_RESULTADOS)

    print("=== INICIANDO REVISIÓN AUTOMATIZADA ===")
    
    for modelo in MODELOS:
        modelo = modelo.strip()
        if not modelo:
            continue
            
        print(f"\n Procesando con el modelo: {modelo}")
        
        # Nombre del archivo de salida para este modelo
        nombre_limpio = modelo.replace(":", "_").replace("-", "_")
        archivo_salida = os.path.join(DIR_RESULTADOS, f"reporte_{nombre_limpio}.md")
        
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(f"# Reporte de Revisión de Literatura\n**Modelo utilizado:** `{modelo}`\n\n---\n\n")
        
        for indice, pdf_ruta in enumerate(pdfs):
            nombre_archivo = os.path.basename(pdf_ruta)
            print(f"Analizando artículo: {nombre_archivo}")
            
            guardar_reporte(archivo_salida, f"## Documento: {nombre_archivo}")
            
            texto_pdf = extraer_texto_pdf(pdf_ruta)
            if not texto_pdf:
                guardar_reporte(archivo_salida, "*Error: No se pudo extraer texto del documento.*")
                continue
                
            version_prompt = indice % 2 
            
            tareas = [
                ("a) Problemas no resueltos", "problemas_no_resueltos"),
                ("b) Factibilidad del Problema (18 meses)", "factibilidad_problema"),
                ("c) Metodología y Pasos", "metodologia"),
                ("d) Referencias para Revisión Sistemática", "revision_sistematica")
            ]
            
            for titulo_tarea, clave_prompt in tareas:
                prompt_usado = PROMPTS[clave_prompt][version_prompt]
                
                guardar_reporte(archivo_salida, f"### {titulo_tarea}\n**Prompt utilizado:** _{prompt_usado}_\n\n**Respuesta del modelo:**\n")
                
                resp = consultar_llm(modelo, prompt_usado, texto_pdf)
                
                respuesta_formateada = "\n".join([f"> {linea}" for linea in resp.split("\n")])
                
                guardar_reporte(archivo_salida, respuesta_formateada)

                print(f"    -> Tarea '{titulo_tarea}' completada.")

    print(f"\n Proceso terminado. Los resultados se han guardado en la carpeta: {DIR_RESULTADOS}")

if __name__ == "__main__":
    main()
    