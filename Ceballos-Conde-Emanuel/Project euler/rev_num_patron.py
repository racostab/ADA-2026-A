#existe un patron en la cantidad de numeros reversibles de acuerdo a el numero de digitos que hay in dicho numero
def rev_num(max_digits):

    rev_num_counter = 0

    for k in range(1, max_digits + 1):
        if k % 2 == 0:
            
            count = 20 * (30 ** (k // 2 - 1))
            rev_num_counter += count

        elif k % 4 == 3:
            count = 100 * (500 ** ((k - 3) // 4))
            rev_num_counter += count
            
    #si el resiudo es 1 entonces no hay numeros revesibles       
    return rev_num_counter

print(rev_num(9))