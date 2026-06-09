import sys

def encontrar(padre, i):
    if padre[i] == i:
        return i
    padre[i] = encontrar(padre, padre[i])
    return padre[i]

def unir(padre, rango, i, j):
    raiz_i = encontrar(padre, i)
    raiz_j = encontrar(padre, j)
    
    if rango[raiz_i] < rango[raiz_j]:
        padre[raiz_i] = raiz_j
    elif rango[raiz_i] > rango[raiz_j]:
        padre[raiz_j] = raiz_i
    else:
        padre[raiz_j] = raiz_i
        rango[raiz_i] += 1

def resolver():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    vertices = int(entrada[0])
    total_aristas = int(entrada[1])
    tipo = entrada[2]
    
    aristas = []
    indice = 3
    
    for _ in range(total_aristas):
        origen = int(entrada[indice])
        destino = int(entrada[indice+1])
        peso = int(entrada[indice+2])
        aristas.append([origen, destino, peso])
        indice += 3
        
    if tipo == "min":
        aristas = sorted(aristas, key=lambda x: x[2])
    else:
        aristas = sorted(aristas, key=lambda x: x[2], reverse=True)
        
    padre = []
    rango = []
    
    for nodo in range(vertices + 1):
        padre.append(nodo)
        rango.append(0)
        
    peso_total = 0
    aristas_usadas = 0
    
    for arista in aristas:
        origen, destino, peso = arista
        
        raiz_origen = encontrar(padre, origen)
        raiz_destino = encontrar(padre, destino)
        
        if raiz_origen != raiz_destino:
            unir(padre, rango, raiz_origen, raiz_destino)
            peso_total += peso
            aristas_usadas += 1
            
            if aristas_usadas == vertices - 1:
                break
                
    print(peso_total)

if __name__ == '__main__':
    resolver()
