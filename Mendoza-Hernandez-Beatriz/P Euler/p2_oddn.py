import math

def periodo(N):
    a0 = int(math.isqrt(N))
    if a0 * a0 == N:
        return 0  # cuadrado perfecto

    m = 0
    d = 1
    a = a0

    period = 0

    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d

        period += 1

        if a == 2 * a0:
            break

    return period


contador = 0

for N in range(2, 10001):
    if periodo(N) % 2 == 1:
        contador += 1

print(contador)