def selection_sort(list):  
    for i in range(len(list)): 
        min = i # Inicializamos el mínimo con el índice actual.
        
        # Buscamos en la lista restante (después del elemento que ya está ordenado) un nuevo máximo y lo guardamos a 'min'.  
        for j in range(i+1, len(list)): 
            if list[j] < list[min]: # Si el valor actual es menor al mínimo.   
                min = j;              # Actualización del índice de máximo y guardado en 'min'.  
        
        # Intercambiamos la posición encontrada con el primero (ordenando) para mantener ordenamiento ascendente: 
        list[i],list[min] = list[min],list[i]   
    
# Prueba del método.     
numbers_to_sort= [64,34,25,12,22,11,90]   # Aquí puedes poner tus números a ordenar aquí 
selection_sort(numbers_to_sort)   
print ("Ordenado en ascendente:", numbers_to_sort )