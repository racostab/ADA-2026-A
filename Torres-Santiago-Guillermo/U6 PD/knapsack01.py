def mochila(W,pesos, valores):
    t_val = [0]*(W+1)
    
    obj = [[] for _ in range(W+ 1)]

    for i in range(1,len(pesos) +1):
        peso_actual = pesos[i-1]
        valor_actual = valores[i-1]
        
        for j in range(W, peso_actual-1, -1):
            
            if t_val[j-peso_actual] + valor_actual > t_val[j]:
                t_val[j] = t_val[j-peso_actual] + valor_actual
                obj[j] = obj[j-peso_actual] + [i] 

    return t_val[W], sorted(obj[W])   

datos = list(map(int,input().split()))
n = datos[0]
W = datos[1]
valores = [0]*n
pesos = [0]*n

for k in range(n):
    datos =list(map(int,input().split()))
    valores[k] = datos[0]
    pesos[k] = datos[1]

valor, objetos = mochila(W, pesos, valores)

print(valor)
n_o = len(objetos)
for l in range(n_o):
    if l == n_o-1:
        print(f"{objetos[l]}")
    else:
        print(f"{objetos[l]}", end=" ")
