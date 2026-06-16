import math

def distancia(p, q):
    return math.dist(p, q)


def ClosestSplitPair(Px, Py, d):
    n = len(Px)
    best = d
    best_pair = None,None

    mid_x = Px[n // 2][0]

    # puntos dentro de la franja 2d
    Sy = []
    for p in Py:
        if mid_x - d <= p[0] <= mid_x + d:
            Sy.append(p)

    # revisar solo hasta 7 vecinos
    for i in range(len(Sy)):
        for j in range(1, 8):
            if i + j < len(Sy):

                p = Sy[i]
                q = Sy[i + j]

                dist = distancia(p, q)

                if dist < best:
                    best = dist
                    best_pair = (p, q)

    return best_pair


def ClosestPair(Px, Py):
    n = len(Px)

    # caso base
    if n <= 3:
        best_pair = None
        best = float("inf")

        for i in range(n):
            for j in range(i + 1, n):
                dist = distancia(Px[i], Px[j])
                if dist < best:
                    best = dist
                    best_pair = (Px[i], Px[j])

        return best_pair

    # dividir
    mid = n // 2
    Lx = Px[:mid]
    Rx = Px[mid:]

    # set para dividir Py en O(n)
    Lx_set = set(Lx)

    Ly = []
    Ry = []

    for p in Py:
        if p in Lx_set:
            Ly.append(p)
        else:
            Ry.append(p)

    # recursión
    p_1, q_1 = ClosestPair(Lx, Ly)
    p_2, q_2 = ClosestPair(Rx, Ry)

    d = min(
        distancia(p_1, q_1),
        distancia(p_2, q_2)
    )

    p_3, q_3 = ClosestSplitPair(Px, Py, d)

    # elegir mejor entre los 3
    candidatos = [
    (p_1, q_1),
    (p_2, q_2),
    (p_3, q_3)
    ]

    candidatos_validos = [
    pair for pair in candidatos
    if pair[0] is not None and pair[1] is not None
    ]

    best_pair = min(
        candidatos_validos,
        key=lambda pair: distancia(pair[0], pair[1]))

    return best_pair    

def closest_pair(points):
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])
    return ClosestPair(Px, Py)
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
p, q = closest_pair(points)
print(f"{distancia(p, q):.6f}")

#EJERCICIO APROBADO POR COUCH
