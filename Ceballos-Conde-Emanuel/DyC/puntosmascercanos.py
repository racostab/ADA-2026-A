import math

user_input = input()
numero_puntos = int(user_input)

puntos = []
for _ in range(numero_puntos):
    user_input = input()
    coordenadas = list(map(int, user_input.split()))
    puntos.append(tuple(coordenadas))


def calcular_distancia(punto_A, punto_B):
    return math.sqrt((punto_A[0] - punto_B[0])**2 + (punto_A[1] - punto_B[1])**2)


def buscar_casos_base(sub_lista):
    distancia_minima = float('inf')
    for i in range(len(sub_lista)):
        for j in range(i + 1, len(sub_lista)):
            d = calcular_distancia(sub_lista[i], sub_lista[j])
            if d < distancia_minima:
                distancia_minima = d
    return distancia_minima


def buscar_franja_cercana(franja, d_minima):
    distancia_minima = d_minima
    franja.sort(key=lambda punto: punto[1])

    for i in range(len(franja)):
        j = i + 1
        while j < len(franja) and (franja[j][1] - franja[i][1]) < distancia_minima:
            d = calcular_distancia(franja[i], franja[j])
            if d < distancia_minima:
                distancia_minima = d
            j += 1
            
    return distancia_minima


def encontrar_par_cercano(puntos_ordenados_x):
    size = len(puntos_ordenados_x)
    
    if size <= 3:
        return buscar_casos_base(puntos_ordenados_x)

    mitad = size // 2
    punto_mitad = puntos_ordenados_x[mitad]

    distancia_izquierda = encontrar_par_cercano(puntos_ordenados_x[:mitad])
    distancia_derecha = encontrar_par_cercano(puntos_ordenados_x[mitad:])

    d_minima = min(distancia_izquierda, distancia_derecha)

    franja = []
    for punto in puntos_ordenados_x:
        if abs(punto[0] - punto_mitad[0]) < d_minima:
            franja.append(punto)

    return min(d_minima, buscar_franja_cercana(franja, d_minima))


puntos.sort(key=lambda punto: punto[0])
resultado = encontrar_par_cercano(puntos)

print(f"{resultado:.6f}")