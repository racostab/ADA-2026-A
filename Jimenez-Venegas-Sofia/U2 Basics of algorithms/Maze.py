from collections import deque

R, C, Sr, Sc, Tr, Tc, O = map(int, input().split())

maze = [list(input()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
parent = [[None]*C for _ in range(R)]

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
dir_char = ['U','R','D','L']

q = deque()
q.append((Sr,Sc))
visited[Sr][Sc] = True

found = False

while q:
    r,c = q.popleft()

    if (r,c) == (Tr,Tc):
        found = True
        break

    for i in range(4):
        nr = r + dirs[i][0]
        nc = c + dirs[i][1]

        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and maze[nr][nc] == ' ':
                visited[nr][nc] = True
                parent[nr][nc] = (r,c,i)
                q.append((nr,nc))

if not found:
    print("False")
else:
    path = []
    r,c = Tr,Tc

    while (r,c) != (Sr,Sc):
        pr,pc,d = parent[r][c]
        path.append(dir_char[d])
        r,c = pr,pc

    path.reverse()

    if O == 1:
        print("True")
    elif O == 2:
        print(len(path))
    elif O == 3:
        print("".join(path))
