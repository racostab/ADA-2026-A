# Author: Jalton Jara Neira
# Date: 15/06/2026
import sys
import math

def dist_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_rec(puntos_x, puntos_y):
    n = len(puntos_x)
    
    #Caso base
    if n <= 3:
        min_d = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                d = dist_euclidiana(puntos_x[i], puntos_x[j])
                if d < min_d:
                    min_d = d
        return min_d

    #Dividir, punto medio
    mid = n // 2
    punto_medio = puntos_x[mid]

    puntos_y_izq = []
    puntos_y_der = []
    for p in puntos_y:
        if p[0] < punto_medio[0]:
            puntos_y_izq.append(p)
        else:
            puntos_y_der.append(p)

    d_izq = closest_pair_rec(puntos_x[:mid], puntos_y_izq)
    d_der = closest_pair_rec(puntos_x[mid:], puntos_y_der)

    delta = min(d_izq, d_der)
    franja = [p for p in puntos_y if abs(p[0] - punto_medio[0]) < delta]

    tam_franja = len(franja)
    for i in range(tam_franja):
        for j in range(i + 1, min(i + 8, tam_franja)):
            d = dist_euclidiana(franja[i], franja[j])
            if d < delta:
                delta = d

    return delta


def main_program():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    total_tokens = len(input_data)

    while idx < total_tokens:
        n = int(input_data[idx])
        idx += 1

        puntos = []
        for _ in range(n):
            if idx >= total_tokens:
                break
            x = int(input_data[idx])
            y = int(input_data[idx+1])
            idx += 2
            puntos.append((x, y))

        if not puntos:
            break

        puntos_x = sorted(puntos, key=lambda p: p[0])
        puntos_y = sorted(puntos, key=lambda p: p[1])

        #distancia mínima
        resultado = closest_pair_rec(puntos_x, puntos_y)
        print(f"{resultado:.6f}")

if __name__ == '__main__':
    main_program()