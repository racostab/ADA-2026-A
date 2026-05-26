def average_prob():
    #P(BB) = [15/21]*[14/20] =1/2
    # (b/t)((b-1)/(t-1)) = 1/2
    #2b(b-1) = t(t-1)
    #Meta: encontrar pares positivos que den solución en reales 
    b = 15
    t = 21
    Lim = 10**12
    #xk+1​=3xk​+4yk​,yk+1​=2xk​+3yk​
    # x = (2t - 1) ; y = (2b - 1)
    while t <= Lim:
        Bnext = 3*b + 2*t - 2
        Tnext = 4*b + 3*t - 3
        b = Bnext
        t = Tnext
    return b
result = average_prob()
print(result)