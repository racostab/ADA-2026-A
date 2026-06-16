from collections import deque
import sys

def solve():
    R,C,Sr,Sc,Tr,Tc,O=map(int,sys.stdin.readline().split()) #Lee la linea completa 
    maze = [sys.stdin.readline().rstrip("\n") for _ in range(R)] #lee matriz por filas

    #Como solo se puede caminar por " " y no por #
    def is_valid(r,c):
        return 0 <= r < R and 0 <= c < C and maze[r][c] == ' '
    if not is_valid(Sr,Sc) or not is_valid(Tr,Tc):
        if O == 1:
            print("False")
        elif O == 2:
            print(-1)
        else:
            print("")
        return
    dirs =[(-1,0,"U"),(0,1,"R"),(1,0,"D"),(0,-1,"L")]

    q = deque()
    q.append((Sr,Sc,)) #pos inicial
    visited = [[False]* C for _ in range (R)]
    visited[Sr][Sc] = True

    dist=[[-1] * C for _ in range (R)]
    dist[Sr][Sc] = 0
    parent = [[None] * C for _ in range (R)]

    found = False
    while q:
        r,c = q.popleft()

        if (r,c) == (Tr,Tc):
            found = True
            break

        for dr,dc,move in dirs:
            nr,nc = r+dr, c+dc

            if is_valid(nr,nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                dist[nr][nc] = dist[r][c] + 1
                parent[nr][nc] = (r,c,move)
                q.append((nr,nc))
    if O == 1:
        print("True" if found else "False")
    elif O == 2:
        print(dist[Tr][Tc] if found else -1)
    else:
        if not found:
            print("")
        else:
            path = []
            r,c = Tr,Tc 

            while (r,c) != (Sr,Sc):
                pr,pc,move = parent[r][c]
                path.append(move)
                r,c = pr,pc
            path.reverse()
            print("".join(path))

if __name__ == "__main__":
    solve()
    