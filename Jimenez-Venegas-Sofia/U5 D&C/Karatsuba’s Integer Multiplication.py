import sys

def karatsuba(numero1, numero2):
    if numero1 < 2 or numero2 < 2:
        return numero1 * numero2

    cantidad_bits = max(numero1.bit_length(), numero2.bit_length())
    mitad = cantidad_bits // 2

    parte_alta1 = numero1 >> mitad
    parte_baja1 = numero1 - (parte_alta1 << mitad)

    parte_alta2 = numero2 >> mitad
    parte_baja2 = numero2 - (parte_alta2 << mitad)

    producto_bajo = karatsuba(parte_baja1, parte_baja2)
    producto_alto = karatsuba(parte_alta1, parte_alta2)
    producto_cruzado = karatsuba(
        parte_baja1 + parte_alta1,
        parte_baja2 + parte_alta2
    )

    return (
        (producto_alto << (2 * mitad))
        + ((producto_cruzado - producto_alto - producto_bajo) << mitad)
        + producto_bajo
    )


def main():
    casos_prueba = int(sys.stdin.readline())

    for _ in range(casos_prueba):
        binario1, binario2 = sys.stdin.readline().split()

        numero1 = int(binario1, 2)
        numero2 = int(binario2, 2)

        resultado = karatsuba(numero1, numero2)

        print(bin(resultado)[2:])


if __name__ == "__main__":
    main()