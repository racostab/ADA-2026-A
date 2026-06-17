class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo_actual, valor):
        if nodo_actual is None:
            return Nodo(valor)


        if valor < nodo_actual.valor:
            nodo_actual.izq = self._insertar_rec(nodo_actual.izq, valor)
        else:
            nodo_actual.der = self._insertar_rec(nodo_actual.der, valor)
        
        return nodo_actual

    def mostrar(self):
        print("\nNodo\tIzq\tDer")
        print("----------------------")
        self._recorrer(self.raiz)

    def _recorrer(self, nodo):
        if nodo is not None:
            izq = nodo.izq.valor if nodo.izq else "-"
            der = nodo.der.valor if nodo.der else "-"
            print(f"{nodo.valor}\t{izq}\t{der}")
            
            self._recorrer(nodo.izq)
            self._recorrer(nodo.der)

arbol = Arbol()
cantidad = int(input("¿Cuántos nodos quieres ingresar?: "))

for i in range(cantidad):
    valor = int(input(f"Ingrese el nodo {i+1}: "))
    arbol.insertar(valor)

arbol.mostrar()