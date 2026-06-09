"""
    Laberinto  

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    11/Marzo/2026 

"""

# -------------------------- Resolver el laberinto ------------------------------------
def resolver (maze, r, c, tr, tc, pos_r, pos_c, camino):
    if(pos_r < 0 or pos_r >= r) or (pos_c < 0 or pos_c >= c):   # Salio del laberinto
        return False,""
    if maze[pos_r][pos_c] == "1":       # Camino por el que paso
        return False,""
    if maze[pos_r][pos_c] == "#":     # Choca con la pared
        return False,""
    if pos_r == tr and pos_c == tc:   # Llega al final
        return True, camino
    
    maze[pos_r][pos_c] = "1"  # Marcar el lugar actual
    
    # Dar un paso en una de 4 direcciones
    
    #camino += "U"   # Arriba
    paso, cam = resolver(maze,r,c,tr,tc,pos_r-1,pos_c,camino+"U")
    if paso:
        return True, cam
    #camino = camino[:-1]    
    
    #camino += "R"   # Derecha
    paso, cam = resolver(maze,r,c,tr,tc,pos_r,pos_c+1,camino+"R")
    if paso:
        return True, cam
    #camino = camino[:-1]
    
    #camino += "D"   # Abajo
    paso, cam = resolver(maze,r,c,tr,tc,pos_r+1,pos_c,camino+"D")
    if paso:
        return True, cam
    #camino = camino[:-1]
    
    #camino += "L"   # Izquierda
    paso, cam = resolver(maze,r,c,tr,tc,pos_r,pos_c-1,camino+"L")
    if paso:
        return True, cam
    #camino = camino[:-1] 

    return False, ""


# ------------------------------- Main ---------------------------------------
"""
laberinto = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
d_lab= "10 10 1 1 8 8 1"
datos_lab = d_lab.split()
"""

camino = ""
laberinto = []
datos_lab = input().split()
l_r = int(datos_lab[0])
l_c = int(datos_lab[1])
s_r = int(datos_lab[2])
s_c = int(datos_lab[3])
t_r = int(datos_lab[4])
t_c = int(datos_lab[5])
out_opc = int(datos_lab[6])

for i in range(l_r):
    fila = list(input())
    laberinto.append(fila)


""""
for j in range(l_r):
    print(laberinto[j], end="")
    print()
"""

existe, camino = resolver(laberinto,l_r,l_c,t_r,t_c,s_r,s_c,camino)

if out_opc == 1:
    print(existe)
elif out_opc == 2:
    print(len(camino))
elif out_opc == 3:
    print(camino)
