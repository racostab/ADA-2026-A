n,m,C1_I,C2_I,C1_F,C2_F,O = map(int,input().split())

#print("n = ", n,"- m = ", m,"-", C1_I,C2_I,"-",C1_F,C2_F,"-",variante)

matriz = []

for i in range(n):
    fila = list(input())
    matriz.append(fila)


#Función recursiva 
def maze (matriz, fila, columna, C1_F,C2_F,O,camino):
    if (fila < 0 or fila >= n) or (columna < 0 or columna >= m):
        return False
    if (matriz[fila][columna] == "#" ):
        return False
    if matriz[fila][columna] == "+" :
        return False
    if fila == C1_F and columna == C2_F:
        return True 
    
    matriz[fila][columna] = "+"
    camino.append("U")
    if maze(matriz, fila-1,columna, C1_F,C2_F,O,camino):   #Arriba 
        return True
    camino.pop()

    camino.append("R")
    if maze(matriz, fila,columna+1, C1_F,C2_F,O,camino):   #Derecha
        return True
    camino.pop()

    camino.append("D")
    if maze(matriz, fila+1,columna, C1_F,C2_F,O,camino):   #Abajo
        return True
    camino.pop()
      
    camino.append("L")
    if maze(matriz, fila,columna-1, C1_F,C2_F,O,camino):   #Izquierda
        return True
    camino.pop()
    
camino = []
if maze(matriz, C1_I, C2_I, C1_F, C2_F, O, camino):
    if O == 1:
        print(True)
    elif O == 2:
        suma = sum(fila.count("+") for fila in matriz)
        print(suma)
    elif O == 3:
        print("".join(camino))
else:
    if O == 1:
        print(False)
    elif O == 2:
        print(0)
    elif O == 3:
        print("No path")