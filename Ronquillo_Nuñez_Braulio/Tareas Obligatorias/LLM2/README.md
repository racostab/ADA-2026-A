# LLM2 - Revision cientifica con modelos locales

Aplicacion local para la segunda tarea de Programacion con LLMs. El objetivo es usar modelos locales para revisar articulos cientificos relacionados con el tema:

```text
Estudio del lenguaje natural usando redes complejas y analisis topologico de datos
```

## Ruta del programa

La carpeta que debes abrir en terminal es:

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
```

El archivo principal para ejecutar el dashboard es:

```text
Tareas Obligatorias/LLM2/run_dashboard.py
```

## Que hace

- Procesa localmente PDFs cientificos.
- Usa modelos locales por Ollama.
- Ejecuta 5 versiones de prompt.
- Evalua actividades de revision academica:
  - Problemas no resueltos.
  - Pertinencia y factibilidad en 18 meses.
  - Metodologias usadas.
  - Referencias para una revision sistematica.
- Muestra resultados en tablas HTML.
- Guarda resultados en `DAT/outputs/`.
- Si Ollama no esta disponible, usa un fallback demo para que el front no falle.

## Estado de articulos

La tarea pide al menos 4 articulos. En `config.json` quedaron configurados los 3 articulos disponibles:

1. `A multiplex analysis of phonological and orthographic networks`
2. `Simplicial complex entropy for time series analysis`
3. `Evaluating the Irregularity of Natural Languages`

El dashboard muestra una advertencia mientras falte el cuarto articulo.

## Opcion A: ejecutar con Ollama real

Usa esta opcion si quieres respuestas reales de modelos locales.

### 1. Entrar a la carpeta

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
```

### 2. Instalar dependencias de Ubuntu

```bash
sudo apt update
sudo apt install python3-venv python3-pip poppler-utils curl
```

`poppler-utils` instala `pdftotext`, usado como respaldo para extraer texto de PDFs.

### 3. Crear y activar entorno virtual

```bash
python3 -m venv .venv-linux
source .venv-linux/bin/activate
```

Cuando el entorno esta activo, la terminal debe mostrar algo parecido a:

```text
(.venv-linux) usuario@equipo
```

### 4. Instalar librerias de Python

```bash
pip install -r requirements.txt
```

Si esta carpeta fue movida desde otra ubicacion, recrea el entorno virtual antes de instalar dependencias:

```bash
deactivate 2>/dev/null
mv .venv-linux .venv-linux-viejo
python3 -m venv .venv-linux
source .venv-linux/bin/activate
pip install -r requirements.txt
```

### 5. Instalar Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 6. Descargar los modelos

```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
ollama pull gemma2:2b
```

Los nombres de modelos usados por el programa estan en `config.json`.

### 7. Verificar que Ollama este corriendo

Primero revisa si responde:

```bash
curl http://localhost:11434/api/tags
```

Si no responde, levanta Ollama en otra terminal:

```bash
ollama serve
```

Despues vuelve a probar:

```bash
curl http://localhost:11434/api/tags
```

Si aparece una respuesta JSON con modelos, Ollama ya esta listo.

### 8. Ejecutar el dashboard

En la terminal donde activaste `.venv-linux`:

```bash
python run_dashboard.py
```

Abre en el navegador:

```text
http://127.0.0.1:8010
```

Para detener el servidor, presiona:

```text
Ctrl + C
```

## Opcion B: ejecutar sin Ollama

Usa esta opcion para probar el front aunque no haya modelos instalados.

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
source .venv-linux/bin/activate
python run_dashboard.py
```

Abre:

```text
http://127.0.0.1:8010
```

En el front puedes activar:

```text
Simular sin Ollama
```

Ademas, si Ollama no esta instalado o no esta corriendo, la aplicacion marca las filas como `fallback` y genera respuestas demo. Esto permite mostrar el sistema aunque el equipo no tenga modelos locales.

## Opcion C: entregar sin instalar nada

Si                                     no quiere instalar Python, Ollama ni dependencias, usa el reporte HTML estatico ya generado:

```text
Tareas Obligatorias/LLM2/reporte_llm2_demo.html
```

Ese archivo se abre directo con doble clic en el navegador.

Importante: ese reporte es demo. Sirve para mostrar la interfaz y las tablas, pero no ejecuta modelos locales. Para respuestas reales se necesita la opcion A con Ollama.

Si quieres regenerar el HTML estatico:

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
source .venv-linux/bin/activate
python export_static_report.py
```

Genera:

```text
reporte_llm2_demo.html
```

## Ejecuciones posteriores

Cuando ya instalaste todo una vez, para volver a correr el programa solo necesitas:

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
source .venv-linux/bin/activate
python run_dashboard.py
```

Y abrir:

```text
http://127.0.0.1:8010
```

Si quieres usar modelos reales, recuerda que Ollama debe estar activo:

```bash
ollama serve
```

## Configuracion

Edita `config.json` para cambiar:

- Tema de tesis.
- Planteamiento del problema.
- Rutas de PDFs.
- Modelos de Ollama.
- Actividades de revision.
- Activar o desactivar el fallback demo con `fallback_to_demo`.

## Estructura

```text
LLM2/
  config.json
  requirements.txt
  run_dashboard.py
  export_static_report.py
  reporte_llm2_demo.html
  DAT/
    prompts/
    processed/
    outputs/
  SRC/
    app.py
    analyzer.py
    config.py
    ollama_client.py
    pdf_processor.py
```

## Nota sobre no hardcodear

Los modelos, rutas de documentos, URL de Ollama, tema y actividades se cargan desde `config.json`. Las versiones de prompt se cargan desde `DAT/prompts/`.
