"""
    Problema 11 Project Euler
    Counting Summations
    Solo numero de formas

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    21/Marzo/2026 

"""

def numero_particiones(n):
    
    for ki in range(1, n + 1):
        for kj in range(ki, n + 1):
            c[kj] += c[kj - ki]

    return

x = 100
c = [0] * (x + 1)
c[0] = 1

numero_particiones(x)
print(c[x]-1)
