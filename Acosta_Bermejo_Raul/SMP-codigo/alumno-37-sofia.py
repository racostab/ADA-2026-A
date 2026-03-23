import sys
var = sys.stdin.read()
listas = [line.strip().split() for line in var.splitlines()]

datos = listas[0]
n = int(datos[0])
quien_propone = datos[1]

m = {}
w = {}

for i in range(1, n+1):
    m[listas[i][0]] = listas[i][1:]

for i in range(n+1, 2*n+1):
    w[listas[i][0]] = listas[i][1:]

if quien_propone == 'm':
    proponedores = m
    receptores = w
else:
    proponedores = w
    receptores = m

ranking = {}

for i in receptores:
    ranking[i] = {}
    
    posicion = 0
    for j in receptores[i]:
        ranking[i][j] = posicion
        posicion += 1

proponedor_receptor = {}               
receptor_proponedor = {}           

pretendientes = list(proponedores.keys())

propuestas = {}
for p in proponedores:
    propuestas[p] = 0

while pretendientes:
    pretendiente = pretendientes[0]

    pareja = proponedores[pretendiente][propuestas[pretendiente]]
    propuestas[pretendiente] += 1

    if pareja not in receptor_proponedor:
        proponedor_receptor[pretendiente] = pareja
        receptor_proponedor[pareja] = pretendiente
        pretendientes.remove(pretendiente)

    else:
        pareja_actual = receptor_proponedor[pareja]

        if ranking[pareja][pretendiente] < ranking[pareja][pareja_actual]:
            proponedor_receptor.pop(pareja_actual)
            pretendientes.append(pareja_actual)

            proponedor_receptor[pretendiente] = pareja
            receptor_proponedor[pareja] = pretendiente
            pretendientes.remove(pretendiente)

if quien_propone == 'm':
    orden = list(m.keys())
else:
    orden = list(w.keys())

for a in orden:
    print(a, proponedor_receptor[a])
 