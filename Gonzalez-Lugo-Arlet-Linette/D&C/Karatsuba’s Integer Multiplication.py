def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(x.bit_length(), y.bit_length())
    m = int(n / 2)

    high1 = x >> m
    low1 = x - (high1 << m)
    high2 = y >> m
    low2 = y - (high2 << m)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return (z2 << (2 * m)) + ((z1 - z2 - z0) << m) + z0


def resolver():
    t = int(input().strip())

    for _ in range(t):
        a, b = input().split()
        x = int(a, 2)
        y = int(b, 2)
        res = karatsuba(x, y)
        print(bin(res)[2:])


resolver()