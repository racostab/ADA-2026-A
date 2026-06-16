# LLM2 - Revision cientifica con Mistral, Gemini y Claude

Aplicacion local para la segunda tarea de Programacion con LLMs. El objetivo es revisar articulos cientificos relacionados con el tema:

```text
Estudio del lenguaje natural usando redes complejas y analisis topologico de datos
```

Ahora el proyecto usa APIs externas en lugar de Ollama local:

- Mistral / Le Chat
- Google Gemini
- Anthropic Claude

## Ruta del programa

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
```

## Primera ejecucion

Instala dependencias de Ubuntu:

```bash
sudo apt update
sudo apt install python3-venv python3-pip poppler-utils
```

Crea o recrea el entorno virtual:

```bash
python3 -m venv .venv-linux
source .venv-linux/bin/activate
pip install -r requirements.txt
```

Si la carpeta fue movida y el entorno virtual falla, recrealo:

```bash
deactivate 2>/dev/null
mv .venv-linux .venv-linux-viejo
python3 -m venv .venv-linux
source .venv-linux/bin/activate
pip install -r requirements.txt
```

## Configurar API keys

Copia el ejemplo:

```bash
cp .env.example .env
```

Edita `.env`:

```text
MISTRAL_API_KEY=tu_llave_de_mistral
GEMINI_API_KEY=tu_llave_de_gemini
ANTHROPIC_API_KEY=tu_llave_de_anthropic
```

Puedes poner solo una llave si solo vas a probar un proveedor. Por ejemplo, si solo tienes Gemini, llena `GEMINI_API_KEY` y en el dashboard selecciona solo Gemini.

El archivo `.env` no se debe subir al repo. El `.gitignore` ya lo ignora.

## Ejecutar dashboard

```bash
cd "/home/acid/Escritorio/Proyectos primer semestre/ADA-2026-A/Ronquillo_Nuñez_Braulio/Tareas Obligatorias/LLM2"
source .venv-linux/bin/activate
python run_dashboard.py
```

Abre:

```text
http://127.0.0.1:8010
```

Para detener el servidor:

```text
Ctrl + C
```

## Uso recomendado

Para que no tarde ni gaste mucho:

1. Selecciona un solo modelo.
2. Selecciona un solo prompt.
3. Selecciona una sola actividad.
4. Ejecuta el analisis.

Si seleccionas todo, se ejecutan muchas combinaciones:

```text
3 modelos x 5 prompts x 4 actividades = 60 consultas
```

Eso puede tardar y consumir credito de API.

## Modo demo

En el front puedes activar:

```text
Simular sin API
```

Tambien, si falta una API key o falla una consulta, la aplicacion usa fallback demo automaticamente y marca la fila como `fallback`.

## Modelos configurados

Los modelos estan en `config.json`:

```text
mistral:mistral-small-latest
gemini:gemini-2.5-flash-lite
claude:claude-haiku-4-5
```

Si una cuenta no tiene acceso a algun modelo, cambia el campo `model` en `config.json` por un modelo disponible para esa cuenta.

Nota sobre Mistral/Le Chat: el proyecto usa `mistral-small-latest`, que es una opcion sencilla de API y suficiente para texto amplio. La llave se obtiene en la consola de Mistral.

Nota sobre Gemini: el proyecto usa `gemini-2.5-flash-lite`, `max_output_tokens` alto, reintentos breves ante saturacion `503` y continuacion automatica si Gemini corta la respuesta por limite de tokens. Si aun aparece `503`, es saturacion temporal del servicio; prueba mas tarde o usa Claude.

Para la entrega, si Claude es el unico proveedor estable en tu equipo, selecciona solo `Claude Haiku 4.5` en el dashboard. Si consigues llave de Mistral, tambien puedes probar `Mistral Small Latest`.

## Articulos

La tarea pide al menos 4 articulos. En `config.json` quedaron configurados los 3 articulos disponibles:

1. `A multiplex analysis of phonological and orthographic networks`
2. `Simplicial complex entropy for time series analysis`
3. `Evaluating the Irregularity of Natural Languages`

El dashboard muestra una advertencia mientras falte el cuarto articulo, pero puede correr con 3.

## Reporte estatico

Si no quiere ejecutar nada, abre:

```text
Tareas Obligatorias/LLM2/reporte_llm2_demo.html
```

Ese reporte es demo. Sirve para mostrar tablas e interfaz, pero no ejecuta APIs reales.

Para regenerarlo:

```bash
source .venv-linux/bin/activate
python export_static_report.py
```

## Estructura

```text
LLM2/
  .env.example
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
    provider_client.py
    pdf_processor.py
```
