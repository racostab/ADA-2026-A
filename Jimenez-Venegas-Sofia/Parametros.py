import inspect
import sys


def mostrar_pila():
    """Muestra las funciones que están actualmente en la pila."""

    print("\nPILA DE LLAMADAS")

    pila = inspect.stack()

    for nivel, marco in enumerate(pila):
        print(f"\nNivel {nivel}")
        print(f"Función: {marco.function}")

        variables = marco.frame.f_locals

        print("Variables locales:")
        for nombre, valor in variables.items():
            print(f"   {nombre} = {valor}")


def modificar_datos(datos):
    """
    Modifica un diccionario recibido como parámetro.
    Esto demuestra una modificación indirecta.
    """

    print("\nModificando datos...")

    datos["edad"] = 25
    datos["nombre"] = "Ana"


def tercera_funcion(datos_persona):
    print("\nEntrando a tercera_funcion()")

    mostrar_pila()

    modificar_datos(datos_persona)


def segunda_funcion(datos_persona):
    numero = 200

    print("\nEntrando a segunda_funcion()")
    print("numero =", numero)

    tercera_funcion(datos_persona)


def primera_funcion():
    numero = 100

    datos_persona = {
        "nombre": "Juan",
        "edad": 20
    }

    print("\nEntrando a primera_funcion()")
    print("numero =", numero)
    print("datos_persona =", datos_persona)

    segunda_funcion(datos_persona)

    print("\nDESPUÉS DE MODIFICAR")
    print(datos_persona)

print("Límite actual de recursión:")
print(sys.getrecursionlimit())

sys.setrecursionlimit(3000)

print("\nNuevo límite de recursión:")
print(sys.getrecursionlimit())

primera_funcion()