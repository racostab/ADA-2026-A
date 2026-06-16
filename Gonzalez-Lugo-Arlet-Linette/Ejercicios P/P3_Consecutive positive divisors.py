def main():
    limite = 10000000

    # SPF (smallest prime factor)
    spf = list(range(limite + 1))

    for i in range(2, int(limite**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limite + 1, i):
                if spf[j] == j:
                    spf[j] = i

    divisores = [1] * (limite + 1)
    pot = [0] * (limite + 1)

    for i in range(2, limite + 1):
        p = spf[i]
        m = int(i / p)

        if spf[m] == p:
            pot[i] = pot[m] + 1
            divisores[i] = int(divisores[m] / (pot[m] + 1)) * (pot[i] + 1)
        else:
            pot[i] = 1
            divisores[i] = divisores[m] * 2

    contador = 0
    for i in range(2, limite):
        if divisores[i] == divisores[i + 1]:
            contador += 1

    print(contador)


if __name__ == "__main__":
    main()