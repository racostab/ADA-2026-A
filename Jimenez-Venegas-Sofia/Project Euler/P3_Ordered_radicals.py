def compute_rad(limit):
    rad = [1] * (limit + 1)

    for i in range(2, limit + 1):
        if rad[i] == 1:  # i es primo
            for j in range(i, limit + 1, i):
                rad[j] *= i

    return rad


def find_E_k(limit, k):
    rad = compute_rad(limit)
    values = [(rad[n], n) for n in range(1, limit + 1)]
    values.sort()
    return values[k - 1][1]

limit = 100000
k = 10000

resultado = find_E_k(limit, k)
print(resultado)