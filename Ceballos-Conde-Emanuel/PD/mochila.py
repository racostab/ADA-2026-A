import sys

def mochila():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    idx = 0
    n = len(entrada)

    while idx < n:
        try:
            num_articulos = int(entrada[idx])
            capacidad = int(entrada[idx + 1])
            idx += 2
            
            articulos = []
            for _ in range(num_articulos):
                valor = int(entrada[idx])
                peso = int(entrada[idx + 1])
                articulos.append((valor, peso))
                idx += 2
                
            dp = [[0] * (capacidad + 1) for _ in range(num_articulos + 1)]
            
            for i in range(1, num_articulos + 1):
                valor, peso = articulos[i - 1]
                for w in range(capacidad + 1):
                    if peso <= w:
                        dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso] + valor)
                    else:
                        dp[i][w] = dp[i - 1][w]
                        
            ganancia_maxima = dp[num_articulos][capacidad]
            
            w_actual = capacidad
            indices_seleccionados = []
            
            for i in range(num_articulos, 0, -1):
                if dp[i][w_actual] != dp[i - 1][w_actual]:
                    indices_seleccionados.append(i)
                    w_actual -= articulos[i - 1][1]
                    
            indices_seleccionados.sort()
            
            print(ganancia_maxima)
            if indices_seleccionados:
                print(" ".join(map(str, indices_seleccionados)))
            else:
                print()
                
        except IndexError:
            break

if __name__ == '__main__':
    mochila()