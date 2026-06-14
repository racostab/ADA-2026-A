import json
import random

def generar_parejas(num_parejas, filename):
    men = [f"M{i}" for i in range(1, num_parejas + 1)]
    women = [f"W{i}" for i in range(1, num_parejas + 1)]
    men_pref = {}
    women_pref = {}

    for m in men:
        pref = women.copy()
        random.shuffle(pref)
        men_pref[m] = pref

    for w in women:
        pref = men.copy()
        random.shuffle(pref)
        women_pref[w] = pref

    data = {
        "num_parejas": num_parejas,
        "men_pref": men_pref,
        "women_pref": women_pref
    }

    with open("../DAT/"+filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Generado: {filename:} | Parejas: {num_parejas}")


print("Generando archivos")

for i in range(1, 26):

    k=12
    exponente = (i - 1) / 24
    #el numero maximo de parejas generadas es 2^k+1
    numero_de_parejas_exp= int(round(2 * ((2**k) ** exponente)))

    salto = ((2**(k+1) -2))/24
    numero_de_parejas_lineal = int(round(2 + ((i-1)*salto)))
    
    numero_de_parejas = numero_de_parejas_exp
    
    nombre_archivo = f"input{i}.json"
    generar_parejas(numero_de_parejas, nombre_archivo)

print("\nProceso finalizado")