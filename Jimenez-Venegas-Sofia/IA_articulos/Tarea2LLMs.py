import fitz
import ollama
import os

pdfs = [
    "A low-power 18-bit sigma-delta digital-to-analog converter.pdf",
    "Sigma-Delta Modulators Tutorial Overview, Design.pdf",
    "Next-Generation_Delta-Sigma_Converters_Trends_and_Perspectives.pdf",
    "Design and optimization of discrete-time delta-sigma modulators.pdf"
]

modelos = [
    "mistral",
    "llama3.2",
    "qwen3:4b"
]

texto_total = ""

for pdf_file in pdfs:

    if not os.path.exists(pdf_file):
        print(f"No se encontró: {pdf_file}")
        continue

    print(f"Leyendo: {pdf_file}")

    pdf = fitz.open(pdf_file)

    texto_total += f"\n\n===== ARTÍCULO: {pdf_file} =====\n\n"

    for pagina in pdf:
        texto_total += pagina.get_text()

    pdf.close()

preguntas = """
a. De estos artículos, ¿qué problemas de investigación no están resueltos?

b. Dado el planteamiento del problema siguiente:

"A pesar de los avances significativos en el diseño de convertidores analógico–digitales sigma delta, el desarrollo de arquitecturas capaces de operar a bajo voltaje de alimentación y bajo consumo de potencia continúa representando un desafío, particularmente en tecnologías CMOS"

y considerando los cuatro artículos analizados:

- ¿El problema es real?
- ¿Es pertinente?
- ¿Es factible resolverlo en un periodo de 18 meses?
- Justifica cada respuesta.

c. Para cada artículo:

- Identifica la metodología utilizada.
- Indica el nombre de la metodología.
- Resume los pasos principales empleados por los autores.

d. Si se realizara una revisión sistemática de literatura sobre Modulación Sigma Delta:

- ¿Qué referencias fundamentales deberían incluirse?
- ¿Qué autores aparecen como recurrentes?
- ¿Qué trabajos son considerados base o estado del arte según los artículos analizados?

Organiza la respuesta utilizando los encabezados:

A)
B)
C)
D)
"""

# Prompt 1

prompt1 = f"""
Eres un investigador experto en convertidores sigma-delta.

Analiza exclusivamente la información contenida en los artículos proporcionados.

ARTÍCULOS:

{texto_total}

{preguntas}
"""

# Prompt 2

prompt2 = f"""
Actúa como un investigador experto en convertidores sigma-delta y metodologías de investigación.

Realiza un análisis crítico de los artículos proporcionados.

Identifica:
- vacíos de investigación
- limitaciones
- metodologías empleadas
- oportunidades de investigación futura

ARTÍCULOS:

{texto_total}

{preguntas}
"""

# Prompt 3

prompt3 = f"""
Actúa como un experto en revisiones sistemáticas de literatura.

Analiza los artículos proporcionados y enfócate en:

- autores relevantes
- tendencias de investigación
- líneas de trabajo actuales
- problemas abiertos
- referencias fundamentales

ARTÍCULOS:

{texto_total}

{preguntas}
"""

prompts = [
    prompt1,
    prompt2,
    prompt3
]


os.makedirs("Resultados", exist_ok=True)

for modelo in modelos:

    print(f"\n===== MODELO: {modelo} =====")

    for i, prompt in enumerate(prompts, start=1):

        print(f"Ejecutando Prompt {i}...")

        try:

            respuesta = ollama.generate(
                model=modelo,
                prompt=prompt
            )

            modelo_archivo = (
                modelo.replace(":", "_")
                      .replace("/", "_")
                      .replace("\\", "_")
            )

            nombre_archivo = os.path.join(
                "Resultados",
                f"{modelo_archivo}_prompt{i}.txt"
            )

            with open(nombre_archivo, "w", encoding="utf-8") as archivo:

                archivo.write(f"MODELO: {modelo}\n")
                archivo.write(f"PROMPT: {i}\n")
                archivo.write("=" * 80 + "\n\n")

                archivo.write(respuesta["response"])

            print(f"Guardado: {nombre_archivo}")

        except Exception as e:

            print(f"Error con {modelo} Prompt {i}")
            print(e)

print("\nProceso terminado.")