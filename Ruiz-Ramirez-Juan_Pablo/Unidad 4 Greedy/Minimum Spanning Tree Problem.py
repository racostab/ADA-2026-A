# ─────────────────────────────────────────────────────────────────
#  Minimum Spanning Tree — Kruskal
#  Paradigma: GREEDY (selección de aristas)
#  Sin librerías externas
# ─────────────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════
#  UNION-FIND (Conjuntos Disjuntos)
#  Detecta si dos vértices ya están conectados → evita ciclos
# ══════════════════════════════════════════════════════════════════

# Cada vértice empieza siendo su propio representante (padre de sí mismo)
def crear_uf(n):
    padre = []
    rango = []
    for i in range(n + 1):     # índices del 0 al n (usamos 1..n)
        padre.append(i)        # padre[i] = i  →  cada quien es raíz
        rango.append(0)        # todos los árboles internos tienen altura 0
    return padre, rango

# Encuentra la raíz del conjunto de x
# "Path compression": en la recursión aplana el árbol apuntando directo a la raíz
def encontrar(padre, x):
    if padre[x] != x:
        padre[x] = encontrar(padre, padre[x])   # compresión de camino
    return padre[x]

# Une los conjuntos de x e y
# Devuelve True si eran distintos (arista válida), False si ya estaban juntos (ciclo)
def unir(padre, rango, x, y):
    raiz_x = encontrar(padre, x)
    raiz_y = encontrar(padre, y)

    if raiz_x == raiz_y:        # mismo conjunto → formaría ciclo
        return False

    # "Union by rank": el árbol de menor altura cuelga del de mayor altura
    # Esto evita que el árbol interno crezca demasiado
    if rango[raiz_x] < rango[raiz_y]:
        padre[raiz_x] = raiz_y          # raiz_x pasa a depender de raiz_y

    elif rango[raiz_x] > rango[raiz_y]:
        padre[raiz_y] = raiz_x          # raiz_y pasa a depender de raiz_x

    else:
        padre[raiz_y] = raiz_x          # mismo rango: uno absorbe al otro
        rango[raiz_x] = rango[raiz_x] + 1   # la raíz elegida crece en altura

    return True                 # unión exitosa, arista aceptada en el árbol


# ══════════════════════════════════════════════════════════════════
#  ORDENAMIENTO — Insertion Sort
#  Ordena la lista de aristas por peso sin usar sorted() ni .sort()
#  Complexity: O(E²) — suficiente para E ≤ 100
# ══════════════════════════════════════════════════════════════════

def insertion_sort(aristas, modo):
    # Recorre desde el segundo elemento hasta el último
    for i in range(1, len(aristas)):
        clave = aristas[i]              # elemento a insertar en su posición
        j = i - 1

        # Desplaza elementos mayores (min) o menores (max) hacia la derecha
        if modo == 'min':
            # Para MST mínimo: queremos orden ascendente por peso
            while j >= 0 and aristas[j][0] > clave[0]:
                aristas[j + 1] = aristas[j]
                j = j - 1
        else:
            # Para MST máximo: queremos orden descendente por peso
            while j >= 0 and aristas[j][0] < clave[0]:
                aristas[j + 1] = aristas[j]
                j = j - 1

        aristas[j + 1] = clave          # coloca el elemento en su hueco
    return aristas


# ══════════════════════════════════════════════════════════════════
#  ALGORITMO DE KRUSKAL
#  Paradigma GREEDY:
#    → En cada paso elige la arista de menor (o mayor) peso
#      que no forme un ciclo con las ya elegidas.
#    → La elección local óptima garantiza el óptimo global
#      gracias a la "Cut Property" de los spanning trees.
# ══════════════════════════════════════════════════════════════════

def kruskal(V, aristas, modo):
    # PASO 1: ordenar aristas por peso (decisión central del greedy)
    aristas = insertion_sort(aristas, modo)

    # PASO 2: inicializar Union-Find con V vértices aislados
    padre, rango = crear_uf(V)

    peso_total   = 0            # acumula el peso del spanning tree
    aristas_usadas = 0          # un spanning tree tiene exactamente V-1 aristas

    # PASO 3: recorrer aristas en orden greedy
    for peso, u, v in aristas:

        # Intento de unión: si son componentes distintas → arista válida
        if unir(padre, rango, u, v):
            peso_total     = peso_total + peso
            aristas_usadas = aristas_usadas + 1

            # Condición de parada: árbol completo con V-1 aristas
            if aristas_usadas == V - 1:
                break
            # Si no rompemos aquí, seguimos buscando la siguiente
            # arista más barata (o cara) disponible

        # Si unir() devolvió False: la arista formaría ciclo → la ignoramos
        # (el greedy la descarta para siempre y pasa a la siguiente)

    return peso_total


# ══════════════════════════════════════════════════════════════════
#  LECTURA DE ENTRADA  (formato exacto del PDF)
#  Primera línea : V E modo
#  Siguientes E  : vi vj w
# ══════════════════════════════════════════════════════════════════

def leer_entrada():
    primera_linea = input().split()
    V    = int(primera_linea[0])   # número de vértices
    E    = int(primera_linea[1])   # número de aristas
    modo = primera_linea[2]        # 'min' o 'max'

    aristas = []
    for _ in range(E):
        partes = input().split()
        u = int(partes[0])         # vértice origen
        v = int(partes[1])         # vértice destino
        w = int(partes[2])         # peso de la arista
        aristas.append((w, u, v))  # guardamos (peso, u, v) para ordenar por peso

    return V, E, modo, aristas


# ══════════════════════════════════════════════════════════════════
#  PROGRAMA PRINCIPAL
# ══════════════════════════════════════════════════════════════════

V, E, modo, aristas = leer_entrada()

resultado = kruskal(V, aristas, modo)

print(resultado)    # salida: un único entero (peso del MST) 