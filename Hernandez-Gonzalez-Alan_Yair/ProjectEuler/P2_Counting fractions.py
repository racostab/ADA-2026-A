#Generamos un arreglo con los números hasta el 1,000,000 para aplicar la Criba de Totient
phi = list(range(1000001))

for i in range(2, 1000001):
    if phi[i] == i:  # i es primo
        #Se generan todos los multiplos del número primo
        for j in range(i, 1000001, i):
            #se modifican los multiplos del número primo
            phi[j] -= phi[j] // i

print(sum(phi[2:]))