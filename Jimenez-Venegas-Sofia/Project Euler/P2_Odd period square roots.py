import math

def periodo(N):
    a0=int(math.sqrt(N))
    if a0*a0 == N:
        return 0

    m=0
    d=1
    a=a0
    count=0

    while True:
        m = d*a-m
        d = (N-m*m) // d
        a = (a0+m) // d
        count += 1

        if a == 2*a0:
            break

    return count



impares = 0
for N in range(2, 10000):
    if periodo(N)%2 == 1:
        impares += 1

print(impares)

