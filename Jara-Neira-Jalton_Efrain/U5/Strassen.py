# Author: Jalton Jara Neira
# Date: 15/06/2026
import sys

def sumar_matrices(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)
    return resultado

def restar_matrices(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] - B[i][j])
        resultado.append(fila)
    return resultado


def multiplicar(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def strassen(A, B):
    n = len(A)
    
    #Caso base 
    if n <= 64:
        return multiplicar(A, B)
        
    mid = n // 2
    
    #Dividir en 4 cuadrantes
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    #productos de Strassen
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
    C22 = restar_matrices(restar_matrices(sumar_matrices(P5, P1), P3), P7)
    
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
        
    return C

def main_program():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n_original = int(input_data[0])
    idx = 1
    
    A_original = []
    for _ in range(n_original):
        fila = [int(input_data[idx+j]) for j in range(n_original)]
        A_original.append(fila)
        idx += n_original
        
    B_original = []
    for _ in range(n_original):
        fila = [int(input_data[idx+j]) for j in range(n_original)]
        B_original.append(fila)
        idx += n_original

    n_potencia = 1
    while n_potencia < n_original:
        n_potencia *= 2
        
    A = [[0] * n_potencia for _ in range(n_potencia)]
    B = [[0] * n_potencia for _ in range(n_potencia)]
    
    for i in range(n_original):
        for j in range(n_original):
            A[i][j] = A_original[i][j]
            B[i][j] = B_original[i][j]
            
    C_potencia = strassen(A, B)

    for i in range(n_original):
        print(*(C_potencia[i][:n_original]))

if __name__ == '__main__':
    main_program()