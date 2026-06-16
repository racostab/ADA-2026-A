import os
import re
import requests
import json
from typing import List
import PyPDF2

#-------------------------- Procesar Archivos -----------------------
def procesar_arch(texto):
   
    texto_limpio = re.sub(r'\s+', ' ', texto)
    resultado = ""
    
    abstract_match = re.search(r'(?i)\b(abstract|resumen)\b(.*?)(?=\b(introduction|1\.\s*intro|background)\b)', texto_limpio)
    if abstract_match:
        resultado += "- ABSTRACT\n" + abstract_match.group(2).strip() + "\n\n"
        
    metodologia_match = re.search(r'(?i)\b(methodology|methods|proposed method|architecture)\b(.*?)(?=\b(results|experiments|discussion|4\.\s*results)\b)', texto_limpio)
    if metodologia_match:
        resultado += "- METODOLOGÍA\n" + metodologia_match.group(2).strip() + "\n\n"
        
    conclusiones_match = re.search(r'(?i)\b(conclusions?|concluding remarks)\b(.*?)(?=\b(acknowledgements?|references?|bibliography)\b)', texto_limpio)
    if conclusiones_match:
        resultado += "- CONCLUSIONES\n" + conclusiones_match.group(2).strip() + "\n\n"
        
    referencias_match = re.search(r'(?i)\b(references?|bibliography)\b(.*)', texto_limpio)
    if referencias_match:
        resultado += "- REFERENCIAS\n" + referencias_match.group(2).strip()[:5000] + "\n\n"
        
    if len(resultado) < 500:
        return texto_limpio 
        
    return resultado

#-------------------------- Cargar Articulos ---------------------------
def get_test_files(directory):
    articulos = []
    base_path = os.path.join(os.getcwd(), directory)
    
    archivos_pdf = [f for f in os.listdir(base_path) if f.lower().endswith(".pdf")]
    
    if not archivos_pdf:
        return articulos

    for filename in archivos_pdf:
        file_path = os.path.join(base_path, filename)
        try:
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
                
                texto = procesar_arch(text)
                
                nombre_base = os.path.splitext(filename)[0]
                ruta_txt = os.path.join("resultados", "textos_extraidos", f"{nombre_base}_selectivo.txt")
                save_res(texto, ruta_txt)
                
                articulos.append({
                    "filename": filename,
                    "text": texto 
                })
                
                
        except Exception as e:
            print(f"Error {filename}: {e}")
            
    return articulos

#-------------------------- Guardar Respuesta --------------------------
def save_res(res, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(res)

#---------------------------- Main -------------------------------------

local  = "localhost"
remote = "100.113.158.78"

urls = [ "http://"+ local  +":11434/api/generate",
         "http://"+ remote +":11434/api/generate",
       ]

models = [ "qwen3:8B",
           "deepseek-r1:7b",
           "gemma4:12b"  
         ]


prompt = [
    ("Eres un investigador cientifico experto. Revisa la siguiente información extraída de varios artículos científicos "
     "acerca de arquitecturas neuromorficas que implementen SNN's en chips con neuronas analogicas tipo LIF.\n\n"
     "Responde a las siguientes 4 preguntas de forma concreta y detallada:\n"
     "1. De cada articulo, ¿Cuales son los problemas de investigacion que no estan resueltos?\n"
     "2. Dado el siguiente planteamineto del problema, ¿El problema es real, pertinente y factible de resolver en 18 meses?\n"
     "Planteamiento del problema: Se plantea abordar el problema mediante el diseño de una arquitectura neuromórfica en tecnología CMOS SKY130, compuesta por neuronas analógicas del tipo LIF y sinapsis memresistivas, "
     "que inicialmente presenta una topología de conectividad densa (fully connected). Utilizando compuertas de transmisión analógicas que permiten conectar o desconectar neuronas de una capa sucesora a una neurona de una capa anterior, "
     "lo cual requiere diseñar un sistema digital de control. Permitiendo así optimizar los recursos en función de la aplicación de la red.\n"
     "3. De cada uno de los articulos, ¿Cual es la metodologia que utiliza? Da en una lista el nombre de cada uno de los pasos asi como una descrpcion resumida de cada paso.\n"
     "4. ¿Qué referencias o bibliografía de los artículos analizados son especialmente relevantes para nuestra investigación? Identifícalas y justifica por qué.\n\n"),
     
    ("Eres un ingeniero principal de diseño de hardware experto en tecnología CMOS SKY130 y sistemas embebidos. Revisa la siguiente información extraída de varios artículos científicos "
     "acerca de arquitecturas neuromorficas que implementen SNN's en chips con neuronas analogicas tipo LIF, evaluando específicamente la viabilidad técnica.\n\n"
     "Responde a las siguientes 4 preguntas de forma concreta y detallada:\n"
     "1. De cada articulo, ¿Cuales son los problemas de investigacion que no estan resueltos?\n"
     "2. Dado el siguiente planteamineto del problema, ¿El problema es real, pertinente y factible de resolver en 18 meses?\n"
     "Planteamiento del problema: Se plantea abordar el problema mediante el diseño de una arquitectura neuromórfica en tecnología CMOS SKY130, compuesta por neuronas analógicas del tipo LIF y sinapsis memresistivas, "
     "que inicialmente presenta una topología de conectividad densa (fully connected). Utilizando compuertas de transmisión analógicas que permiten conectar o desconectar neuronas de una capa sucesora a una neurona de una capa anterior, "
     "lo cual requiere diseñar un sistema digital de control. Permitiendo así optimizar los recursos en función de la aplicación de la red.\n"
     "3. De cada uno de los articulos, ¿Cual es la metodologia que utiliza? Da en una lista el nombre de cada uno de los pasos asi como una descrpcion resumida de cada paso.\n"
     "4. ¿Qué referencias o bibliografía de los artículos analizados son especialmente relevantes para nuestra investigación? Identifícalas y justifica por qué.\n\n"),
 
    ("Eres un revisor académico (Peer Reviewer) altamente crítico y exigente del IEEE. Revisa la siguiente información extraída de varios artículos científicos "
     "acerca de arquitecturas neuromorficas que implementen SNN's en chips con neuronas analogicas tipo LIF, enfocándote en identificar las brechas metodológicas rigurosamente.\n\n"
     "Responde a las siguientes 4 preguntas de forma concreta y detallada:\n"
     "1. De cada articulo, ¿Cuales son los problemas de investigacion que no estan resueltos?\n"
     "2. Dado el siguiente planteamineto del problema, ¿El problema es real, pertinente y factible de resolver en 18 meses?\n"
     "Planteamiento del problema: Se plantea abordar el problema mediante el diseño de una arquitectura neuromórfica en tecnología CMOS SKY130, compuesta por neuronas analógicas del tipo LIF y sinapsis memresistivas, "
     "que inicialmente presenta una topología de conectividad densa (fully connected). Utilizando compuertas de transmisión analógicas que permiten conectar o desconectar neuronas de una capa sucesora a una neurona de una capa anterior, "
     "lo cual requiere diseñar un sistema digital de control. Permitiendo así optimizar los recursos en función de la aplicación de la red.\n"
     "3. De cada uno de los articulos, ¿Cual es la metodologia que utiliza? Da en una lista el nombre de cada uno de los pasos asi como una descrpcion resumida de cada paso.\n"
     "4. ¿Qué referencias o bibliografía de los artículos analizados son especialmente relevantes para nuestra investigación? Identifícalas y justifica por qué.\n\n")
]

print("Ejecucion de Modelo:")
print("0 - Local (localhost)")
print("1 - Remoto (100.113.158.78)")
try:
    opcion_url = int(input().strip())
    if opcion_url not in [0, 1]:
        print("Opción inválida. Se usará Local (0) por defecto.")
        opcion_url = 0
except ValueError:
    print("Entrada inválida. Se usará Local (0) por defecto.")
    opcion_url = 0

url = urls[opcion_url]

dir_input = input("Ingresar direccion de carpeta con articulos, por defecto (snn_chips): \n").strip()
articulos = dir_input if dir_input else "snn_chips"
print(f"\nCarpeta seleccionada: {articulos}\n")

print("Lista de modelos: ")
n_mod = len(models)
for k in range(n_mod):
    print(f"{k+1} - {models[k]}")
    
print("\nColoque el numero de cada modelo que desea usar separado por espacios:")
try:
    sel_mod = list(map(int,input().split()))
except ValueError:
    print("Entrada inválida. Ingrese números enteros.")
    exit()

n_modelos = len(sel_mod)

list_articulos = get_test_files(articulos)

if not list_articulos:
    print("Sin articulos")
    exit()

for i in range(n_modelos):
    modelo_actual = models[sel_mod[i] - 1]
    model_name = modelo_actual.replace(':', '_')
    
    
    print(f"*** INICIANDO PROCESO: {modelo_actual} ***")
    

    # Juntar articulos
    articulos_comb = ""
    for art in list_articulos:
        articulos_comb += f"\n\n--- INICIO ARTÍCULO: {art['filename']} ---\n"
        articulos_comb += art['text']
        articulos_comb += f"\n--- FIN ARTÍCULO: {art['filename']} ---\n"
        
    if articulos_comb.strip():
        art_limit = articulos_comb[:50000]      # Limitar contenido de los articulos
        
        txt_resp = f"MODELO UTILIZADO: {modelo_actual}\n\n"
        
        # Respuesta por Prompt
        for j, prompt_act in enumerate(prompt):
            print(f"- Generando Respuesta {j+1}/3 ...")
            
            prompt_f = (
                prompt_act +"A CONTINUACIÓN SE PRESENTAN LOS TEXTOS DE LOS ARTÍCULOS:\n" +art_limit+
                "\n\n[RECORDATORIO IMPORTANTE]: Responde de manera profesional y detallada en español a las 4 preguntas planteadas basándote ÚNICAMENTE en los textos proporcionados."
            )

            payload = {
                "model": modelo_actual,
                "prompt": prompt_f,
                "stream": False,
                "options": {
                    "num_ctx": 16384,
                    "temperature": 0.3 
                }
            }

            try:
                response = requests.post(url, json=payload)
                response.raise_for_status()
                texto_final = response.json().get("response", "Sin respuesta.")
                
                # Armar respuesta pata .txt
                txt_resp += f"RESPUESTA {j+1}\n"
                txt_resp += f"---------------------------------------------------\n\n"
                txt_resp += texto_final + "\n\n"
                
            except Exception as e:
                print(f"Error con el modelo {modelo_actual}: {e}")
                
        # Guardar archivo con las 3 respuestas juntas
        file_name = f"resultados/res_invest_{model_name}.txt"
        save_res(txt_resp, file_name)
        print("\nRespuestas obtenidas")

    else:
        print("Sin texto")

print("\nFin del Proceso")