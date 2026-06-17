import sys

def suma(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def resta(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def classical_mult(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            for j in range(n):
                C[i][j] += aik * B[k][j]

    return C

def strassen(A, B):
    n = len(A)

    if n <= 64:
        return classical_mult(A, B)

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(suma(A11, A22), suma(B11, B22))
    M2 = strassen(suma(A21, A22), B11)
    M3 = strassen(A11, resta(B12, B22))
    M4 = strassen(A22, resta(B21, B11))
    M5 = strassen(suma(A11, A12), B22)
    M6 = strassen(resta(A21, A11), suma(B11, B12))
    M7 = strassen(resta(A12, A22), suma(B21, B22))

    C11 = suma(resta(suma(M1, M4), M5), M7)
    C12 = suma(M3, M5)
    C21 = suma(M2, M4)
    C22 = suma(resta(suma(M1, M3), M2), M6)

    C = [[0] * n for _ in range(n)]

    for i in range(mid):
        C[i][:mid] = C11[i]
        C[i][mid:] = C12[i]

    for i in range(mid):
        C[i + mid][:mid] = C21[i]
        C[i + mid][mid:] = C22[i]

    return C

def siguiente_potencia_dos(n):
    p = 1
    while p < n:
        p <<= 1
    return p

def main():
    data = sys.stdin.buffer.read().split()

    idx = 0
    n = int(data[idx])
    idx += 1

    A = [[0] * n for _ in range(n)]
    B = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            A[i][j] = int(data[idx])
            idx += 1

    for i in range(n):
        for j in range(n):
            B[i][j] = int(data[idx])
            idx += 1

    m = siguiente_potencia_dos(n)

    if m != n:
        Ap = [[0] * m for _ in range(m)]
        Bp = [[0] * m for _ in range(m)]

        for i in range(n):
            Ap[i][:n] = A[i]
            Bp[i][:n] = B[i]

        C = strassen(Ap, Bp)

        for i in range(n):
            print(*C[i][:n])
    else:
        C = strassen(A, B)

        for row in C:
            print(*row)

if __name__ == "__main__":
    main()