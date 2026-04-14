# API_Claude

Proyecto local para consumir Claude desde Python, generar soluciones a problemas de programacion competitiva y validarlas con una rubrica local `@3` y `@5`.

## En que consiste

El flujo completo del proyecto es este:

1. Una API local en FastAPI recibe un prompt.
2. Esa API consulta Claude usando la API oficial de Anthropic.
3. La respuesta se guarda en JSON.
4. El codigo Python se extrae de la respuesta.
5. La solucion extraida se prueba con casos oficiales y casos borde.
6. Una rubrica local resume si la solucion llega a `@3` o `@5`.

## Estado actual

- La conexion a Claude ya esta funcionando con `ANTHROPIC_API_KEY` en `.env`.
- La API local ya responde en `/health` y `/api/chat`.
- Ya existen soluciones generadas para `Combinations` y `Maze`.
- Con la rubrica local actual:
  - `Combinations` pasa `@5`.
  - `Maze` pasa `@5`.

## Estructura actual

```text
API_Claude/
|-- .env
|-- .gitignore
|-- .venv/
|-- README.md
|-- requirements.txt
|-- SRC/
|   |-- __init__.py
|   |-- api.py
|   |-- evaluar_rubrica.py
|   |-- extraer_codigo.py
|   |-- pedir_y_guardar.py
|   |-- probar_CLAUDE.py
|   |-- probar_solucion.py
|   |-- validar_maze.py
|   `-- soluciones/
|       |-- combinations.py
|       `-- maze.py
`-- DAT/
    |-- COMBINATIONS.pdf
    |-- MAZE.pdf
    |-- body.JSON
    |-- body_gnome_sort.json
    |-- body_maze.json
    |-- example.md
    |-- response_CLAUDE GNOME SORT.json
    |-- response_CLAUDE2 PRUEBA.json
    |-- prompts/
    |-- respuestas/
    `-- tests/
```

## Requisitos

- Python 3.10 o superior
- Git Bash o PowerShell
- Una clave valida de Anthropic

## Configuracion inicial

1. Abre una terminal en la carpeta del proyecto.
2. Activa el entorno virtual.
3. Verifica que `.env` tenga `ANTHROPIC_API_KEY`.

### Git Bash

```bash
source .venv/Scripts/activate
```

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

## Como ejecutar la API

Desde la raiz del proyecto:

```bash
python -m uvicorn SRC.api:app --reload
```

La API queda disponible en:

```text
http://127.0.0.1:8000
```

## Verificacion rapida

### Health check

```bash
curl http://127.0.0.1:8000/health
```

### Prueba directa contra Claude sin pasar por FastAPI

```bash
python SRC/probar_CLAUDE.py "Dame una implementacion de Gnome Sort en Python con ejemplo."
```

## Flujo completo para generar una solucion nueva

### 1. Pedir la solucion y guardarla como JSON

#### Combinations

```bash
python SRC/pedir_y_guardar.py DAT/prompts/combinations_solver.json DAT/respuestas/combinations.json
```

#### Maze

```bash
python SRC/pedir_y_guardar.py DAT/prompts/maze_solver.json DAT/respuestas/maze.json
```

### 2. Extraer el codigo Python desde la respuesta

#### Combinations

```bash
python SRC/extraer_codigo.py DAT/respuestas/combinations.json SRC/soluciones/combinations.py
```

#### Maze

```bash
python SRC/extraer_codigo.py DAT/respuestas/maze.json SRC/soluciones/maze.py
```

## Como probar las soluciones

### Pruebas puntuales de Combinations

```bash
python SRC/probar_solucion.py SRC/soluciones/combinations.py DAT/tests/combinations_case1.in DAT/tests/combinations_case1.out
python SRC/probar_solucion.py SRC/soluciones/combinations.py DAT/tests/combinations_case2.in DAT/tests/combinations_case2.out
```

### Pruebas puntuales de Maze

```bash
python SRC/validar_maze.py SRC/soluciones/maze.py DAT/tests/maze_sample_o1.in
python SRC/validar_maze.py SRC/soluciones/maze.py DAT/tests/maze_sample_o2.in
python SRC/validar_maze.py SRC/soluciones/maze.py DAT/tests/maze_sample_o3.in
```

Si quieres aceptar cualquier camino valido en `O=3`, aunque no sea el mas corto:

```bash
python SRC/validar_maze.py SRC/soluciones/maze.py DAT/tests/maze_sample_o3.in --allow-any-path
```

## Rubrica local @3 y @5

La rubrica implementada en `SRC/evaluar_rubrica.py` usa esta suposicion:

- `@3`: pasa los casos oficiales del enunciado.
- `@5`: pasa los casos oficiales y casos borde adicionales.

Para ejecutarla:

```bash
python SRC/evaluar_rubrica.py
```

## Resultado actual de la rubrica

- `Combinations`: `@5`
- `Maze`: `@5`

## Nota importante sobre Maze

La validacion local de `Maze` asume lo siguiente:

- Para `O = 2`, la respuesta correcta es la longitud del camino mas corto.
- Para `O = 3`, la respuesta correcta es un camino minimo.
- El desempate de exploracion se considera con el orden `U, R, D, L`.

Eso nos permite probar la solucion de manera consistente. Si tu profesor usa una rubrica o interpretacion distinta, la podemos ajustar.

## Seguridad

La clave de Anthropic debe quedarse en `.env` y no debe subirse al repositorio.
