import sys
input = sys.stdin.readline

def add_matriz(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matriz(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)    
    
    if n == 1:
        C = [[0]]
        C[0][0] = A[0][0] * B[0][0]
        return C

    mid = n // 2    

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    M1 = strassen(add_matriz(A11, A22), add_matriz(B11, B22))
    M2 = strassen(add_matriz(A21, A22), B11)
    M3 = strassen(A11, sub_matriz(B12, B22))
    M4 = strassen(A22, sub_matriz(B21, B11))
    M5 = strassen(add_matriz(A11, A12), B22)
    M6 = strassen(sub_matriz(A21, A11), add_matriz(B11, B12))
    M7 = strassen(sub_matriz(A12, A22), add_matriz(B21, B22))
    
    C = [[0]*n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j]         = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j]
            C[i][j+mid]     = M3[i][j] + M5[i][j]
            C[i+mid][j]     = M2[i][j] + M4[i][j]
            C[i+mid][j+mid] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j]
    
    return C

def get_size_2(n):
    p = 1
    while p < n:
        p <<= 1
    return p

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

size = get_size_2(n)

if size != n:
    for i in range(n):
        A[i] += [0] * (size - n)
        B[i] += [0] * (size - n)
    zero_row = [0] * size
    for _ in range(size - n):
        A.append(zero_row[:])
        B.append(zero_row[:])

C = strassen(A, B)

out = []
for i in range(n):
    out.append(' '.join(map(str, C[i][:n])))
print('\n'.join(out))

