import fitz
import os

def extract_pdf_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    return text


def load_all_pdfs(folder):

    papers = {}

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            path = os.path.join(folder, file)

            papers[file] = extract_pdf_text(path)

    return papers