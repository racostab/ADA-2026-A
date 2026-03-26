"""Maze P2"""
from collections import deque
class Maze:
    """OO Maze solution"""
    def __init__(self, maze, out):
        self.maze = maze
        self.out = out
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.path = deque()
    def walk(self, curr, dest):
        """Walk acrros the maze"""
        if curr == dest:
            return True
        y, x = curr
        self.maze[y][x] = "*"#visited
        #order for moves
        for ny, nx, step in [(y, x+1, "R"), (y+1, x, "D"), (y, x-1, "L"), (y-1, x, "U")]:
            if 0 <= ny < self.rows and 0 <= nx < self.cols:
                if self.maze[ny][nx] not in ("#", "*"):
                    if self.walk((ny, nx), dest):
                        self.path.append(step)
                        return True
        return False
    def solve(self, start, end):
        """find the path and print result"""
        found = self.walk(start, end)
        res = "".join(list(self.path)[::-1])
        if self.out == 1:
            #T-way F-no way
            print("True" if found or start == end else "False")
        elif self.out == 2:
            print(len(res))
        else:
            print(res)

if __name__ == '__main__':
    d = input().split()
    p = list(map(int, d))
    m = [list(input()) for _ in range(p[0])]
    solver = Maze(m, p[6])
    solver.solve((p[2], p[3]), (p[4], p[5]))
