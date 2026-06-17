def mochila(capacidad, pesos, valores):
    dp = [0] * (capacidad + 1)
    objetos = [[] for _ in range(capacidad + 1)]
    for i in range(len(pesos)):
        peso = pesos[i]
        valor = valores[i]
        for j in range(capacidad, peso - 1, -1):
            if dp[j - peso] + valor > dp[j]:
                dp[j] = dp[j - peso] + valor
                objetos[j] = objetos[j - peso] + [i + 1]

    return dp[capacidad], sorted(objetos[capacidad])


def entrada():
    n, capacidad = map(int, input().split())
    valores = []
    pesos = []

    for _ in range(n):
        valor, peso = map(int, input().split())
        valores.append(valor)
        pesos.append(peso)

    return capacidad, pesos, valores


def main():
    capacidad, pesos, valores = entrada()
    valor_maximo, seleccion = mochila(capacidad, pesos, valores)
    print(valor_maximo)
    print(*seleccion)

if __name__ == "__main__":
    main()
