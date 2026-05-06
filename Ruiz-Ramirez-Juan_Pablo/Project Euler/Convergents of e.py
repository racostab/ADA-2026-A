def get_coef(n):
    if n == 0:
        return 2
    elif n % 3 == 2:
        return 2 * (int((n+1)/3))
    else:
        return 1

def calculo_conv(n):
    hn1, hn2 = get_coef(0), 1
    kn1, kn2 = 1, 0
    for i in range(1, n+1):
        ai = get_coef(i)
        ha = ai * hn1 + hn2
        ka = ai * kn1 + kn2
        hn1, hn2 = ha, hn1
        kn1, kn2 = ka, kn1
    return hn1,kn1
num,den = calculo_conv(99)
Resultado = num/den
Digitos = []
for digito in str(num):
    Digitos.append(int(digito))
SumDig = sum(Digitos)
print(SumDig)