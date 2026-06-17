# Author: Jalton Efrain Jara Neira
# Date: 01/04/2026 
import sys
def main_program():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    V, E = int(input_data[0]), int(input_data[1])
    adj = [[] for _ in range(V + 1)]
    idx_ptr = 2
    for _ in range(E):
        u = int(input_data[idx_ptr])
        v = int(input_data[idx_ptr+1])
        adj[u].append(v)
        idx_ptr += 2

    indices = [-1] * (V+1)
    lowlink = [-1] * (V+1)
    on_stack = [False] * (V+1)
    stack = []
    timer = 0
    all_sccs = []

    def strongconnect(v):
        nonlocal timer
        indices[v] = lowlink[v] = timer
        timer += 1
        stack.append(v)
        on_stack[v] = True

        for w in adj[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            current_scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                current_scc.append(w)
                if w == v: 
                    break
            all_sccs.append(sorted(current_scc))

    for i in range(1, V+1):
        if indices[i] == -1:
            strongconnect(i)

    print(len(all_sccs))
    all_sccs.sort(key=lambda x: x[0])
    for scc in all_sccs:
        print(*(scc))

if __name__ == "__main__":
    main_program()