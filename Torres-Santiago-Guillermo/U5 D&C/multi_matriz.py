def suma(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def resta(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mult_mtz(A, iA, jA, B, iB, jB, n):

    if n == 1:
        C = [[0]]
        C[0][0] = A[iA][jA] * B[iB][jB]
        return C

    mitad = n // 2

    def suma_sub(M, f, c, N, f2, c2):
        res = [[0] * mitad for _ in range(mitad)]
        for i in range(mitad):
            for j in range(mitad):
                res[i][j] = M[f + i][c + j] + N[f2 + i][c2 + j]
        return res

    def resta_sub(M, f, c, N, f2, c2):
        res = [[0] * mitad for _ in range(mitad)]
        for i in range(mitad):
            for j in range(mitad):
                res[i][j] = M[f + i][c + j] - N[f2 + i][c2 + j]
        return res

    sA_M1 = suma_sub(A, iA, jA, A, iA + mitad, jA + mitad)
    sB_M1 = suma_sub(B, iB, jB, B, iB + mitad, jB + mitad)
    M1 = mult_mtz(sA_M1, 0, 0, sB_M1, 0, 0, mitad)

    sA_M2 = suma_sub(A, iA + mitad, jA, A, iA + mitad, jA + mitad)
    M2 = mult_mtz(sA_M2, 0, 0, B, iB, jB, mitad)

    sB_M3 = resta_sub(B, iB, jB + mitad, B, iB + mitad, jB + mitad)
    M3 = mult_mtz(A, iA, jA, sB_M3, 0, 0, mitad)

    sB_M4 = resta_sub(B, iB + mitad, jB, B, iB, jB)
    M4 = mult_mtz(A, iA + mitad, jA + mitad, sB_M4, 0, 0, mitad)

    sA_M5 = suma_sub(A, iA, jA, A, iA, jA + mitad)
    M5 = mult_mtz(sA_M5, 0, 0, B, iB + mitad, jB + mitad,mitad)

    sA_M6 = resta_sub(A, iA + mitad, jA, A, iA, jA)
    sB_M6 = suma_sub(B, iB, jB, B, iB, jB + mitad)
    M6 = mult_mtz(sA_M6, 0, 0, sB_M6, 0, 0, mitad)

    sA_M7 = resta_sub(A, iA, jA + mitad, A, iA + mitad, jA + mitad)
    sB_M7 = suma_sub(B, iB + mitad, jB, B, iB + mitad, jB + mitad)
    M7 = mult_mtz(sA_M7, 0, 0, sB_M7, 0, 0, mitad)

    C11 = resta(suma(M1, M4), M5)
    C11 = suma(C11, M7)
    
    C12 = suma(M3, M5)
    C21 = suma(M2, M4)
    
    C22 = suma(resta(M1, M2), M3)
    C22 = suma(C22, M6)

    C = [[0] * n for _ in range(n)]
    for i in range(mitad):
        for j in range(mitad):
            C[i][j] = C11[i][j]
            C[i][j + mitad] = C12[i][j]
            C[i + mitad][j] = C21[i][j]
            C[i + mitad][j + mitad] = C22[i][j]
            
    return C


n_mtz = int(input())
mtz_A = [0]*n_mtz
mtz_B = [0]*n_mtz


for i in range(n_mtz):
    mtz_A[i] = list(map(int,input().split()))

for i in range(n_mtz):
    mtz_B[i] = list(map(int,input().split()))

if not(n_mtz > 0 and  (n_mtz & (n_mtz - 1)) == 0):
    n_mtz2 = 1 << (n_mtz - 1).bit_length()
    for f in mtz_A:
        while len(f) < n_mtz2:
            f.append(0)

    while len(mtz_A) < n_mtz2:
        mtz_A.append([0] * n_mtz2)

    for f in mtz_B:
        while len(f) < n_mtz2:
            f.append(0)

    while len(mtz_B) < n_mtz2:
        mtz_B.append([0] * n_mtz2)

else:
    n_mtz2 = n_mtz

mtz_C = mult_mtz(mtz_A,0,0,mtz_B,0,0,n_mtz2)

for z1 in range(n_mtz):
        for z2 in range(n_mtz):
            if z2 == n_mtz-1:
            
                print(f"{mtz_C[z1][z2]}")
            else:
            
                print(f"{mtz_C[z1][z2]}", end=" ")
