#-------------------------- unir partes del arreglo ----------------------------
def ord_comp(arr,temp_arr,left,mid,right):

    i = left
    j = mid+1
    k = left
    inver = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inver += (mid-i+1)
            j += 1
        k += 1

    while i <= mid: #Copiar el resto de la izquierda
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right: #Copiar el resto de la derecha
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for k1 in range(left,right+1):  # devolver todo ordenado
        arr[k1] = temp_arr[k1]

    return inver

#------------------------------ Dividir el arreglo -----------------------------
def ord_cont(arr,temp_arr,left,right):
    inver = 0

    if left < right:
        mid = (left+right)//2

        inver += ord_cont(arr,temp_arr,left,mid)        #Dividir arreglo
        inver += ord_cont(arr,temp_arr,mid+1,right)     
        
        inver += ord_comp(arr,temp_arr,left,mid,right)# Ordenar y unir

    return inver

#--------------------------------------- MAIN ----------------------------------
tc = int(input())
datos = [0]*tc
for i in range(tc):
    datos[i] = input().split()
    
for i in range(tc):
    arr = list(map(int,datos[i]))
    n = len(arr)
    temp_arr = [0]*n
    
    total_inv = ord_cont(arr,temp_arr,0,n-1)
    
    print(total_inv)
