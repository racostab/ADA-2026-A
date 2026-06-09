import math

def closest_pair(puntos,n):
    d = float("inf")

    if n <= 3:
        for i in range(n):
            for j in range(i + 1, n):
                d4 = math.sqrt((puntos[i][0] - puntos[j][0])**2 +(puntos[i][1] - puntos[j][1])**2)
                d = min(d, d4)
        return d

    m = n // 2
    m_point = puntos[m]

    d1 = closest_pair(puntos[:m],m)
    d2 = closest_pair(puntos[m:],n-m)

    d = min(d1, d2)

    p_md = [p for p in puntos if abs(p[0] - m_point[0]) < d]

    d3 = d
    p_md.sort(key=lambda p: p[1])

    for i in range(len(p_md)):
        for j in range(i + 1, len(p_md)):
            if p_md[j][1] - p_md[i][1] >= d3:
                break
            new_d = math.sqrt((p_md[i][0] - p_md[j][0])**2 +(p_md[i][1] - p_md[j][1])**2)
            d3 = min(d3, new_d)

    return min(d, d3)

n_puntos = int(input())
puntos = []
for k in range(n_puntos):
    punto = input().split()
    puntos.append((int(punto[0]),int(punto[1])))

puntos.sort()
dist = closest_pair(puntos,n_puntos)

print(f"{dist:.6f}")
