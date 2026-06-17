def busqueda_binaria(trabajos, indice):
    izquierda = 0
    derecha = indice - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if trabajos[medio][1] <= trabajos[indice][0]:
            if medio == derecha or trabajos[medio + 1][1] > trabajos[indice][0]:
                return medio
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


while True:
    try:
        n = int(input().strip())
    except EOFError:
        break
    except:
        continue

    trabajos = []

    for i in range(n):
        inicio, fin, ganancia = map(int, input().split())
        trabajos.append((inicio, fin, ganancia, i + 1))

    trabajos.sort(key=lambda x: x[1])

    dp = [0] * n
    tomar = [False] * n
    previo = [-1] * n

    for i in range(n):
        incluir = trabajos[i][2]

        j = busqueda_binaria(trabajos, i)

        if j != -1:
            incluir += dp[j]

        excluir = dp[i - 1] if i > 0 else 0

        if incluir > excluir:
            dp[i] = incluir
            tomar[i] = True
            previo[i] = j
        else:
            dp[i] = excluir

    seleccionados = []
    i = n - 1

    while i >= 0:
        incluir = trabajos[i][2]

        j = busqueda_binaria(trabajos, i)

        if j != -1:
            incluir += dp[j]

        excluir = dp[i - 1] if i > 0 else 0

        if incluir > excluir:
            seleccionados.append(trabajos[i][3])
            i = j
        else:
            i -= 1

    seleccionados.sort()

    print(dp[n - 1])

    if seleccionados:
        print(*seleccionados)
    else:
        print()