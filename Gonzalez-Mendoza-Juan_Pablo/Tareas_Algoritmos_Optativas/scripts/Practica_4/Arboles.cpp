
//  Práctica: Implementación de Árbol Binario con Tabla
//  Opción 1: Tabla con nodos y apuntadores
//  Opción 2: Tabla con hijo izquierdo y derecho (arreglo)
//  Materia: Análisis y Diseño de Algoritmos — CIC IPN
//  Alumno:  Juan Pablo González Mendoza
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <string>
using namespace std;

// 1: Tabla con nodos y apuntadores

struct Nodo {
    int dato;
    Nodo* izq;
    Nodo* der;
};
Nodo* crearNodo(int valor) {
    Nodo* nuevo = new Nodo;
    nuevo->dato = valor;
    nuevo->izq  = nullptr;
    nuevo->der  = nullptr;
    return nuevo;
}

Nodo* insertarBST(Nodo* raiz, int valor) {
    if (raiz == nullptr)
        return crearNodo(valor);
    if (valor < raiz->dato)
        raiz->izq = insertarBST(raiz->izq, valor);
    else if (valor > raiz->dato)
        raiz->der = insertarBST(raiz->der, valor);
    return raiz;
}
// Recorridos
void inorden(Nodo* raiz) {
    if (raiz == nullptr) return;
    inorden(raiz->izq);
    cout << raiz->dato << " ";
    inorden(raiz->der);
}
void preorden(Nodo* raiz) {
    if (raiz == nullptr) return;
    cout << raiz->dato << " ";
    preorden(raiz->izq);
    preorden(raiz->der);
}
void postorden(Nodo* raiz) {
    if (raiz == nullptr) return;
    postorden(raiz->izq);
    postorden(raiz->der);
    cout << raiz->dato << " ";
}
// Mostrar tabla: cada nodo con sus apuntadores
void mostrarTablaApuntadores(Nodo* raiz) {
    if (raiz == nullptr) return;
    cout << "  Indice | Dato | Dir. Nodo        | "
         << "Hijo Izq         | Hijo Der" << endl;
    cout << "  -------|------|------------------|"
         << "------------------|------------------" << endl;
    queue<Nodo*> cola;
    cola.push(raiz);
    int idx = 0;
    while (!cola.empty()) {
        Nodo* actual = cola.front();
        cola.pop();
        cout << "  " << setw(5) << idx << "  | "
             << setw(4) << actual->dato << " | "
             << setw(16) << actual << " | ";
        if (actual->izq)
            cout << setw(16) << actual->izq;
        else
            cout << setw(16) << "NULL";
        cout << " | ";
        if (actual->der)
            cout << setw(16) << actual->der;
        else
            cout << setw(16) << "NULL";
        cout << endl;
        if (actual->izq) cola.push(actual->izq);
        if (actual->der) cola.push(actual->der);
        idx++;
    }
}
void liberarArbol(Nodo* raiz) {
    if (raiz == nullptr) return;
    liberarArbol(raiz->izq);
    liberarArbol(raiz->der);
    delete raiz;
}

//  2: Tabla con hijo izquierdo y derecho

class ArbolTabla {
    static const int MAX_NODOS = 31; // soporte hasta 5 niveles
    static const int VACIO = -1;
    int datos[MAX_NODOS];
    int hijoIzq[MAX_NODOS]; // indice del hijo izquierdo
    int hijoDer[MAX_NODOS]; // indice del hijo derecho
    int padre[MAX_NODOS];   // indice del padre
    int numNodos;
public:
    ArbolTabla() : numNodos(0) {
        for (int i = 0; i < MAX_NODOS; i++) {
            datos[i]   = VACIO;
            hijoIzq[i] = VACIO;
            hijoDer[i] = VACIO;
            padre[i]   = VACIO;
        }
    }
    void insertar(int valor) {
        if (numNodos >= MAX_NODOS) {
            cout << "  Tabla llena, no se puede insertar "
                 << valor << endl;
            return;
        }
        int nuevo = numNodos;
        datos[nuevo] = valor;
        numNodos++;
        if (nuevo == 0) return; // es la raíz
        int actual = 0;
        while (true) {
            if (valor < datos[actual]) {
                if (hijoIzq[actual] == VACIO) {
                    hijoIzq[actual] = nuevo;
                    padre[nuevo] = actual;
                    return;
                }
                actual = hijoIzq[actual];
            } else {
                if (hijoDer[actual] == VACIO) {
                    hijoDer[actual] = nuevo;
                    padre[nuevo] = actual;
                    return;
                }
                actual = hijoDer[actual];
            }
        }
    }
    // Mostrar tabla completa
    void mostrarTabla() {
        cout << "  Indice | Dato | Padre | Hijo Izq | Hijo Der"
             << endl;
        cout << "  -------|------|-------|----------|--------"
             << endl;
        for (int i = 0; i < numNodos; i++) {
            cout << "  " << setw(5) << i << "  | "
                 << setw(4) << datos[i] << " | ";
            if (padre[i] == VACIO)
                cout << setw(5) << "---";
            else
                cout << setw(5) << padre[i];
            cout << " | ";
            if (hijoIzq[i] == VACIO)
                cout << setw(8) << "---";
            else
                cout << setw(8) << hijoIzq[i];
            cout << " | ";
            if (hijoDer[i] == VACIO)
                cout << setw(8) << "---";
            else
                cout << setw(8) << hijoDer[i];
            cout << endl;
        }
    }
    // Recorridos usando la tabla
    void inorden(int idx) {
        if (idx == VACIO) return;
        inorden(hijoIzq[idx]);
        cout << datos[idx] << " ";
        inorden(hijoDer[idx]);
    }
    void preorden(int idx) {
        if (idx == VACIO) return;
        cout << datos[idx] << " ";
        preorden(hijoIzq[idx]);
        preorden(hijoDer[idx]);
    }
    void postorden(int idx) {
        if (idx == VACIO) return;
        postorden(hijoIzq[idx]);
        postorden(hijoDer[idx]);
        cout << datos[idx] << " ";
    }
    int getRaiz() { return (numNodos > 0) ? 0 : VACIO; }
    int getNumNodos() { return numNodos; }
};
// ============================================================
//  OPCIÓN 2-B: Representación implícita (fórmulas de índices)
// ============================================================
class ArbolImplicito {
    static const int MAX_SIZE = 63;
    static const int VACIO = -1;
    int arr[MAX_SIZE];
    int capacidad;
public:
    ArbolImplicito() : capacidad(MAX_SIZE) {
        for (int i = 0; i < MAX_SIZE; i++)
            arr[i] = VACIO;
    }
    int hijoIzq(int i)  { return 2 * i + 1; }
    int hijoDer(int i)  { return 2 * i + 2; }
    int indicePadre(int i) { return (i - 1) / 2; }
    void insertar(int valor) {
        if (arr[0] == VACIO) {
            arr[0] = valor;
            return;
        }
        int i = 0;
        while (i < capacidad) {
            if (arr[i] == VACIO) {
                arr[i] = valor;
                return;
            }
            if (valor < arr[i])
                i = hijoIzq(i);
            else
                i = hijoDer(i);
        }
        cout << "  Arbol lleno (implicito)" << endl;
    }
    void mostrarTabla() {
        cout << "  Indice | Dato | Hijo Izq (2i+1) | "
             << "Hijo Der (2i+2) | Padre ((i-1)/2)" << endl;
        cout << "  -------|------|-----------------|"
             << "-----------------|----------------" << endl;
        for (int i = 0; i < capacidad; i++) {
            if (arr[i] == VACIO) continue;
            cout << "  " << setw(5) << i << "  | "
                 << setw(4) << arr[i] << " | ";
            int li = hijoIzq(i);
            if (li < capacidad && arr[li] != VACIO)
                cout << setw(15) << arr[li];
            else
                cout << setw(15) << "---";
            cout << " | ";
            int ri = hijoDer(i);
            if (ri < capacidad && arr[ri] != VACIO)
                cout << setw(15) << arr[ri];
            else
                cout << setw(15) << "---";
            cout << " | ";
            if (i == 0)
                cout << setw(14) << "RAIZ";
            else
                cout << setw(14) << arr[indicePadre(i)];
            cout << endl;
        }
    }
    void inorden(int i) {
        if (i >= capacidad || arr[i] == VACIO) return;
        inorden(hijoIzq(i));
        cout << arr[i] << " ";
        inorden(hijoDer(i));
    }
};
// ============================================================
//  MAIN
// ============================================================
int main() {
    // Datos de ejemplo para insertar
    int valores[] = {50, 30, 70, 20, 40, 60, 80, 10, 25, 35};
    int n = sizeof(valores) / sizeof(valores[0]);
    cout << "============================================" << endl;
    cout << "  PRACTICA: Arbol Binario con Tabla" << endl;
    cout << "  Analisis y Diseno de Algoritmos - CIC IPN" << endl;
    cout << "============================================" << endl;
    cout << "\n  Valores a insertar: ";
    for (int i = 0; i < n; i++) cout << valores[i] << " ";
    cout << endl << endl;
    // ---- OPCIÓN 1: Nodos con apuntadores ----
    cout << "========================================" << endl;
    cout << "  OPCION 1: Tabla con Nodos y Apuntadores" << endl;
    cout << "========================================" << endl;
    Nodo* raiz = nullptr;
    for (int i = 0; i < n; i++)
        raiz = insertarBST(raiz, valores[i]);
    cout << "\n  Tabla (recorrido por niveles):" << endl << endl;
    mostrarTablaApuntadores(raiz);
    cout << "\n  Recorrido Inorden:   ";
    inorden(raiz);
    cout << endl;
    cout << "  Recorrido Preorden:  ";
    preorden(raiz);
    cout << endl;
    cout << "  Recorrido Postorden: ";
    postorden(raiz);
    cout << endl << endl;
    liberarArbol(raiz);
    // ---- OPCIÓN 2: Tabla con hijo izq/der (explícita) ----
    cout << "========================================" << endl;
    cout << "  OPCION 2: Tabla con Hijo Izq y Der" << endl;
    cout << "  (Indices explicitos)" << endl;
    cout << "========================================" << endl;
    ArbolTabla arbolTabla;
    for (int i = 0; i < n; i++)
        arbolTabla.insertar(valores[i]);
    cout << "\n  Tabla:" << endl << endl;
    arbolTabla.mostrarTabla();
    cout << "\n  Recorrido Inorden:   ";
    arbolTabla.inorden(arbolTabla.getRaiz());
    cout << endl;
    cout << "  Recorrido Preorden:  ";
    arbolTabla.preorden(arbolTabla.getRaiz());
    cout << endl;
    cout << "  Recorrido Postorden: ";
    arbolTabla.postorden(arbolTabla.getRaiz());
    cout << endl << endl;
    // ---- OPCIÓN 2-B: Arreglo implícito (fórmulas) ----
    cout << "========================================" << endl;
    cout << "  OPCION 2-B: Arreglo Implicito" << endl;
    cout << "  (Formulas: 2i+1, 2i+2, (i-1)/2)" << endl;
    cout << "========================================" << endl;
    ArbolImplicito arbolImpl;
    for (int i = 0; i < n; i++)
        arbolImpl.insertar(valores[i]);
    cout << "\n  Tabla:" << endl << endl;
    arbolImpl.mostrarTabla();
    cout << "\n  Recorrido Inorden:   ";
    arbolImpl.inorden(0);
    cout << endl << endl;
    cout << "========================================" << endl;
    cout << "  COMPARACION" << endl;
    cout << "========================================" << endl;
    cout << "\n  Opcion 1 (Apuntadores):" << endl;
    cout << "    - Memoria: sizeof(Nodo) = " << sizeof(Nodo)
         << " bytes por nodo" << endl;
    cout << "    - Total: " << n << " nodos x "
         << sizeof(Nodo) << " = "
         << n * sizeof(Nodo) << " bytes" << endl;
    cout << "\n  Opcion 2 (Tabla indices):" << endl;
    cout << "    - Memoria: 4 arreglos de int" << endl;
    cout << "    - Total: " << n << " nodos x "
         << 4 * sizeof(int) << " = "
         << n * 4 * sizeof(int) << " bytes" << endl;
    cout << "\n  Opcion 2-B (Implicito):" << endl;
    cout << "    - Memoria: 1 arreglo de int" << endl;
    cout << "    - Sin apuntadores, acceso O(1) por indice" << endl;
    cout << "    - Ideal para arboles completos (heaps)" << endl;
    cout << "\n========================================" << endl;
    cout << "  Practica finalizada." << endl;
    cout << "========================================" << endl;
    return 0;
}
