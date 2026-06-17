# Author: Jalton Jara Neira
# Date: 15/06/2026
import sys

def mochila(n, capacidad, pesos, valores):
    opt = []
    for _ in range(n+1):
        fila = [0] * (capacidad+1)
        opt.append(fila)

    for i in range(1, n+1):
        w_i = pesos[i-1]
        v_i = valores[i-1]
        
        for j in range(capacidad+1):
            if w_i <= j:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j-w_i] + v_i)
            else:

                opt[i][j] = opt[i-1][j]

    ganancia_maxima = opt[n][capacidad]

    items_elegidos = []
    peso_actual = capacidad
    
    for i in range(n, 0, -1):
        if ganancia_maxima <= 0:
            break
        if opt[i][peso_actual] != opt[i-1][peso_actual]:
            items_elegidos.append(i) 
            peso_actual -= pesos[i-1]

    items_elegidos.sort()
    
    return ganancia_maxima, items_elegidos


def main_program():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    total_tokens = len(input_data)
    
    while idx < total_tokens:
        if idx >= total_tokens:
            break

        n = int(input_data[idx])
        capacidad = int(input_data[idx+1])
        idx += 2
        
        valores = []
        pesos = []

        for _ in range(n):
            valores.append(int(input_data[idx]))
            pesos.append(int(input_data[idx+1]))
            idx += 2

        beneficio, items = mochila(n, capacidad, pesos, valores)

        print(beneficio)
        print(*(items))

if __name__ == '__main__':
    main_program()