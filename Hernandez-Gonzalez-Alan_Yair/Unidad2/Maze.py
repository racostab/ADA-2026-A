from collections import deque

maze_config = [int(x) for x in input().split()]

NEIGHBORS_NUMBER = 4
maze_row_size = maze_config[0]  # R = número de filas
maze_col_size = maze_config[1]  # C = número de columnas
maze_source = (maze_config[2], maze_config[3])
maze_target= (maze_config[4], maze_config[5])
maze_result_type = maze_config[6]
maze = []

for _ in range(maze_row_size):
    line = input()
    maze.append(list(line))

def get_neighbors(maze, node):
    row = node[0]
    col = node[1]
    
    row_size = len(maze[0])
    col_size = len(maze)
    
    neighbors = []
    adjacent_cells = []

    adjacent_cells.append((row-1, col, 'U')) #Up
    adjacent_cells.append((row, col+1, 'R')) #Right
    adjacent_cells.append((row+1, col, 'D')) #Down
    adjacent_cells.append((row, col-1, 'L')) #Left

    if NEIGHBORS_NUMBER == 8:
        adjacent_cells.append((row - 1, col - 1, 'UL'))
        adjacent_cells.append((row - 1, col + 1, 'UR'))
        adjacent_cells.append((row + 1, col - 1, 'DL'))
        adjacent_cells.append((row + 1, col + 1, 'DR'))

    neighbors = []
    for cell in adjacent_cells:
        r, c, direction = cell
        if 0 <= r < row_size and 0 <= c < col_size and maze[r][c] != '#':
            neighbors.append(cell)    
    return neighbors


def solve_maze(maze, source, target):
    visited = set([source])
    queue = deque([(source, '')])    

    while queue:
        current, path = queue.popleft()
        if current == target:
            return path
        
        for neighbor in get_neighbors(maze, current):
            nx, ny, dir = neighbor
            next_neighbor = (nx, ny)
            if next_neighbor not in visited:
                visited.add(next_neighbor)
                queue.append((next_neighbor, path + dir))
    return None

result = solve_maze(maze, maze_source, maze_target)

match maze_result_type:
    case 1:
        print(result is not None)
    case 2:
        print(len(result) if result is not None else 0)
    case 3:
        print(result if result is not None else '')
    case _:
        print('Error')
