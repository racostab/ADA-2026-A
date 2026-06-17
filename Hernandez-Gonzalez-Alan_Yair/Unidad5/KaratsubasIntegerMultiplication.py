import sys

input = sys.stdin.readline

def karatsuba(x_bin, y_bin):
    #completando longitudes
    n = max(len(x_bin), len(y_bin))
    x_bin = x_bin.zfill(n)
    y_bin = y_bin.zfill(n)

    #caso base
    if n == 1:
        return int(x_bin) * int(y_bin)

    
    m = n // 2
    x1, x0 = x_bin[:-m], x_bin[-m:]
    y1, y0 = y_bin[:-m], y_bin[-m:]


    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    x1_x0 = bin(int(x1, 2) + int(x0, 2))[2:]
    y1_y0 = bin(int(y1, 2) + int(y0, 2))[2:]
    z1 = karatsuba(x1_x0, y1_y0) - z2 - z0

    return (z2 << (2 * m)) + (z1 << m) + z0



n = int(input())
for _ in range(n):
    parts = input().split()
    a_bin = parts[0].replace('_', '')
    b_bin = parts[1].replace('_', '')

    if a_bin == '0' or b_bin == '0':
        print(0) 

    resultado = karatsuba(a_bin, b_bin)
    print(bin(resultado)[2:])

