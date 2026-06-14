import math

limite = 10**8
p_limite = limite//2
primos = []
es_primo = [True]*(p_limite+1)

for p in range(2, p_limite + 1):
    if es_primo[p]:
        primos.append(p)
        for i in range(p * p, p_limite + 1, p):
            es_primo[i] = False

numero_de_primos= len(primos)
num_semiprimos = 0
puntero_derecho = numero_de_primos -1

for puntero_izquierdo in range(numero_de_primos):
    p = primos[puntero_izquierdo]

    if (p*p) > limite:
        break
    
    while puntero_derecho >= puntero_izquierdo and p*primos[puntero_derecho]>=limite:
        puntero_derecho -=1
    
    if puntero_derecho >= puntero_izquierdo:
        num_semiprimos += (puntero_derecho - puntero_izquierdo +1)

print(num_semiprimos)