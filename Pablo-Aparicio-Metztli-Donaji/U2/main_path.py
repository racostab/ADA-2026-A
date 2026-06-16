# Given a maze in the form of a rectangular matrix, find a path from a given source to a given destination. The path can only be constructed out of 
# cells that represents a wall and without going out of bounds; at any moment, we can only move one step in one of the four directions: Up, Right, Down, and Left, 
# in other words, using a four neighbor topology and counterclockwise.

# The main variations of this problem are: 1) using eight neighbor topology (adding diagonal movements), and 2) find the sorthest path.

# Input
# The input contains only one test case as described below. The first line contains seven integers, R and C (1 <= R, C <= 1000) specifying the number of 
# rows and columns, Sr, Sc, Tr, and Tc that represents the coordinates of Source cell (Sr, Sc) and Target cell (Tr, Tc). These coordinates are top left corner 
# and 0-indexed. And finally, a number O that describes the type of output.

# This is followed by the maze as a rectangular matrix M composed by R lines each one with C characters. Each character represents a cell that can either be ‘ ‘ 
# (the space that represents a corridor) or ‘#’ (the hashtag that represents a wall).

# Output
# The meaning of the number O is:

# 1: “True” if exist a path or “False” other case.
# 2: The length as an integer.
# 3: The path using the four letters that represent the directions taken: U, R, D and L.

# Sample Input
# 10 10 1 1 8 8 1
# ##########
# #     #  #
# # #   #  #
# # ### #  #
# #   # #  #
# #   #   ##
# # ###    #
# # #   #  #
# #     #  #
# ##########
# Sample Output
# True

# Using the same maze and if the O number is 2 the output is:
# 14

# If the O number is 3 the output is:
# RRRRDDDDRRDRDD

from collections import deque

maze = []
# arriba, abajo, izquierda, derecha
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
moves = ['R','D','L','U']
queue = deque()
parent = {}

def star_path(i,j):
    queue.append((i,j))

def save_path(i,j,dir):
    queue.append((i,j))
    return queue

def reconstruct_path(Sr,Sc,Tr,Tc):
    path = []
    cur = (Tr,Tc)

    while cur != (Sr,Sc):
        prev, move = parent[cur]
        path.append(move)
        cur = prev

    path.reverse()
    return path

def find_maze(r,c,Sr,Sc,Tr,Tc):

    while queue:
        i,j = queue.popleft()

        for k in range(4):

            ni = i + dirs[k][0]
            nj = j + dirs[k][1]

            if 0 <= ni < r and 0 <= nj < c and (maze[ni][nj] == ' ' or (ni,nj) == (Tr,Tc)):

                maze[ni][nj] = '.'
                queue.append((ni,nj))
                parent[(ni,nj)] = ((i,j), moves[k])

                if (ni,nj) == (Tr,Tc):
                    return reconstruct_path(Sr,Sc,Tr,Tc)

    return []

def evaluate_o(parent, o):
    if o == 1:
        return "True" if parent else "False"
    if o == 2:
        return len(parent)  # Placeholder for path length
    if o == 3:
        return ''.join(parent)  # Placeholder for path directions

def main():
    r, c, Sr, Sc, Tr, Tc, o = map(int, input().split())
    
    # read the maze
    for _ in range(r):
        maze.append(list(input()))
            
    # coordenada de inicio
    star_path(Sr,Sc)
    
    # encontrar el camino
    path = find_maze(r,c,Sr,Sc,Tr,Tc)

    #evaluar el tipo de salida
    output = evaluate_o(path, o)
    print(output)

    # print the maze with the path marked
    # for row in maze:
    #     print(''.join(row))

if __name__ == "__main__":
    main()