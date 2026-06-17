# Revisión Automatizada de Literatura Científica con LLMs

Este proyecto es una herramienta en Python diseñada para automatizar el proceso de revisión del estado del arte en investigaciones y protocolos de tesis de maestría. Utiliza Modelos de Lenguaje Generativo (LLMs) ejecutados de forma local (vía [Ollama](https://ollama.com/)) para leer artículos científicos en formato PDF y responder preguntas críticas de investigación de manera estructurada.

##  Cumplimiento de los Requerimientos

Este programa fue diseñado cumpliendo estrictamente con las especificaciones y la rúbrica de la tarea:

1. **Uso de múltiples modelos**: Soporta cualquier modelo local instalado en Ollama. Por defecto, ejecuta el análisis completo realizando llamadas sucesivas a `mistral:latest`, `llama3:latest` y `gemma:latest`.
2. **Cero *Hardcoding***: Absolutamente nada está estático en el código. Las rutas de los documentos, el tema de la tesis, el planteamiento del problema y la selección de modelos se introducen dinámicamente como argumentos en la terminal.
3. **Múltiples versiones de Prompts**: Se implementó el parámetro `--prompt_version`, permitiendo al usuario alternar entre prompts directos (`v1`) y prompts con un enfoque de "persona experta/sinodal estricto" (`v2`).
4. **Procesamiento Local de PDFs**: Utiliza la librería `PyMuPDF` (`fitz`) para extraer el texto de los artículos PDF directamente en tu máquina. Ningún documento científico se envía a servidores de terceros.

##  Consideraciones importantes de añadir: Soporte con LaTeX y generador de citas BibTeX (IEEE)

Para aportar valor real a la escritura del documento de tesis de los usuarios, se diseñaron dos funcionalidades avanzadas:

- **Generación Automática de Citas BibTeX**: A partir del texto extraído, un prompt exclusivo actúa como "bibliotecario experto" para extraer los metadatos de los artículos (Autor, Título, Año, Revista) y generar sus respectivas citas en código **BibTeX** bajo el estilo **IEEE**.
- **Reporte Automático en LaTeX**: Al finalizar el análisis por parte de los LLMs, el programa ensambla las respuestas y compila automáticamente un documento `reporte_revision.tex`. Este documento incluye la estructura LaTeX adecuada (`\documentclass`, `\section`), listando los problemas encontrados, viabilidad y metodologías, así como insertando de manera impecable (mediante `verbatim`) las citas BibTeX para ser añadidas de inmediato al archivo `.bib` del usuario.

##  Uso e Instalación

### 1. Requisitos previos
- Tener [Ollama](https://ollama.com/) instalado y ejecutándose localmente.
- Descargar previamente los modelos deseados (ej. `ollama run mistral`).
- Entorno local de Python 3.

### 2. Instalación de dependencias
Clona este repositorio o ubícate en la carpeta del proyecto y ejecuta:
```bash
pip install -r requirements.txt
```

### 3. Ejecución
Para arrancar el script, debes proporcionarle el directorio raíz donde tengas tus artículos, tu tema de tesis, y el planteamiento del problema. El script buscará recursivamente todos los PDFs.

```bash
python main.py \
  --pdf_dir "rutas/a/tus/articulos" \
  --thesis_topic "Machine Learning aplicado a inferencia en grafos" \
  --problem_statement "Mejorar la inferencia en grafos muy grandes en tiempo real" \
  --models mistral:latest llama3:latest gemma:latest \
  --num_articles 4 \
  --prompt_version v2
```

## Ejemplo de Interacción con lq IA

El programa consulta internamente los artículos pasándole al modelo fragmentos contextuales. A continuación, un ejemplo ilustrativo de cómo retorna la información:

**P: Problemas de investigación no resueltos**
> **Respuesta del Modelo (Ej. Mistral)**: 
> * "No se ha abordado adecuadamente el problema del consumo excesivo de memoria computacional durante el mapeo de subgrafos dinámicos de gran tamaño."
> * "Falta de validación matemática en redes descentralizadas bajo escenarios de desconexión."
> * "Las metodologías actuales carecen de escalabilidad para arquitecturas de hardware limitado (IoT)."

**P: Evaluación de viabilidad a 18 meses**
> **Respuesta del Modelo (Ej. Llama3)**: 
> * **Veredicto:** Parcialmente Factible.
> * **Justificación:** La literatura en *Graph Neural Networks* muestra que las optimizaciones en tiempo real se logran implementar algorítmicamente en periodos de 6 a 10 meses. Sin embargo, tu planteamiento del problema no acota el hardware objetivo; probar en supercomputadoras vs Raspberry Pi alterará la factibilidad. Es real y pertinente, pero requiere acotación temporal.

**P: Generación de Cita**
> **Respuesta del Modelo**:
> ```bibtex
> @article{VisualLidar2023,
>   title={VisualLiDAR SLAM for Rover Navigation in Planetary Environments},
>   author={Smith, J. and Doe, A.},
>   journal={IEEE Robotics and Automation Letters},
>   year={2023}
> }
> ```
