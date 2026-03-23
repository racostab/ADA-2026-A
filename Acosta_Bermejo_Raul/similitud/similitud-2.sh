#
#
#
#!/bin/bash
# ssdeep_compare.sh
# Compara similitud fuzzy entre todos los archivos de una carpeta
# Uso: ./ssdeep_compare.sh [carpeta] [umbral]
# Ejemplo: ./ssdeep_compare.sh ./malware 50

# ---------- configuración ----------
CARPETA="${1:-.}"          # carpeta a analizar (default: directorio actual)
UMBRAL="${2:-1}"           # score mínimo de similitud a mostrar (1-100)
HASHES_TMP=$(mktemp)       # archivo temporal para los hashes
# -----------------------------------

# colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # sin color

# verificar que ssdeep está instalado
if ! command -v ssdeep &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} ssdeep no está instalado."
    echo "Instálalo con:"
    echo "  Ubuntu/Debian: sudo apt install ssdeep"
    echo "  macOS:         brew install ssdeep"
    echo "  RHEL/CentOS:   sudo yum install ssdeep"
    exit 1
fi

# verificar que la carpeta existe
if [ ! -d "$CARPETA" ]; then
    echo -e "${RED}[ERROR]${NC} La carpeta '$CARPETA' no existe."
    exit 1
fi

# contar archivos (solo archivos regulares, no directorios)
TOTAL=$(find "$CARPETA" -maxdepth 1 -type f | wc -l | tr -d ' ')

if [ "$TOTAL" -eq 0 ]; then
    echo -e "${YELLOW}[AVISO]${NC} No se encontraron archivos en '$CARPETA'."
    exit 0
fi

echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}   ssdeep — comparación de similitud   ${NC}"
echo -e "${CYAN}========================================${NC}"
echo -e "Carpeta  : ${CARPETA}"
echo -e "Archivos : ${TOTAL}"
echo -e "Umbral   : ${UMBRAL}%"
echo -e "${CYAN}----------------------------------------${NC}\n"

# paso 1: generar hashes de todos los archivos
echo -e "[1/2] Generando hashes fuzzy..."
ssdeep -r "$CARPETA" > "$HASHES_TMP" 2>/dev/null

HASH_COUNT=$(grep -c ',' "$HASHES_TMP" 2>/dev/null || echo 0)
echo -e "      ${HASH_COUNT} hashes generados\n"

# paso 2: comparar todos contra todos
echo -e "[2/2] Comparando similitudes (umbral >= ${UMBRAL}%)...\n"
echo -e "${CYAN}----------------------------------------${NC}"
printf "%-6s %-35s %-35s %s\n" "Score" "Archivo A" "Archivo B" "Similitud"
echo -e "${CYAN}----------------------------------------${NC}"

MATCHES=0

# ssdeep -m compara un archivo de hashes contra sí mismo
# -t umbral mínimo de similitud
ssdeep -m "$HASHES_TMP" -t "$UMBRAL" "$HASHES_TMP" 2>/dev/null | \
while IFS= read -r line; do
    # ssdeep output: "archivo1" matches "archivo2" (score)
    if [[ "$line" =~ \"(.+)\"\ matches\ \"(.+)\"\ \(([0-9]+)\) ]]; then
        FILE_A="${BASH_REMATCH[1]}"
        FILE_B="${BASH_REMATCH[2]}"
        SCORE="${BASH_REMATCH[3]}"

        # evitar comparar un archivo consigo mismo
        if [ "$FILE_A" == "$FILE_B" ]; then
            continue
        fi

        # color según score
        if [ "$SCORE" -ge 90 ]; then
            COLOR=$RED        # muy similar / posible duplicado
        elif [ "$SCORE" -ge 60 ]; then
            COLOR=$YELLOW     # bastante similar
        else
            COLOR=$GREEN      # algo similar
        fi

        # acortar nombres largos para que quepan en pantalla
        A_SHORT=$(basename "$FILE_A")
        B_SHORT=$(basename "$FILE_B")

        printf "${COLOR}%-6s${NC} %-35s %-35s\n" \
            "${SCORE}%" \
            "${A_SHORT:0:34}" \
            "${B_SHORT:0:34}"

        MATCHES=$((MATCHES + 1))
    fi
done

echo -e "${CYAN}----------------------------------------${NC}"

# resumen final
if [ "$MATCHES" -eq 0 ]; then
    echo -e "\n${GREEN}Sin coincidencias${NC} por encima del umbral ${UMBRAL}%."
else
    echo -e "\n${YELLOW}${MATCHES} par(es)${NC} con similitud >= ${UMBRAL}%."
fi

# leyenda de colores
echo -e "\nLeyenda:"
echo -e "  ${RED}■${NC} 90-100% — muy similar / posible duplicado o variante"
echo -e "  ${YELLOW}■${NC} 60-89%  — bastante similar"
echo -e "  ${GREEN}■${NC}  1-59%  — similitud parcial"

# limpiar temporal
rm -f "$HASHES_TMP"

