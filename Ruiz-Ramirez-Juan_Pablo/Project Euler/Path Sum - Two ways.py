with open(r"C:\Users\PLANETMEDIA\Documents\Python\matriz.txt", "r") as archivo:
    matriz = []
    for linea in archivo:
        matriz.append([int(x) for x in linea.strip().split(",")])
    print(matriz)
print("#####")

mejor = float("inf")

#Blactrackin + poda 
def backtracking(i,j,suma,camino):
   global mejor
   n = len(matriz)
   m = len(matriz[0])
   if i >= n or j >= m:
       return
   suma += matriz[i][j]
   
   camino = camino + [(i, j)]
   print(f"Visitando {i},{j} valor={matriz[i][j]} suma={suma} camino={camino}")

   if suma >= mejor:
       print("  ❌ Podado (suma mayor que mejor)")
       return
   
   if i == n-1 and j == m-1:
       mejor = suma
       print(f"  ✅ Llegué al final. Nueva mejor = {mejor}")
       return
   backtracking(i+1,j,suma,camino)
   backtracking(i,j+1,suma,camino)

backtracking(0,0,0,[])
print(mejor)

print("############################################")
#Blactrackin + poda + Memoizacion
memo = {}
mejorMEMO = float("inf")

def backtrackingMEMO(i, j, suma, camino):
    global mejorMEMO
    n = len(matriz)
    m = len(matriz[0])

    if i >= n or j >= m:
        return

    suma += matriz[i][j]
    camino = camino + [(i, j)]

    print(f"Visitando {i},{j} valor={matriz[i][j]} suma={suma} camino={camino}")

    # 🔹 poda global
    if suma >= mejorMEMO:
        print("  ❌ Podado (suma >= mejor global)")
        return

    # 🔹 poda por memoización
    if (i, j) in memo and suma >= memo[(i, j)]:
        print(f"  ❌ Podado por memo en {(i,j)} (ya había mejor suma: {memo[(i,j)]})")
        return

    # 🔹 guardamos mejor suma para esta celda
    memo[(i, j)] = suma
    print(f"  💾 Guardando memo[{(i,j)}] = {suma}")

    # caso final
    if i == n-1 and j == m-1:
        mejorMEMO = suma
        print(f"  ✅ Llegué al final. Nueva mejor = {mejorMEMO}")
        return

    backtrackingMEMO(i+1, j, suma, camino)
    backtrackingMEMO(i, j+1, suma, camino)


backtrackingMEMO(0, 0, 0, [])
print("Mejor resultado:", mejorMEMO)

#Programación Dinamica
n = len(matriz)
m = len(matriz[0])
dp = [[0] * m for _ in range(n)]

dp[0][0] = matriz[0][0]# esquina
# primera fila
for j in range(1, m):
   dp[0][j] = dp[0][j-1] + matriz[0][j]
# primera columna
for i in range(1, n):
   dp[i][0] = dp[i-1][0] + matriz[i][0]
# resto de la matriz
for i in range(1, n):
   for j in range(1, m):
      dp[i][j] = matriz[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
for fila in dp:
    print(fila)