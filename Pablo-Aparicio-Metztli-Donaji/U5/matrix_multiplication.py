# Given two square matrices A and B of size N x N each, find their multiplication matrix (C = AB) using the Strassen’s algorithm.

# Input
# The input file contains one test case described below. The first line contains the integer N (1 ≤ N ≤ 1000). This is followed 
# by 2N lines with integer numbers that represente the rows of the matrices A and B. The first N lines contains the N rows of 
# matrix A and the next N lines the rows of matrix B. Each row has N columns separated by a space. Each cell of a matrix takes 
# values ai and bi (0 ≤ ai, bi ≤ 1000000).
# Output
# The output file contains the multiplication matrix C. There are N rows, each one with N columns separated by a space. Each cell 
# of the matrix takes values ci (0 ≤ ci ≤ 10000002).
# Sample Input
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output
# 30 36 42
# 66 81 96
# 102 126 150
import sys
input = sys.stdin.readline

def entry(n):
    mtx_1 = []
    mtx_2 = []
    for _ in range(n):
        mtx_1.append(list(map(int, input().split())))
    for _ in range(n):
        mtx_2.append(list(map(int, input().split())))
    return mtx_1, mtx_2

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

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
    M3 = strassen(A11,           sub(B12, B22))
    M4 = strassen(A22,           sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C

def pad(M, size):
    n = len(M)
    padded = [row + [0] * (size - n) for row in M]
    for _ in range(size - n):
        padded.append([0] * size)
    return padded

def next_power_of_2(n):
    p = 1
    while p < n:
        p <<= 1
    return p

def main():
    n = int(input())
    A, B = entry(n)

    size = next_power_of_2(n)
    A = pad(A, size)
    B = pad(B, size)

    C = strassen(A, B)

    for i in range(n):
        print(*C[i][:n])

if __name__ == "__main__":
    main()