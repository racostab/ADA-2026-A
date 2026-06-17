import os
import fitz  # PyMuPDF

def get_pdf_files(root_dir, limit=4):
    """
    Busca recursivamente archivos PDF en el directorio dado y retorna una lista de rutas.
    Limitado a 'limit' cantidad de artículos para esta prueba (por defecto 4).
    """
    pdf_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.lower().endswith('.pdf'):
                pdf_paths.append(os.path.join(dirpath, f))
                if len(pdf_paths) >= limit:
                    return pdf_paths
    return pdf_paths

def extract_text_from_pdf(pdf_path):
    """
    Extrae el texto de un archivo PDF usando PyMuPDF.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
    except Exception as e:
        print(f"Error al leer {pdf_path}: {e}")
    return text

def process_pdfs(pdf_paths):
    """
    Procesa una lista de PDFs y retorna un diccionario con el texto de cada uno.
    """
    documents = {}
    for path in pdf_paths:
        print(f"Extrayendo texto de: {path}")
        documents[os.path.basename(path)] = extract_text_from_pdf(path)
    return documents
