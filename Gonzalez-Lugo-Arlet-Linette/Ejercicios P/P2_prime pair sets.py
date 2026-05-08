import math

def es_primo(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def concat(a, b):
    return int(str(a) + str(b))

def valido(a, b):
    return es_primo(concat(a, b)) and es_primo(concat(b, a))

def generar_primos(limite):
    primos = []
    for i in range(2, limite):
        if es_primo(i):
            primos.append(i)
    return primos

def buscar(primos, grupo, inicio):
    if len(grupo) == 5:
        return grupo
    
    for i in range(inicio, len(primos)):
        p = primos[i]
        cumple = True
        
        for g in grupo:
            if not valido(p, g):
                cumple = False
                break
        
        if cumple:
            res = buscar(primos, grupo + [p], i + 1)
            if res:
                return res
    return None

def resolver():
    primos = generar_primos(10000)
    resultado = buscar(primos, [], 0)
    if resultado:
        #print("Conjunto:", resultado)
        print(sum(resultado))
    else:
        print("No encontrado")

resolver()