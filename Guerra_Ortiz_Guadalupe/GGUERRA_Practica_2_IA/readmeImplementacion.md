# ==============================================
# Autor GGUERRA
# Proyecto desarrollado como práctica de integración de modelos de lenguaje locales y construcción de APIs compatibles con el formato de OpenAI, orientadas a asistentes de código tipo Copilot.
#
# Este sistema emula el comportamiento de herramientas como Copilot a nivel funcional (autocompletado y generación de código), sin utilizar modelos propietarios ni servicios oficiales.
# ==============================================

# ==============================================
# Objetivo:
# Implementar una API REST para generación de texto utilizando un modelo de lenguaje local (DeepSeek Coder 1.3B), ejecutado dentro de un contenedor Docker y expuesto mediante FastAPI.
#
# La API es compatible con el formato de OpenAI, permitiendo integrarse con herramientas como asistentes tipo Copilot en Visual Studio Code mediante la extensión Continue.
# ==============================================

# ==============================================
# Arquitectura
# VS Code (Continue)
#       ↓ 
# API Local (FastAPI)
#       ↓ 
# Modelo DeepSeek
#       ↓ 
# Respuesta JSON
# 
# Tecnologías utilizadas
# -: Python 3.10
# -: Transformers (Hugging Face)
# -: Docker
# -: DeepSeek Coder 1.3B
# -:Continue (VS Code Extension)
# ==============================================

# ==============================================
# Instalación del modelo
# Modelo utilizado: deepseek-ai/deepseek-coder-1.3b-instruct
#
# Clonar desde Hugging Fase:
# -: git lfs install
# -: git clone https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct
# -: cd deepseek-coder-1.3b-instruct
# -:git lfs pull
# ==============================================

# ==============================================
# La construcción del contenedor Docker
# Desde la carpeta del proyecto: "...\deepseek-api"
# -:  docker build -t deepseek-api .
# ==============================================

# ==============================================
# Ejecución del contenedor
# -: docker run -it -p 8000:8000 -v C:\Users\TuUsuario\Desktop\deepseek-coder-1.3b-instruct:/model --name deepseek-container deepseek-api
#
# Acceso a la API
# Endpoint tipo OpenAI: POST http://localhost:8000/v1/completions
# ==============================================

# ==============================================
# Estructura del proyecto --
# .
# ├── app.py
# ├── Dockerfile
# ├── requirements.txt
# └── README.md
# ==============================================

# ==============================================
# Funcionamiento interno
# 1. El usuario escribe código en VS Code
# 2. Continue envía el contexto a la API local
# 3. FastAPI procesa la solicitud
# 4. El modelo DeepSeek genera texto
# 5. Se devuelve la respuesta en formato JSON
# 6. VS Code muestra sugerencias en tiempo rea
# ==============================================

# ==============================================
# NOTAS
# .
# ├─Se requiere Docker en ejecución
# ├─El modelo puede consumir varios GB de RAM
# └─El rendimiento depende del hardware local
#
# Especificaciones del entorno de ejecución
# 
# El proyecto fue probado en el siguiente entorno:
# 
# Equipo: HP Pavilion 15-eg0xxx
# Procesador: Intel Core i7-1165G7 @ 2.80GHz
# Memoria RAM: 16 GB (3200 MT/s)
# GPU: Intel Iris Xe Graphics (integrada)
# Almacenamiento: 477 GB SSD
# 
# Consideraciones de rendimiento
# El modelo DeepSeek Coder 1.3B puede ejecutarse correctamente en CPU.
# No se requiere GPU dedicada, aunque mejora el rendimiento si está disponible.
# El consumo de memoria puede oscilar entre 2 GB y 6 GB de RAM durante la inferencia.
# El tiempo de respuesta depende del tamaño del prompt y del número de tokens generados.
# 
# Limitaciones
# El rendimiento es inferior a soluciones comerciales como GitHub Copilot.
# La generación puede ser más lenta debido a ejecución en CPU.
# No incluye entrenamiento adicional (fine-tuning).
# No tiene acceso a contexto en la nube ni repositorios completos.
# ==============================================4