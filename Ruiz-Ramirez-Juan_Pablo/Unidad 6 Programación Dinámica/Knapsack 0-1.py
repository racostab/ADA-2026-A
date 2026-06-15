def mochila(W, pesos, valores):
    n = len(valores)
    
    # Crear tabla DP
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    seleccion = [[False] * (W + 1) for _ in range(n + 1)]
    
    # Llenar tabla DP
    for i in range(1, n + 1):
        for j in range(W + 1):
            if pesos[i-1] > j:
                dp[i][j] = dp[i-1][j]
                seleccion[i][j] = False
            else:
                incluir = dp[i-1][j - pesos[i-1]] + valores[i-1]
                excluir = dp[i-1][j]
                
                if incluir > excluir:
                    dp[i][j] = incluir
                    seleccion[i][j] = True
                else:
                    dp[i][j] = excluir
                    seleccion[i][j] = False
    
    objetos = []
    j = W
    for i in range(n, 0, -1):
        if seleccion[i][j]:
            objetos.append(i) 
            j -= pesos[i-1]
    
    objetos.sort()  # Orden ascendente
    return dp[n][W], objetos


datos = list(map(int, input().split()))
n = datos[0]
W = datos[1]
valores = [0] * n
pesos = [0] * n

for k in range(n):
    datos = list(map(int, input().split()))
    valores[k] = datos[0]
    pesos[k] = datos[1]

valor, objetos = mochila(W, pesos, valores)

# Resultados
print(valor)
if objetos:
    print(' '.join(map(str, objetos)))
