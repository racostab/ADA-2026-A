user_input= input()
combination_values = user_input.split(" ")
user_input = input()
valores = user_input.split(" ")

len_combinacion = int(combination_values[1])

def combinaciones(lista, n):
    if n == 0:
        return [[]]
    
    if len(lista) == 0:
        return []
    
    head = lista[0]
    tail = lista[1:]
    
    head_combination = []
    for combinacion in combinaciones(tail, n - 1):
        head_combination.append([head] + combinacion)
        
    headless_combination = combinaciones(tail, n)
    
    return head_combination + headless_combination


resultado = combinaciones(valores, len_combinacion)

for combi in resultado:
  print(" ".join(combi))