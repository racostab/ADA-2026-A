#------------------------- Criba de primos -------------------------
def sieve(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False

    for i in range(2, int(limite**0.5) + 1):
        if primos[i]:
            for j in range(i*i, limite + 1, i):
                primos[j] = False

    return [i for i in range(2, limite + 1) if primos[i]]


#------------------------- Comparar digitos -------------------------
def comparar(a, b):
    if len(str(a)) != len(str(b)):
        return False
    return sorted(str(a)) == sorted(str(b))


#-------------------- Encontrar ratio minimo -----------------------
def permutacion_totient(limite):
    primos = sieve(10000)

    min_ratio = float('inf')
    n_min = 0

    for i in range(len(primos)):
        for j in range(i, len(primos)):
            p = primos[i]
            q = primos[j]

            n = p * q
            if n > limite:
                break

            phi = (p - 1) * (q - 1)

            if comparar(n, phi):
                ratio = n / phi

                if ratio < min_ratio:
                    min_ratio = ratio
                    n_min = n

    return n_min


#------------------------- MAIN -------------------------
n = 10000000
print(permutacion_totient(n))
