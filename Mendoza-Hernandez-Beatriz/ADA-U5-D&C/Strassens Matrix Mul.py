import sys

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def conventional(A, B):
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

    # Caso base
    if n <= 64:
        return conventional(A, B)

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    C = [[0] * n for _ in range(n)]

    for i in range(mid):
        C[i][:mid] = C11[i]
        C[i][mid:] = C12[i]

    for i in range(mid):
        C[i + mid][:mid] = C21[i]
        C[i + mid][mid:] = C22[i]

    return C

def next_power_of_two(n):
    p = 1
    while p < n:
        p <<= 1
    return p

def main():
    data = sys.stdin.read().strip().splitlines()

    n = int(data[0])

    A = [list(map(int, data[i + 1].split())) for i in range(n)]
    B = [list(map(int, data[i + 1 + n].split())) for i in range(n)]

    m = next_power_of_two(n)

    if m != n:
        A_pad = [[0] * m for _ in range(m)]
        B_pad = [[0] * m for _ in range(m)]

        for i in range(n):
            for j in range(n):
                A_pad[i][j] = A[i][j]
                B_pad[i][j] = B[i][j]

        A = A_pad
        B = B_pad

    C = strassen(A, B)

    for i in range(n):
        print(*C[i][:n])

if __name__ == "__main__":
    main()