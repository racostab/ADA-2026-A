def read_matrix(n):
    mat = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        print(' '.join(map(str, row)))

def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(mat):
    n = len(mat)
    mid = n // 2
    A11 = [row[:mid] for row in mat[:mid]]
    A12 = [row[mid:] for row in mat[:mid]]
    A21 = [row[:mid] for row in mat[mid:]]
    A22 = [row[mid:] for row in mat[mid:]]
    return A11, A12, A21, A22

def merge_matrix(C11, C12, C21, C22):
    n = len(C11) + len(C21)
    mat = [[0] * n for _ in range(n)]
    mid = len(C11)
    for i in range(mid):
        for j in range(mid):
            mat[i][j] = C11[i][j]
            mat[i][j + mid] = C12[i][j]
    for i in range(mid):
        for j in range(mid):
            mat[i + mid][j] = C21[i][j]
            mat[i + mid][j + mid] = C22[i][j]
    return mat

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, subtract_matrix(B12, B22))
    M4 = strassen(A22, subtract_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(subtract_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(subtract_matrix(add_matrix(M1, M3), M2), M6)

    return merge_matrix(C11, C12, C21, C22)

def next_power_of_two(n):
    p = 1
    while p < n:
        p <<= 1
    return p

def pad_matrix(mat, new_size):
    """Agranda la matriz con ceros hasta new_size x new_size"""
    n = len(mat)
    padded = [[0] * new_size for _ in range(new_size)]
    for i in range(n):
        for j in range(n):
            padded[i][j] = mat[i][j]
    return padded

def unpad_matrix(mat, original_size):
    """Elimina el padding para devolver la matriz al tamaño original"""
    return [row[:original_size] for row in mat[:original_size]]

N = int(input())
A = read_matrix(N)
B = read_matrix(N)

m = next_power_of_two(N)
A_padded = pad_matrix(A, m)
B_padded = pad_matrix(B, m)
C_padded = strassen(A_padded, B_padded)
C = unpad_matrix(C_padded, N)
print_matrix(C)