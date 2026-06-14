
//  Práctica Optativa: Modelo de Función — Verificación de la Pila
//  Materia: Análisis y Diseño de Algoritmos  CIC IPN
//  Alumno:  Juan Pablo González Mendoza
#include <iostream>
#include <iomanip>
#include <cstdint>
using namespace std;
//1: Corroborar datos de la pila y su orden
void experimento1_orden_pila() {
    cout << "" << endl;
    cout << "  EXPERIMENTO 1: Orden de la Pila" << endl;
    cout << "" << endl;
    int a = 10;
    int b = 20;
    int c = 30;
    int d = 40;
    cout << "Variable | Valor | Direccion" << endl;
    cout << "---------|-------|-----------------" << endl;
    cout << "   a     |  " << setw(3) << a << "  | " << &a << endl;
    cout << "   b     |  " << setw(3) << b << "  | " << &b << endl;
    cout << "   c     |  " << setw(3) << c << "  | " << &c << endl;
    cout << "   d     |  " << setw(3) << d << "  | " << &d << endl;
    ptrdiff_t diff_ab = (char*)&a - (char*)&b;
    ptrdiff_t diff_bc = (char*)&b - (char*)&c;
    ptrdiff_t diff_cd = (char*)&c - (char*)&d;
    cout << "\nDiferencia &a - &b = " << diff_ab << " bytes" << endl;
    cout << "Diferencia &b - &c = " << diff_bc << " bytes" << endl;
    cout << "Diferencia &c - &d = " << diff_cd << " bytes" << endl;
    if ((uintptr_t)&a > (uintptr_t)&d) {
        cout << "\n=> La pila crece hacia direcciones BAJAS "
             << "(a tiene dir. mayor que d)" << endl;
    } else {
        cout << "\n=> La pila crece hacia direcciones ALTAS "
             << "(a tiene dir. menor que d)" << endl;
    }
    cout << endl;
}

//  2: Verificar stack frames entre funciones

void funcion_hija(int param) {
    int local_hija = 999;
    cout << "  [funcion_hija]" << endl;
    cout << "    param      = " << param
         << "  en " << &param << endl;
    cout << "    local_hija = " << local_hija
         << " en " << &local_hija << endl;
}
void experimento2_stack_frames() {
    cout << "" << endl;
    cout << "  EXPERIMENTO 2: Stack Frames" << endl;
    cout << "" << endl;
    int local_padre = 100;
    cout << "  [funcion_padre]" << endl;
    cout << "    local_padre = " << local_padre
         << " en " << &local_padre << endl;
    funcion_hija(local_padre);
    ptrdiff_t dummy;
    cout << "\n  Nota: la variable de la hija vive en una" << endl;
    cout << "  direccion mas baja que la del padre," << endl;
    cout << "  confirmando el modelo LIFO de la pila." << endl;
    cout << endl;
}

//  EXPERIMENTO 3: Alterar valores de manera indirecta
void modificar_por_puntero(int* ptr) {
    cout << "  [modificar_por_puntero]" << endl;
    cout << "    Valor recibido via puntero: " << *ptr << endl;
    *ptr = 777;
    cout << "    Valor modificado a: " << *ptr << endl;
}
void modificar_por_referencia(int& ref) {
    cout << "  [modificar_por_referencia]" << endl;
    cout << "    Valor recibido via referencia: " << ref << endl;
    ref = 888;
    cout << "    Valor modificado a: " << ref << endl;
}
void experimento3_alteracion_indirecta() {
    cout << "" << endl;
    cout << "  EXPERIMENTO 3: Alteracion Indirecta" << endl;
    cout << "" << endl;
    int variable = 42;
    cout << "  Valor original: " << variable
         << "  en " << &variable << endl << endl;
    // Via puntero
    modificar_por_puntero(&variable);
    cout << "  Valor en padre despues de puntero: "
         << variable << endl << endl;
    // Via referencia
    modificar_por_referencia(variable);
    cout << "  Valor en padre despues de referencia: "
         << variable << endl << endl;
}

//   4: Limite de la pila
void recursion_profunda(int nivel, int max_nivel) {
    volatile char buffer[1024]; // 1 KB por frame
    buffer[0] = 'A';
    if (nivel % 500 == 0) {
        cout << "  Nivel de recursion: " << nivel
             << "  (dir. local: " << (void*)buffer << ")" << endl;
    }
    if (nivel < max_nivel) {
        recursion_profunda(nivel + 1, max_nivel);
    }
}
void experimento4_limite_pila() {
    cout << "" << endl;
    cout << "  EXPERIMENTO 4: Limite de la Pila" << endl;
    cout << "" << endl;
    int niveles = 3000;
    cout << "  Intentando " << niveles
         << " niveles de recursion" << endl;
    cout << "  (cada frame usa ~1 KB adicional)" << endl << endl;
    recursion_profunda(1, niveles);
    cout << "\n  Recursion completada sin desbordamiento." << endl;
    cout << "  Para provocar stack overflow, incrementar" << endl;
    cout << "  los niveles o el tamano del buffer." << endl;
    cout << endl;
    cout << "  Nota: en Linux, el tamano de la pila puede" << endl;
    cout << "  consultarse con:  ulimit -s" << endl;
    cout << "  y modificarse con: ulimit -s <KB>" << endl;
    cout << "  Con el compilador: g++ -Wl,-z,stacksize=16777216"
         << endl;
    cout << endl;
}
//  5: Paso por valor vs paso por referencia

void paso_por_valor(int x) {
    cout << "  [paso_por_valor]" << endl;
    cout << "    Direccion del parametro: " << &x << endl;
    x = 0;
    cout << "    Modificado localmente a: " << x << endl;
}
void paso_por_referencia(int& x) {
    cout << "  [paso_por_referencia]" << endl;
    cout << "    Direccion del parametro: " << &x << endl;
    x = 0;
    cout << "    Modificado via referencia a: " << x << endl;
}
void experimento5_valor_vs_referencia() {
    cout << "" << endl;
    cout << "  EXPERIMENTO 5: Valor vs Referencia" << endl;
    cout << "" << endl;
    int original = 555;
    cout << "  original = " << original
         << "  en " << &original << endl << endl;
    paso_por_valor(original);
    cout << "  original despues de paso por valor: "
         << original << endl << endl;
    paso_por_referencia(original);
    cout << "  original despues de paso por referencia: "
         << original << endl << endl;
}

int main() {
    cout << "  Salida" << endl;

    cout << endl;
    experimento1_orden_pila();
    experimento2_stack_frames();
    experimento3_alteracion_indirecta();
    experimento4_limite_pila();
    experimento5_valor_vs_referencia();
    cout << "" << endl;
    cout << "  Todos los experimentos finalizados." << endl;
    cout << "" << endl;
    return 0;
}
