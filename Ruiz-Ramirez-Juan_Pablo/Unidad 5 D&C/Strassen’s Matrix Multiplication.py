def sumar_matrices(X, Y):
    filas = len(X)
    columnas = len(X[0])
    result = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            result[i][j] = X[i][j] + Y[i][j]
    return result

def restar_matrices(X, Y):
    filas = len(X)
    columnas = len(X[0])
    result = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            result[i][j] = X[i][j] - Y[i][j]
    return result

def dividir_matriz(A):
    n = len(A)
    mid = n // 2
    A11 = [fila[:mid] for fila in A[:mid]]
    A12 = [fila[mid:] for fila in A[:mid]]
    A21 = [fila[:mid] for fila in A[mid:]]
    A22 = [fila[mid:] for fila in A[mid:]]
    return A11, A12, A21, A22

def combinar_matrices(A11, A12, A21, A22):
    resultado = []
    for i in range(len(A11)):
        resultado.append(A11[i] + A12[i])
    for i in range(len(A21)):
        resultado.append(A21[i] + A22[i])
    return resultado

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    A11, A12, A21, A22 = dividir_matriz(A)
    B11, B12, B21, B22 = dividir_matriz(B)
    P1 = strassen(A11, restar_matrices(B12, B22))
    P2 = strassen(sumar_matrices(A11, A12), B22)
    P3 = strassen(sumar_matrices(A21, A22), B11)
    P4 = strassen(A22, restar_matrices(B21, B11))
    P5 = strassen(sumar_matrices(A11, A22), sumar_matrices(B11, B22))
    P6 = strassen(restar_matrices(A12, A22), sumar_matrices(B21, B22))
    P7 = strassen(restar_matrices(A11, A21), sumar_matrices(B11, B12))
    C11 = sumar_matrices(restar_matrices(sumar_matrices(P5, P4), P2), P6)
    C12 = sumar_matrices(P1, P2)
    C21 = sumar_matrices(P3, P4)
    C22 = restar_matrices(restar_matrices(sumar_matrices(P1, P5), P3), P7)
    return combinar_matrices(C11, C12, C21, C22)

def siguiente_potencia_2(n):
    potencia = 1
    while potencia < n:
        potencia *= 2
    return potencia

def pad_matriz(M, nuevo_tam):
    filas = len(M)
    columnas = len(M[0])
    resultado = [[0 for _ in range(nuevo_tam)] for _ in range(nuevo_tam)]
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = M[i][j]
    return resultado

def recortar_matriz(M, filas, columnas):
    return [fila[:columnas] for fila in M[:filas]]

def multiplicar(A, B, n):
    m = siguiente_potencia_2(n)
    A_pad = pad_matriz(A, m)
    B_pad = pad_matriz(B, m)
    C_pad = strassen(A_pad, B_pad)
    return recortar_matriz(C_pad, n, n)

def leer_matriz(n):
    matriz = []
    for _ in range(n):
        matriz.append(list(map(int, input().split())))
    return matriz

n = int(input())
A = leer_matriz(n)
B = leer_matriz(n)
C = multiplicar(A, B, n)
for fila in C:
    print(' '.join(map(str, fila)))