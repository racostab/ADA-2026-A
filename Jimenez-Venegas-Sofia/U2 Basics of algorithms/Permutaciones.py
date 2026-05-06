N, R = map(int, input().split())
elementos = input().split()

elementos.sort()  

usados = [False] * N
perm = []

def generar():
    if len(perm) == R:
        print(" ".join(perm))
        return

    for i in range(N):
        if not usados[i]:
            usados[i] = True
            perm.append(elementos[i])

            generar()

            perm.pop()
            usados[i] = False

generar()