n = int(input(""))
elementos = input("").split()
conjunto = []

def subconjuntos(inicio, tamaño, actual):
    if len(actual) == tamaño:
        print(" ".join(actual))
        return
    for i in range(inicio,n):
        actual.append(elementos[i])
        subconjuntos(i+1, tamaño, actual)
        actual.pop()

for tamaño in range(1,n+1):
    subconjuntos(0, tamaño, [])


