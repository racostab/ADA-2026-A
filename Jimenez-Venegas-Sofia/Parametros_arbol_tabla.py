class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:
            if valor < actual.valor:
                if actual.izq is None:
                    actual.izq = nuevo
                    return
                actual = actual.izq
            else:
                if actual.der is None:
                    actual.der = nuevo
                    return
                actual = actual.der

    def mostrar(self):
        print("\nNodo\tIzq\tDer")
        self.recorrer(self.raiz)

    def recorrer(self, nodo):
        if nodo is not None:
            izq = nodo.izq.valor if nodo.izq else "-"
            der = nodo.der.valor if nodo.der else "-"

            print(f"{nodo.valor}\t{izq}\t{der}")

            self.recorrer(nodo.izq)
            self.recorrer(nodo.der)

arbol = Arbol()
cantidad = int(input("Número de nodos: "))
for i in range(cantidad):
    valor = int(input(f"Ingrese el nodo {i+1}: "))
    arbol.insertar(valor)

arbol.mostrar()