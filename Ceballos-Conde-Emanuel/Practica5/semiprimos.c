#include <stdio.h>
#include <stdlib.h>

int main() {
    long long limite = 100000000LL;
    long long p_limite = limite / 2;

    unsigned char *no_es_primo = (unsigned char *)calloc(p_limite + 1, sizeof(unsigned char));
    
    for (long long p = 2; p * p <= p_limite; p++) {
        if (!no_es_primo[p]) {
            for (long long i = p * p; i <= p_limite; i += p)
                no_es_primo[i] = 1;
        }
    }

    long long *primos = (long long *)malloc((p_limite / 2) * sizeof(long long)); 
    long long num_primos = 0;
    for (long long p = 2; p <= p_limite; p++) {
        if (!no_es_primo[p]) {
            primos[num_primos++] = p;
        }
    }
    free(no_es_primo);

    long long num_semiprimos = 0;
    long long der = num_primos - 1;

    for (long long izq = 0; izq < num_primos; izq++) {
        long long p = primos[izq];
        if (p * p >= limite) break;
        while (der >= izq && p * primos[der] >= limite) {
            der--;
        }
        if (der >= izq) {
            num_semiprimos += (der - izq + 1);
        }
    }

    printf("%lld\n", num_semiprimos);

    free(primos);
    return 0;
}