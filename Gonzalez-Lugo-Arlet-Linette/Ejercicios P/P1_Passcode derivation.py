def resolver():
    intentos = [
        "319", "680", "180", "690", "129",
        "620", "762", "689", "762", "318",
        "368", "710", "720", "710", "629",
        "168", "160", "689", "716", "731",
        "736", "729", "316", "729", "729",
        "710", "769", "290", "719", "680",
        "318", "389", "162", "289", "162",
        "718", "729", "319", "790", "680",
        "890", "362", "319", "760", "316",
        "729", "380", "319", "728", "716"
    ]
    
    digitos = set()
    for intento in intentos:
        for c in intento:
            digitos.add(c)
    
    restricciones = set()
    for intento in intentos:
        restricciones.add((intento[0], intento[1]))
        restricciones.add((intento[1], intento[2]))
        restricciones.add((intento[0], intento[2]))
    
    cambio = True
    while cambio:
        cambio = False
        nuevas = set()
        for a, b in restricciones:
            for c, d in restricciones:
                if b == c and (a, d) not in restricciones:
                    nuevas.add((a, d))
                    cambio = True
        restricciones.update(nuevas)
    
    anterior = {d: set() for d in digitos}
    siguiente = {d: set() for d in digitos}
    
    for a, b in restricciones:
        siguiente[a].add(b)
        anterior[b].add(a)
    
    resultado = []
    while digitos:
        disponibles = [d for d in digitos if not anterior[d]]
        if not disponibles:
            break
        disponibles.sort()
        elegido = disponibles[0]
        resultado.append(elegido)
        digitos.remove(elegido)
        for sig in list(siguiente[elegido]):
            anterior[sig].remove(elegido)
    
    return ''.join(resultado)

print(resolver())