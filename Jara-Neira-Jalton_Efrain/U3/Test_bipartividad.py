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
    for _ in range(E):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    rojo = "rojo"
    azul = "azul"
    color = [None] * (V+1)
    
    for i_node in range(1, V+1):
        if color[i_node] is None:
            queue = [i_node]
            color[i_node] = rojo 
            while queue:
                u = queue.pop(0)
                color_opuesto = azul if color[u] == rojo else rojo
                for neighbor in adj[u]:
                    if color[neighbor] is None:
                        color[neighbor] = color_opuesto
                        queue.append(neighbor)
                    elif color[neighbor] == color[u]:
                        print("EMPTY")
                        return

    set_u = [i for i in range(1, V+1) if color[i] == rojo]
    set_v = [i for i in range(1, V+1) if color[i] == azul]
    set_u.sort()
    set_v.sort()

    if set_v and (not set_u or set_v[0] < set_u[0]):
        print(*(set_v))
        print(*(set_u))
    else:
        print(*(set_u))
        print(*(set_v))

if __name__ == "__main__":
    main_program()