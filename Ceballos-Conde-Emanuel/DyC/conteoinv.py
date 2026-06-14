user_input = input()
numero_tcs = int(user_input)

test_cases = []
for _ in range(numero_tcs):
    user_input = input()
    tc = list(map(int, user_input.split()))
    test_cases.append(tc)


def merge_count(lista_A, lista_B):
    i = 0
    j = 0
    inv_cont = 0
    lista_ordenada = []
     
    while i < len(lista_A) and j < len(lista_B):
        if lista_A[i] <= lista_B[j]:
            lista_ordenada.append(lista_A[i])
            i += 1
        else:
            lista_ordenada.append(lista_B[j])
            j += 1
            inv_cont += len(lista_A) - i

    while i < len(lista_A):
        lista_ordenada.append(lista_A[i])
        i += 1

    while j < len(lista_B):
        lista_ordenada.append(lista_B[j])
        j += 1

    return inv_cont, lista_ordenada


def sort_count(lista):
    if len(lista) <= 1:
        return 0, lista

    mitad = len(lista) // 2
    inv_A, A = sort_count(lista[:mitad])
    inv_B, B = sort_count(lista[mitad:])
    inv_AB, lista_ordenada = merge_count(A, B)

    return inv_A + inv_B + inv_AB, lista_ordenada


for tc in test_cases:
    num_inv, lista = sort_count(tc)
    print(num_inv)