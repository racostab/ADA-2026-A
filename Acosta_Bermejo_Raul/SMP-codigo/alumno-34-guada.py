# ==============================================
# GGUERRA
# Stable Matching - Gale-Shapley
# ==============================================

import re

# ========================================================== UTILERIAS - PRINT'S
debug = False
def impresion_args(*args, **kwargs):
    if debug:
        print(*args, **kwargs)
   
def impresion(argumento):
    if debug:
        print(argumento)


def gale_shapley(proposers_pref, receivers_pref):
    impresion(f" algoritmo Gale-Shapley")
    libres = list(proposers_pref.keys())
    compromisos = {}
    propuestas = {p: [] for p in proposers_pref}
    impresion(f"While libres: {libres}")
    while libres:
        p = libres[0]
        for r in proposers_pref[p]:
            if r not in propuestas[p]:
                propuestas[p].append(r)

                if r not in compromisos:
                    compromisos[r] = p
                    libres.pop(0)
                else:
                    actual = compromisos[r]
                    ranking = receivers_pref[r]

                    if ranking.index(p) < ranking.index(actual):
                        compromisos[r] = p
                        libres.pop(0)
                        libres.append(actual)
                break
    impresion(f" compromisos: {compromisos}")
    return compromisos

def main_test():
    # 
    # Parámetros de entrada fijos para probar el caso 4
    N = 5
    proposer = 'w'  # mujeres proponen
    impresion(f"N: {N}, proposer: {proposer}")  
    hombres_pref = {}
    mujeres_pref = {} 

    hombres_pref = {
        'Adam': ['Beth', 'Amy', 'Diane', 'Ellen', 'Cara'],
        'Bill': ['Diane', 'Beth', 'Amy', 'Cara', 'Ellen'],
        'Carl':['Beth', 'Ellen', 'Cara', 'Diane', 'Amy'],
        'Dan':['Amy', 'Diane', 'Cara', 'Beth', 'Ellen'],
        'Eric':['Beth', 'Diane', 'Amy', 'Ellen', 'Cara'],
    }

    mujeres_pref = {
        'Amy':['Eric', 'Adam', 'Bill', 'Dan', 'Carl'],
        'Beth':['Carl', 'Bill', 'Dan', 'Adam', 'Eric'],
        'Cara':['Bill', 'Carl', 'Dan', 'Eric', 'Adam'],
        'Diane':['Adam', 'Eric', 'Dan', 'Carl', 'Bill'],
        'Ellen':['Dan', 'Bill', 'Eric', 'Carl', 'Adam']
    }

    impresion(f"N: {N}")
    impresion(f"proposer: {proposer}")
    impresion(f"mujeres_pref {mujeres_pref}")
    impresion(f"hombres_pref: {hombres_pref}")
    

    # Gale-Shapley
    if proposer == 'w':  # mujeres proponen
        resultado = gale_shapley(mujeres_pref, hombres_pref)
        parejas = {h: m for m, h in resultado.items()}
        orden_general = list(mujeres_pref.keys())
    else:  # hombres proponen
        resultado = gale_shapley(hombres_pref, mujeres_pref)
        parejas = {m: h for h, m in resultado.items()}
        orden_general = list(hombres_pref.keys())

    impresion(f"Resultado bruto: {resultado}")
    impresion(f"Parejas finales: {parejas}")
    impresion(f"orden_general: {orden_general}")
    # Imprimir en orden dinámico
    for i in range(len(orden_general)):
        persona = orden_general[i]
        impresion(f"{persona} {parejas[persona]}")



def main():
    impresion(f"Iniciando ejecución del algoritmo Gale-Shapley")
    first_line = input().split()
    impresion(f"Entrada recibida: {first_line}")
    N = int(first_line[0]) # Numero entre 1 y 100
    proposer = first_line[1]  # 'm' hombres, 'w' mujeres
    impresion(f"N: {N}, proposer: {proposer}")  
    
    hombres_pref = {}
    mujeres_pref = {}

    # Leer hombres
    for _ in range(N):
        datos = input().split()
        impresion(f"datos:{datos}")
        nombre = datos[0]
        impresion(f"nombre: {nombre}")
        hombres_pref[nombre] = datos[1:]
        impresion(f"hombres_pref {hombres_pref}")
        
    # Leer mujeres
    for _ in range(N):
        datos = input().split()
        nombre = datos[0]
        mujeres_pref[nombre] = datos[1:]
        impresion(f"mujeres_pref {mujeres_pref}")
    
    # Gale-Shapley
    if proposer == 'w':  # mujeres proponen
        resultado = gale_shapley(mujeres_pref, hombres_pref)
        parejas = {h: m for m, h in resultado.items()}
        orden_general = list(mujeres_pref.keys())
    else:  # hombres proponen
        resultado = gale_shapley(hombres_pref, mujeres_pref)
        parejas = {m: h for h, m in resultado.items()}
        orden_general = list(hombres_pref.keys())

    for i in range(len(orden_general)):
        persona = orden_general[i]
        print(f"{persona} {parejas[persona]}")

if __name__ == "__main__":
    # Ejecutar la función de prueba con datos jarcodeados
    #main_test()
    main()