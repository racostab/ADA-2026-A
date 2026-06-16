from collections import defaultdict, deque

ve = input().split()
v = int(ve[0])
e = int(ve[1])

graph = defaultdict(list)


for _ in range(e):
    uv = input().split()
    u, v = int(uv[0]), int(uv[1])
    graph[u].append(v)
    graph[v].append(u)    

color = {} #0=U, 1=V

def validate_bipartite():

    queue = deque([1])
    color[1] = 0

    is_bipartite = True

    while queue and is_bipartite:
        u = queue.popleft()
        #recirremos sus nodos adjacentes
        for v in graph[u]:
            if v not in color:
                #asignamos color opuesto
                color[v] = 1 - color[u]
                #se agrega vecino a la queue
                queue.append(v)
            elif color[v] == color[u]:
                is_bipartite = False
                break

    if not is_bipartite:
        print("EMPTY")
        return

    U = sorted([v for v in color if color[v] == 0])
    V_set = sorted([v for v in color if color[v] == 1])

    print(" ".join(str(v) for v in U))
    print(" ".join(str(v) for v in V_set))

validate_bipartite()