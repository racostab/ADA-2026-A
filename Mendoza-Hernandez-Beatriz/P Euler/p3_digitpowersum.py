def digit_sum(n):
    return sum(int(d) for d in str(n))

sequence = []

# Buscar números con la propiedad
for s in range(2, 200):

    k = 2
    while True:

        value = s ** k

        # Si el número ya es demasiado grande, detenemos
        if value > 10**20:
            break

        # Debe tener al menos 2 dígitos
        if value >= 10 and digit_sum(value) == s:
            sequence.append(value)

        k += 1

# Ordenar y eliminar repetidos
sequence = sorted(set(sequence))

# Obtener a30
a30 = sequence[29]

print( a30)