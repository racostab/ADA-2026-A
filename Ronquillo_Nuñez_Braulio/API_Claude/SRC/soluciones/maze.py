from collections import deque

def solve_maze():
    # Read input
    first_line = input().split()
    R, C, Sr, Sc, Tr, Tc, O = map(int, first_line)
    
    maze = []
    for _ in range(R):
        maze.append(input())
    
    # BFS to find path
    queue = deque([(Sr, Sc, "")])
    visited = set()
    visited.add((Sr, Sc))
    
    # Directions: U, R, D, L (in order for tie-breaking)
    directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]
    
    found = False
    path = ""
    
    while queue:
        r, c, current_path = queue.popleft()
        
        # Check if we reached the target
        if r == Tr and c == Tc:
            found = True
            path = current_path
            break
        
        # Explore neighbors in order: U, R, D, L
        for dr, dc, move in directions:
            nr, nc = r + dr, c + dc
            
            # Check bounds and valid position
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and maze[nr][nc] == ' ':
                visited.add((nr, nc))
                queue.append((nr, nc, current_path + move))
    
    # Output based on O
    if O == 1:
        print(found)
    elif O == 2:
        if found:
            print(len(path))
        else:
            print(-1)  # No path exists
    elif O == 3:
        if found:
            print(path)
        else:
            print("")  # No path exists

solve_maze()
