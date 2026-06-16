import math

prime_list = [2]
n = 10001
limite_superior = int(n*(math.log(n)+math.log(math.log(n))))

def es_primo(x):
    
    for p in prime_list:
        if x%p == 0:
            primo = False
            break
        else:
            primo = True

    return primo

for i in range(2,limite_superior):
    if es_primo(i):
        prime_list.append(i)

print(prime_list[n-1])