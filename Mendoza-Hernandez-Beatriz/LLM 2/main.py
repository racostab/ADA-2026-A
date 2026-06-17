import os
import json
import ollama

from utils.pdf_reader import load_all_pdfs
from utils.prompt_loader import load_prompts

# ==========================================
# Directorio base del proyecto
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(f"BASE_DIR = {BASE_DIR}")

# ==========================================
# Cargar configuración
# ==========================================

CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

if not os.path.exists(CONFIG_FILE):
    raise FileNotFoundError(
        f"No existe config.json en:\n{CONFIG_FILE}"
    )

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

# ==========================================
# Construir rutas absolutas
# ==========================================

PDF_FOLDER = os.path.join(
    BASE_DIR,
    config["pdf_folder"]
)

PROMPT_FOLDER = os.path.join(
    BASE_DIR,
    config["prompt_folder"]
)

OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    config["output_folder"]
)

# ==========================================
# Verificaciones
# ==========================================

print(f"PDF_FOLDER     = {PDF_FOLDER}")
print(f"PROMPT_FOLDER  = {PROMPT_FOLDER}")
print(f"OUTPUT_FOLDER  = {OUTPUT_FOLDER}")

if not os.path.exists(PDF_FOLDER):
    raise FileNotFoundError(
        f"No existe la carpeta papers:\n{PDF_FOLDER}"
    )

if not os.path.exists(PROMPT_FOLDER):
    raise FileNotFoundError(
        f"No existe la carpeta prompts:\n{PROMPT_FOLDER}"
    )

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================================
# Cargar PDFs
# ==========================================

print("\nCargando PDFs...")

papers = load_all_pdfs(PDF_FOLDER)

print(f"PDFs encontrados: {len(papers)}")

if len(papers) == 0:
    raise Exception(
        f"No se encontraron PDFs en:\n{PDF_FOLDER}"
    )

# ==========================================
# Cargar prompts
# ==========================================

print("\nCargando prompts...")

prompts = load_prompts(PROMPT_FOLDER)

print(f"Prompts encontrados: {len(prompts)}")

if len(prompts) == 0:
    raise Exception(
        f"No se encontraron prompts en:\n{PROMPT_FOLDER}"
    )

# ==========================================
# Unir texto de artículos
# ==========================================

all_papers_text = "\n\n".join(
    papers.values()
)

# Limitar tamaño para no saturar contexto
MAX_CHARS = 20000

all_papers_text = all_papers_text[:MAX_CHARS]

# ==========================================
# Ejecutar modelos
# ==========================================

for model in config["models"]:

    print(f"\nEjecutando modelo: {model}")

    report = ""

    for prompt_name, prompt in prompts.items():

        print(f"  -> {prompt_name}")

        final_prompt = prompt.replace(
            "{papers}",
            all_papers_text
        )

        try:

            response = ollama.generate(
                model=model,
                prompt=final_prompt
            )

            report += (
                "\n\n"
                + "=" * 80
                + "\n"
                + prompt_name
                + "\n"
                + "=" * 80
                + "\n\n"
                + response["response"]
            )

        except Exception as e:

            report += (
                "\n\n"
                + "=" * 80
                + "\nERROR EN "
                + prompt_name
                + "\n"
                + "=" * 80
                + "\n\n"
                + str(e)
            )

    output_file = os.path.join(
        OUTPUT_FOLDER,
        f"{model}_report.txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    print(f"Reporte guardado en:\n{output_file}")

print("\nProceso terminado.")