def resolver():
    while True:
        try:
            linea = input().strip()
            if not linea:
                continue
            
            n, W = map(int, linea.split())
            
            valores = []
            pesos = []
            
            for _ in range(n):
                v, w = map(int, input().split())
                valores.append(v)
                pesos.append(w)
            
            # DP
            dp = [[0] * (W + 1) for _ in range(n + 1)]
            
            for i in range(1, n + 1):
                for w in range(W + 1):
                    if pesos[i - 1] <= w:
                        dp[i][w] = max(
                            dp[i - 1][w],
                            dp[i - 1][w - pesos[i - 1]] + valores[i - 1]
                        )
                    else:
                        dp[i][w] = dp[i - 1][w]
            
            print(dp[n][W])
            w = W
            seleccionados = []
            
            for i in range(n, 0, -1):
                if dp[i][w] != dp[i - 1][w]:
                    seleccionados.append(i)
                    w -= pesos[i - 1]
            
            seleccionados.sort()
            print(" ".join(map(str, seleccionados)))
        
        except EOFError:
            break


resolver()