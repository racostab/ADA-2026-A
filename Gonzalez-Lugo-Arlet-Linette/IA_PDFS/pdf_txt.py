import os
import pdfplumber

CARPETA_ENTRADA = "DOCS"
CARPETA_SALIDA = "TXT"

def convertir_pdf_a_txt(ruta_pdf, ruta_txt):
    texto = ""

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            contenido = pagina.extract_text()
            if contenido:
                texto += contenido + "\n"

    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(texto)


def main():
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)
        
    for archivo in os.listdir(CARPETA_ENTRADA):
        if archivo.endswith(".pdf"):
            ruta_pdf = os.path.join(CARPETA_ENTRADA, archivo)
            nombre_txt = archivo.replace(".pdf", ".txt")
            ruta_txt = os.path.join(CARPETA_SALIDA, nombre_txt)

            print(f"Convirtiendo: {archivo}...")
            convertir_pdf_a_txt(ruta_pdf, ruta_txt)

    print("\n Todos los PDFs fueron convertidos a TXT.")


if __name__ == "__main__":
    main()