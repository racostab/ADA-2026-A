# Author: Jalton Efrain Jara Neira
# Date: 01/04/2026 
import sys

def main_program():
    input_data = sys.stdin.read().split()
    if not input_data: 
        return
    
    V = int(input_data[0])
    E = int(input_data[1])

    adj = [[] for i in range(V+1)]
    idx = 2
    for i in range(E):
        u = int(input_data[idx]) 
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    discovery = [-1] * (V+1)
    low = [-1] * (V+1)
    is_cut_point = [False] * (V+1)
    cont = 0

    def dfs(u, p=-1):
        nonlocal cont
        discovery[u] = low[u] = cont
        cont += 1
        child = 0
        
        for v in adj[u]:
            if v == p: continue 
            
            if discovery[v] != -1:
                low[u] = min(low[u], discovery[v])
            else:
                child += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                
                if p != -1 and low[v] >= discovery[u]:
                    is_cut_point[u] = True
        
        if p == -1 and child > 1:
            is_cut_point[u] = True

    for i in range(1, V + 1):
        if discovery[i] == -1:
            dfs(i)

    result = [i for i in range(1, V+1) if is_cut_point[i]]
    print(*(result))



if __name__ == "__main__":
    main_program()