def merge_sort(array):                                      #Función principal 
    conteo = 0              
    if len(array) <= 1:                                     #Caso base      
        return array, conteo
    mitad = len(array) // 2                                 #El arreglo se divide en 2 mitades
    ladoI, conteoI = merge_sort(array[:mitad])              #Ordenamiento recursivo lado izquierdo 
    ladoD, conteoD = merge_sort(array[mitad:])              #Ordenamiento recursivo lado derecho
    array_ordenado, conteo_merge = merge(ladoI, ladoD)      #Combinar y contar las inversiones
    conteo += conteoI + conteoD + conteo_merge              #Suma de inversiones encontradas 
    return array_ordenado, conteo

def merge(izquierda, derecha):                              #Función que combina listas ordenadas 
    resultado = []
    conteo = 0
    i = 0                                                   #indices 
    j = 0
    while i < len(izquierda) and j < len(derecha):          #Se comparan elementos de ambas listas  
        if izquierda[i] <= derecha[j]:                      #Comparar elementos y agregar al resultado
            resultado.append(izquierda[i])
            i += 1
        else:                                               #Caso contrario al if     
            resultado.append(derecha[j])
            conteo += len(izquierda) - i
            j += 1
    resultado.extend(izquierda[i:])                         #Agregar elementos restantes de la izquierda
    resultado.extend(derecha[j:])                           #Agregar elementos restantes de la derecha 
    return resultado, conteo

t = int(input())                                    

for _ in range(t):
    arr = list(map(int, input().split()))
    _, conteo = merge_sort(arr)     #Dame los valores que retorna la función ignora el 1ro "_" guarda el segundo "conteo"
    print(conteo)

#EJERCICIO APROBADO POR COUCH