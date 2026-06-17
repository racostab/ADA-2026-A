# Author: Jalton Efrain Jara Neira
# Date: 12/03/2026

import sys
from collections import deque

def program_main():
    input_all = sys.stdin.read().splitlines()
    if not input_all:
        return

    it = iter(input_all)
    header = input_all[0].split()
    if not header: return
    
    R, C, Sr, Sc, Tr, Tc, O = map(int, header)
    laberinto = input_all[1:1+R]

    #BFS (fila, columna, distancia, camino)
    queue = deque([(Sr, Sc, 0, "")])
    visited = [[False for j in range(C)] for j in range(R)]
    visited[Sr][Sc] = True

    #Movimientos: arriba, derecha, abajo e izquierda
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dir_labels = ['U', 'R', 'D', 'L']

    while queue:
        r, c, dist, path = queue.popleft()

        if r == Tr and c == Tc:
            if O == 1: print("True")
            elif O == 2: print(dist)
            elif O == 3: print(path)
            return

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            #Límites y pasillos
            if 0 <= nr < R and 0 <= nc < C and laberinto[nr][nc] == ' ' and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1, path + dir_labels[i]))

    if O == 1:
        print("False")

if __name__ == "__main__":
    program_main()