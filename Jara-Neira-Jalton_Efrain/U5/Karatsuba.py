# Author: Jalton Jara Neira
# Date: 15/06/2026
import sys

sys.setrecursionlimit(200000)

def karatsuba(x, y):
    #Caso base
    if x < 2 or y < 2:
        return x * y

    max_len = max(x.bit_length(), y.bit_length())

    if max_len <= 1:
        return x * y

    #Dividir
    m = max_len // 2


    x_izq = x >> m
    x_der = x & ((1<<m)-1)
    
    y_izq = y >> m
    y_der = y & ((1<<m)-1)

    #Llamadas recursivas de Karatsuba
    p1 = karatsuba(x_izq, y_izq)
    p2 = karatsuba(x_der, y_der)
    p3 = karatsuba(x_izq + x_der, y_izq + y_der)

    return (p1<<(2*m)) + ((p3-p1-p2)<<m) + p2


def main_program():
    input_data = sys.stdin.read().split()    
    if not input_data:
        return

    tc = int(input_data[0])    
    idx = 1
    for _ in range(tc):
        if idx >= len(input_data):
            break

        str_a = input_data[idx]
        str_b = input_data[idx+1]
        idx += 2

        int_a = int(str_a, 2)
        int_b = int(str_b, 2)

        resultado_entero = karatsuba(int_a, int_b)
        resultado_binario = bin(resultado_entero)[2:]
        print(resultado_binario)

if __name__ == '__main__':
    main_program()