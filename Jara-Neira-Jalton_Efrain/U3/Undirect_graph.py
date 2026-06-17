# Author: Jalton Efrain Jara Neira
# Date: 30/03/2026 
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

    visited = [False] * (V+1)
    components = []

    def dfs(u, node):
        visited[u] = True
        node.append(u)
        for neighbor in sorted(adj[u]):
            if not visited[neighbor]:
                dfs(neighbor, node)

    for i in range(1, V+1):
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(sorted(component))


    print(len(components))
    for comp in components:
        print(*(comp))

if __name__ == "__main__":
    main_program()
