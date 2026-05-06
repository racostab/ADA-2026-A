#!/bin/bash

#
# Usa el requirements.txt para crear un entorno virtual.
# Para recrearlo: 
#     $ pip freeze > requirements.txt

# ── Configuración ──────────────────────────────────────────
VENV_NAME="${1:-.venv}"          # Nombre por defecto: .venv
PYTHON="${2:-python3}"           # Intérprete por defecto: python3

# ── Colores ────────────────────────────────────────────────
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# ── Verificar que Python existe ────────────────────────────
if ! command -v "$PYTHON" &>/dev/null; then
  echo -e "${RED}[ERROR]${NC} No se encontró '$PYTHON'. Instálalo primero."
  exit 1
fi

# ── Crear el entorno ───────────────────────────────────────
echo -e "${YELLOW}[INFO]${NC} Creando entorno virtual '$VENV_NAME' con $($PYTHON --version)..."
$PYTHON -m venv "$VENV_NAME"

if [ $? -ne 0 ]; then
  echo -e "${RED}[ERROR]${NC} Falló la creación del entorno."
  exit 1
fi

echo -e "${GREEN}[OK]${NC} Entorno creado en './$VENV_NAME'"

# ── Activar y actualizar pip ───────────────────────────────
source "$VENV_NAME/bin/activate"
echo -e "${YELLOW}[INFO]${NC} Actualizando pip..."
pip install --upgrade pip -q

# ── Instalar requirements.txt si existe ───────────────────
if [ -f "requirements.txt" ]; then
  echo -e "${YELLOW}[INFO]${NC} Instalando dependencias desde requirements.txt..."
  pip install -r requirements.txt
  echo -e "${GREEN}[OK]${NC} Dependencias instaladas."
else
  echo -e "${YELLOW}[INFO]${NC} No se encontró requirements.txt, omitiendo."
fi

# ── Instrucciones finales ──────────────────────────────────
echo ""
echo -e "${GREEN}✔ Entorno listo.${NC} Para activarlo manualmente:"
echo -e "   source ${VENV_NAME}/bin/activate"
echo -e "Para desactivarlo: ${YELLOW}deactivate${NC}"
