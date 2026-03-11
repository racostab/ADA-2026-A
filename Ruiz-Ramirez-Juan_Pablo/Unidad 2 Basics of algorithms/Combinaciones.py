#Generación de combinaciones dada una lista
#Dado 2 valores (n - r) siendo n el número elementos y r el número sub-elementos 

n,r = map(int,input().split())
elementos = input().split()
resultado = []
def combinaciones (n,r,elementos,inicio, actual):
    if len(actual) == r:
        resultado.append((actual[:]))
        return
    for i in range (inicio, n):
        actual.append(elementos[i])
        combinaciones(n,r,elementos, i+1, actual)
        actual.pop()

combinaciones(n,r,elementos,0,[])
for c in resultado:
    print(" ".join(c))
