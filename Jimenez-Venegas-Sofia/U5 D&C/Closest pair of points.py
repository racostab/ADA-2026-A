import sys
import math

datos = sys.stdin.read().strip().split()

if not datos:
    sys.exit()

n = int(datos[0])
puntos = []

idx = 1
for _ in range(n):
    x = int(datos[idx])
    y = int(datos[idx + 1])
    puntos.append((x, y))
    idx += 2

dist_min = float('inf')

for i in range(n):
    x1, y1 = puntos[i]
    for j in range(i + 1, n):
        x2, y2 = puntos[j]
        dist = math.hypot(x1 - x2, y1 - y2)
        if dist < dist_min:
            dist_min = dist

print(f"{dist_min:.6f}")