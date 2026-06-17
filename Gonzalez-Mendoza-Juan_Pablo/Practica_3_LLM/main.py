import argparse
import os
import json
from pdf_processor import get_pdf_files, process_pdfs
from llm_agent import generate_prompts, query_llm

def generate_latex_report(results, thesis_topic, output_file="reporte_revision.tex"):
    """
    Genera un archivo LaTeX estructurado usando los resultados del primer modelo evaluado,
    incluyendo el bloque de citas BibTeX en la sección correspondiente.
    """
    if not results:
        return
        
    # Usamos los resultados del primer modelo como representativos para el reporte
    first_model = list(results.keys())[0]
    data = results[first_model]
    
    latex_content = f"""\\documentclass[12pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[spanish]{{babel}}
\\usepackage{{hyperref}}
\\usepackage{{geometry}}
\\geometry{{margin=2.5cm}}

\\title{{Reporte de Revisión de Literatura Automático\\\\
\\large Generado con Modelos de Lenguaje (LLM)}}
\\author{{Análisis del Estado del Arte}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\section*{{Tema de Tesis}}
{thesis_topic}

\\section{{Problemas de Investigación no Resueltos}}
{data.get("A_Problemas_No_Resueltos", "No disponible")}

\\section{{Viabilidad del Problema}}
{data.get("B_Viabilidad_Problema", "No disponible")}

\\section{{Metodologías Identificadas}}
{data.get("C_Metodologias", "No disponible")}

\\section{{Recomendaciones para Revisión Sistemática}}
{data.get("D_Revision_Sistematica", "No disponible")}

\\section{{Citas Generadas (BibTeX - Formato IEEE)}}
\\begin{{verbatim}}
{data.get("E_Generar_Cita", "No se generaron citas.")}
\\end{{verbatim}}

\\end{{document}}
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(latex_content)
    print(f"\\n[+] Reporte LaTeX generado exitosamente en '{output_file}'.")

def parse_args():
    parser = argparse.ArgumentParser(description="Automatización de Revisión de Documentos Científicos con LLMs")
    parser.add_argument("--pdf_dir", type=str, required=True, help="Ruta al directorio que contiene los PDFs (y subcarpetas).")
    parser.add_argument("--thesis_topic", type=str, required=True, help="Tema de la tesis.")
    parser.add_argument("--problem_statement", type=str, required=True, help="Planteamiento del problema de la tesis.")
    parser.add_argument("--models", type=str, nargs='+', default=["mistral:latest", "llama3:latest", "gemma:latest"], help="Lista de modelos locales de Ollama a utilizar.")
    parser.add_argument("--num_articles", type=int, default=4, help="Número de artículos a procesar (mínimo 4 según requisitos).")
    parser.add_argument("--prompt_version", type=str, choices=["v1", "v2"], default="v1", help="Versión de los prompts a utilizar (v1=Directos, v2=Experto).")
    return parser.parse_args()

def main():
    args = parse_args()

    print(f"Buscando artículos en: {args.pdf_dir}")
    pdf_paths = get_pdf_files(args.pdf_dir, limit=args.num_articles)
    
    if len(pdf_paths) < 1:
        print("No se encontraron archivos PDF en la ruta proporcionada.")
        return
        
    print(f"Se seleccionaron {len(pdf_paths)} artículos para revisar.")
    
    # 1. Extraer texto de los PDFs
    articles_text = process_pdfs(pdf_paths)
    
    # 2. Generar los prompts para las 4 actividades
    print(f"\nGenerando prompts (Versión: {args.prompt_version})...")
    prompts = generate_prompts(args.thesis_topic, args.problem_statement, articles_text, version=args.prompt_version)
    
    results = {}
    
    # 3. Consultar a los modelos
    for model in args.models:
        print(f"\n==========================================")
        print(f"Evaluando con el modelo: {model}")
        print(f"==========================================")
        
        model_results = {}
        for task_id, prompt in prompts.items():
            print(f"\n-> Ejecutando actividad: {task_id}")
            response = query_llm(model, prompt)
            model_results[task_id] = response
            print(f"Respuesta:\n{response}\n")
            
        results[model] = model_results
        
    # Guardar resultados en un archivo
    with open("resultados_revision.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print("\nProceso terminado. Resultados guardados en 'resultados_revision.json'.")
    
    # 4. Generar reporte LaTeX con formato IEEE
    generate_latex_report(results, args.thesis_topic)

if __name__ == "__main__":
    main()
