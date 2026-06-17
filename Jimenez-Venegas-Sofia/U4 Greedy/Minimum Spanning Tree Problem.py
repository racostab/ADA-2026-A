V, E, tipo = input().split()
V = int(V)
E = int(E)

aristas = []

for _ in range(E):
    u, v, w = map(int, input().split())
    aristas.append((w, u, v))

if tipo == "min":
    aristas.sort()             
else:
    aristas.sort(reverse=True)  

padre = [i for i in range(V + 1)]

def find(x):
    if padre[x] != x:
        padre[x] = find(padre[x])
    return padre[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        padre[rb] = ra
        return True
    return False

total = 0
contar = 0

for w, u, v in aristas:
    if union(u, v):
        total += w
        contar += 1

        if contar == V - 1:
            break

print(total)