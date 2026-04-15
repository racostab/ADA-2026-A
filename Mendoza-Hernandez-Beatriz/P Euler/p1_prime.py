import math

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(math.sqrt(n)) + 1

    for i in range(3, limite, 2):
        if n % i == 0:
            return False

    return True


def primo_n(n):
    contador = 0
    num = 1

    while contador < n:
        num += 1
        if es_primo(num):
            contador += 1

    return num


# Encontrar el primo 10001
print(primo_n(10001))