import sys

datos = list(map(int, sys.stdin.read().split()))
posicion = 0

while posicion < len(datos):
    cantidad_objetos = datos[posicion]
    posicion += 1

    if posicion >= len(datos):
        break

    capacidad = datos[posicion]
    posicion += 1

    valores = []
    pesos = []

    for _ in range(cantidad_objetos):
        valor = datos[posicion]
        peso = datos[posicion + 1]
        posicion += 2

        valores.append(valor)
        pesos.append(peso)

    dp = [[0] * (capacidad + 1) for _ in range(cantidad_objetos + 1)]

    for i in range(1, cantidad_objetos + 1):
        valor_actual = valores[i - 1]
        peso_actual = pesos[i - 1]

        for peso_disponible in range(capacidad + 1):
            dp[i][peso_disponible] = dp[i - 1][peso_disponible]

            if peso_actual <= peso_disponible:
                dp[i][peso_disponible] = max(
                    dp[i][peso_disponible],
                    dp[i - 1][peso_disponible - peso_actual] + valor_actual
                )

    ganancia_maxima = dp[cantidad_objetos][capacidad]
    objetos_elegidos = []
    peso_restante = capacidad

    for i in range(cantidad_objetos, 0, -1):
        if dp[i][peso_restante] != dp[i - 1][peso_restante]:
            objetos_elegidos.append(i)  # índice 1-based
            peso_restante -= pesos[i - 1]

    objetos_elegidos.reverse()

    print(ganancia_maxima)

    if objetos_elegidos:
        print(*objetos_elegidos)
    else:
        print()