# Author: Jalton Efrain Jara Neira
# Date: 27/02/2026 
import sys

def gsp():
    input_all = sys.stdin.read().split()
    if not input_all:
        return
    
    n = int(input_all[0])
    propone = input_all[1].lower()

    orden_bloque1 = []
    bloque1_pref = {}
    ptr = 2
    for _ in range(n):
        nombre = input_all[ptr]
        orden_bloque1.append(nombre)
        bloque1_pref[nombre] = input_all[ptr+1 : ptr+1+n]
        ptr += 1+n
        
    orden_bloque2 = []
    bloque2_pref = {}
    for _ in range(n):
        nombre = input_all[ptr]
        orden_bloque2.append(nombre)
        bloque2_pref[nombre] = input_all[ptr+1 : ptr+1+n]
        ptr += 1+n

    if propone == 'm':
        proponentes = {h: list(pref) for h, pref in bloque1_pref.items()}
        receptores = bloque2_pref
    else:
        proponentes = {m: list(pref) for m, pref in bloque2_pref.items()}
        receptores = bloque1_pref

    rank_receptores = {r: {p: i for i, p in enumerate(lista)} for r, lista in receptores.items()}
    parejas = {r: None for r in receptores}
    libres = list(proponentes.keys())

    while libres:
        p = libres.pop(0)
        lista_p = proponentes[p]
        if not lista_p: continue
        
        candidata = lista_p.pop(0)
        actual = parejas[candidata]

        if actual is None:
            parejas[candidata] = p
        else:
            if rank_receptores[candidata][p] < rank_receptores[candidata][actual]:
                parejas[candidata] = p
                libres.append(actual)
            else:
                libres.append(p)

    emparejamiento_final = {}
    for r, p in parejas.items():
        emparejamiento_final[r] = p
        emparejamiento_final[p] = r

    if propone == 'm':
        orden_salida = orden_bloque1
    else:
        orden_salida = orden_bloque2

    for persona in orden_salida:
        pareja = emparejamiento_final[persona]
        print(f"{persona} {pareja}")

if __name__ == "__main__":
    gsp()
 