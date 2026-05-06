def generar_combinaciones(arr, r, inicio, combinacion):
    if len(combinacion) == r:
        print(" ".join(combinacion))
        return

    for i in range(inicio, len(arr)):
        combinacion.append(arr[i])
        generar_combinaciones(arr, r, i + 1, combinacion)
        combinacion.pop()

N, R = map(int, input().split())
arr = input().split()

generar_combinaciones(arr, R, 0, [])