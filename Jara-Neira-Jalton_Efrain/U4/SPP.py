# Author: Jalton Jara Neira
# Date: 28/05/2026 
import sys
import heapq

def program_main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    while True:
        try:
            N = int(next(it))  #N° vértices
            M = int(next(it))  #N° aristas
            T = int(next(it))  
            
            graph = [[] for i in range(N+1)]
            for i in range(M):
                try:
                    u = int(next(it))
                    v = int(next(it))
                    w = int(next(it))
                    if 1 <= u <= N and 1 <= v <= N:
                        graph[u].append((v, w))
                        graph[v].append((u, w))
                except StopIteration:
                    break
                
            INF = 10**9
            dist = [INF] * (N+1)
            parent = [-1] * (N+1)
            
            source = 1
            dist[source] = 0
            
            priority_queue = [(0, source)]
            
            #Dijkstra
            while priority_queue:
                current_dist, u = heapq.heappop(priority_queue)
                
                if current_dist > dist[u]:
                    continue
                    
                for neighbor, weight in graph[u]:
                    distance_via_u = current_dist + weight
                    
                    if distance_via_u < dist[neighbor]:
                        dist[neighbor] = distance_via_u
                        parent[neighbor] = u
                        heapq.heappush(priority_queue, (distance_via_u, neighbor))
                        
            output_distances = []
            for j in range(2, N+1):
                output_distances.append(str(dist[j]))
            print(" ".join(output_distances))
            
            path = []
            if dist[T] != INF:
                current = T
                while current != -1:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                
            print(" ".join(map(str, path)))
            
        except StopIteration:
            break

if __name__ == "__main__":
    program_main()