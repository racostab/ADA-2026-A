import sys
sys.setrecursionlimit(10**6)

def dfs(u, parent):
    global time
    visited[u] = True
    disc[u] = low[u] = time
    time += 1

    children = 0

    for v in adj[u]:
        if not visited[v]:
            children += 1
            dfs(v, u)

            low[u] = min(low[u], low[v])

            # Caso 1: u no es raíz
            if parent != -1 and low[v] >= disc[u]:
                articulation[u] = True

        elif v != parent:
            low[u] = min(low[u], disc[v])

    # Caso 2: u es raíz
    if parent == -1 and children > 1:
        articulation[u] = True


# Entrada
V, E = map(int, input().split())

adj = {i: [] for i in range(1, V+1)}

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (V + 1)
disc = [0] * (V + 1)
low = [0] * (V + 1)
articulation = [False] * (V + 1)

time = 0

# Puede ser grafo desconectado
for i in range(1, V+1):
    if not visited[i]:
        dfs(i, -1)

# Resultado
result = [i for i in range(1, V+1) if articulation[i]]

print(*sorted(result))