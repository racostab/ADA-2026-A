/*
    Implementacion del algoritmo de Heap
    Permutaciones    

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    10/Marzo/2026 

*/
#include <stdio.h>
#include <string.h>

void ordenar(char *sub_ar[], int inicio, int n)// Ordenar Sub arreglo
{
    for(int i = inicio; i < n-1; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(strcmp(sub_ar[i], sub_ar[j]) > 0)
            {
                char *t = sub_ar[i];
                sub_ar[i] = sub_ar[j];
                sub_ar[j] = t;
            }
        }
    }
}

void permutaciones(char *conj_o[], int n, int r, int p)
{
    char *buffer_a;
    char *conj[100];

    for(int k5 = 0; k5 < n; k5++)
        conj[k5] = conj_o[k5];

    if(p == r)
    {
        for(int k2 = 0; k2 < r; k2++)
        {
            if(k2 == r-1)
                printf("%s", conj[k2]);
            else
                printf("%s ", conj[k2]);
        }
        printf("\n");
        return;
    }
    
    for(int k3 = p; k3 < n; k3++)
    {       
        buffer_a = conj[p];
        conj[p] = conj[k3];
        conj[k3] = buffer_a;

        ordenar(conj, p+1, n);
        
        permutaciones(conj, n, r, p + 1);
        
        buffer_a = conj[p];
        conj[p] = conj[k3];
        conj[k3] = buffer_a;
    }
}

int main(void)
{
    int k1 = 0;
    int n_ele, r_ele;

    char linea[1000];
    char *conj[100];

    scanf("%d %d", &n_ele, &r_ele);
    getchar();   // Limpiar el buffer de entrada

    fgets(linea, sizeof(linea), stdin);

    linea[strcspn(linea, "\n")] = 0;

    char *token = strtok(linea, " ");

    while(token != NULL && k1 < n_ele)
    {
        conj[k1] = token;
        k1++;
        token = strtok(NULL, " ");
    }

    permutaciones(conj, n_ele, r_ele, 0);

    return 0;
}
