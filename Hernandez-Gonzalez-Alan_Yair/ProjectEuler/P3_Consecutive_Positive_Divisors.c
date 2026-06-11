#include <stdio.h>
#include <string.h>

#define N 10000001

int divisors[N];

int main() {
    memset(divisors, 0, sizeof(divisors));
    
    for (int i = 1; i < N; i++) {
        //Se utiliza el mismo principio de la a Criba de Totient generando todos sus multiplos del número
        for (int j = i; j < N; j += i) {
            //a cada multiplo se le suma uno, ya que es divisor
            divisors[j]++;
        }
    }
    

    //se itera el arreglo para ver cuantos comparten la misma cantidad de divisores
    int count = 0;
    for (int n = 2; n < N - 1; n++) {
        if (divisors[n] == divisors[n + 1]) {
            count++;
        }
    }
    
    printf("%d\n", count);
    return 0;
}