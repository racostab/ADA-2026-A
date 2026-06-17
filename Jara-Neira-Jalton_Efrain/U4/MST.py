# Author: Jalton Jara Neira
# Date: 28/05/2026 
import sys
import heapq 

sys.setrecursionlimit(5000)

def find_component(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find_component(parent, parent[i]) 
    return parent[i]

def merge_components(parent, rank, u, v):
    root_u = find_component(parent, u)
    root_v = find_component(parent, v)
    
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal(heap, parent, rank, edges_count, target_edges):

    #Condición de parada T tenga menos de n-1 aristas
    if edges_count == target_edges or not heap:
        return 0
    
    weight, u, v = heapq.heappop(heap)
    
    #Si C(v) != C(u) devuelve la componente a la que pertenece u
    if find_component(parent, u) != find_component(parent, v):
        merge_components(parent, rank, u, v)
        
        return weight + kruskal(heap, parent, rank, edges_count + 1, target_edges)
    else:
        return kruskal(heap, parent, rank, edges_count, target_edges)

def program_main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    
    try:
        V = int(next(it))
        E = int(next(it))
        st_type = next(it) #'min' o 'max'
        heap = []
        
        for _ in range(E):
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            
            #Para el Max Spanning Tree, invertir los pesos en min-heap
            if st_type == "min":
                heapq.heappush(heap, (w, u, v))
            else:
                heapq.heappush(heap, (-w, u, v)) 
        
        parent = [i for i in range(V+1)]
        rank = [0] * (V+1)
        
        target_edges = V-1
        total_weight = kruskal(heap, parent, rank, 0, target_edges)
        
        if st_type == "max":
            total_weight = -total_weight
            
        print(total_weight)
        
    except StopIteration:
        return

if __name__ == "__main__":
    program_main()