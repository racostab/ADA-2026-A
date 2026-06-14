user_input = input()
n_original = int(user_input)

matriz_A_original = []
for _ in range(n_original):
    user_input = input()
    fila = list(map(int, user_input.split()))
    matriz_A_original.append(fila)

matriz_B_original = []
for _ in range(n_original):
    user_input = input()
    fila = list(map(int, user_input.split()))
    matriz_B_original.append(fila)


def rellenar_matriz(matriz, n_actual, n_nuevo):
    matriz_rellena = [[0] * n_nuevo for _ in range(n_nuevo)]
    for i in range(n_actual):
        for j in range(n_actual):
            matriz_rellena[i][j] = matriz[i][j]
    return matriz_rellena


def sumar_matrices(matriz_X, matriz_Y):
    size = len(matriz_X)
    resultado = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            resultado[i][j] = matriz_X[i][j] + matriz_Y[i][j]
    return resultado


def restar_matrices(matriz_X, matriz_Y):
    size = len(matriz_X)
    resultado = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            resultado[i][j] = matriz_X[i][j] - matriz_Y[i][j]
    return resultado


def strassen(matriz_X, matriz_Y):
    size = len(matriz_X)
    
    if size == 1:
        return [[matriz_X[0][0] * matriz_Y[0][0]]]

    mitad = size // 2

    a11 = [[matriz_X[i][j] for j in range(mitad)] for i in range(mitad)]
    a12 = [[matriz_X[i][j] for j in range(mitad, size)] for i in range(mitad)]
    a21 = [[matriz_X[i][j] for j in range(mitad)] for i in range(mitad, size)]
    a22 = [[matriz_X[i][j] for j in range(mitad, size)] for i in range(mitad, size)]

    b11 = [[matriz_Y[i][j] for j in range(mitad)] for i in range(mitad)]
    b12 = [[matriz_Y[i][j] for j in range(mitad, size)] for i in range(mitad)]
    b21 = [[matriz_Y[i][j] for j in range(mitad)] for i in range(mitad, size)]
    b22 = [[matriz_Y[i][j] for j in range(mitad, size)] for i in range(mitad, size)]

    p1 = strassen(a11, restar_matrices(b12, b22))
    p2 = strassen(sumar_matrices(a11, a12), b22)
    p3 = strassen(sumar_matrices(a21, a22), b11)
    p4 = strassen(a22, restar_matrices(b21, b11))
    p5 = strassen(sumar_matrices(a11, a22), sumar_matrices(b11, b22))
    p6 = strassen(restar_matrices(a12, a22), sumar_matrices(b21, b22))
    p7 = strassen(restar_matrices(a11, a21), sumar_matrices(b11, b12))

    c11 = sumar_matrices(restar_matrices(sumar_matrices(p5, p4), p2), p6)
    c12 = sumar_matrices(p1, p2)
    c21 = sumar_matrices(p3, p4)
    c22 = restar_matrices(restar_matrices(sumar_matrices(p5, p1), p3), p7)

    matriz_C = [[0] * size for _ in range(size)]
    for i in range(mitad):
        for j in range(mitad):
            matriz_C[i][j] = c11[i][j]
            matriz_C[i][j + mitad] = c12[i][j]
            matriz_C[i + mitad][j] = c21[i][j]
            matriz_C[i + mitad][j + mitad] = c22[i][j]

    return matriz_C


n_potencia = 1
while n_potencia < n_original:
    n_potencia *= 2

matriz_A = rellenar_matriz(matriz_A_original, n_original, n_potencia)
matriz_B = rellenar_matriz(matriz_B_original, n_original, n_potencia)

matriz_C_grande = strassen(matriz_A, matriz_B)

for i in range(n_original):
    fila_recortada = matriz_C_grande[i][:n_original]
    print(*fila_recortada)