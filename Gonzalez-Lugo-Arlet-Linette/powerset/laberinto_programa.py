valores = list(map(int, input().split()))
filas, columnas, fila_inicio, columna_inicio, fila_destino, columna_destino, tipo_salida = valores
laberinto = []
for _ in range(filas):
    linea = input()
    if len(linea) < columnas:
        linea = linea + ' ' * (columnas - len(linea))
    laberinto.append(list(linea))

if laberinto[fila_inicio][columna_inicio] == '#' or laberinto[fila_destino][columna_destino] == '#':
    if tipo_salida == 1:
        print("False")
    elif tipo_salida == 2:
        print(-1)
    elif tipo_salida == 3:
        print("NO PATH")
    exit()

cola = [(fila_inicio, columna_inicio)]
distancia = [[-1] * columnas for _ in range(filas)]
padre = [[None] * columnas for _ in range(filas)]
distancia[fila_inicio][columna_inicio] = 0

for fila_actual, columna_actual in cola:
    if fila_actual == fila_destino and columna_actual == columna_destino:
        break
    
    for df, dc, letra in [(-1,0,'U'), (0,1,'R'), (1,0,'D'), (0,-1,'L')]:
        fila_nueva = fila_actual + df
        columna_nueva = columna_actual + dc
        
        if 0 <= fila_nueva < filas and 0 <= columna_nueva < columnas:
            if laberinto[fila_nueva][columna_nueva] != '#' and distancia[fila_nueva][columna_nueva] == -1:
                distancia[fila_nueva][columna_nueva] = distancia[fila_actual][columna_actual] + 1
                padre[fila_nueva][columna_nueva] = (fila_actual, columna_actual, letra)
                cola.append((fila_nueva, columna_nueva))

if tipo_salida == 1:
    print("True" if distancia[fila_destino][columna_destino] != -1 else "False")
elif tipo_salida == 2:
    print(distancia[fila_destino][columna_destino] if distancia[fila_destino][columna_destino] != -1 else -1)
elif tipo_salida == 3:
    if distancia[fila_destino][columna_destino] == -1:
        print("NO PATH")
    else:
        camino = []
        fila_actual, columna_actual = fila_destino, columna_destino
        while (fila_actual, columna_actual) != (fila_inicio, columna_inicio):
            fila_padre, columna_padre, letra = padre[fila_actual][columna_actual]
            camino.append(letra)
            fila_actual, columna_actual = fila_padre, columna_padre
        camino.reverse()
        print(''.join(camino))