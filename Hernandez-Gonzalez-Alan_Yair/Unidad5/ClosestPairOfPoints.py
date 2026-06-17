import math
import sys

def get_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

#caso base, cuando se tienen pocos puntos no vale la pena dividilo
def case_base(points):
    min_d = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_d = min(min_d, get_distance(points[i], points[j]))
    return min_d

def closest_strip(strip, d):
    strip.sort(key=lambda p: p[1])
    min_d = d
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_d:
            min_d = min(min_d, get_distance(strip[i], strip[j]))
            j += 1
    return min_d

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return case_base(points)
    
    mid = n // 2
    mid_x = points[mid][0]
    
    d = min(closest_pair(points[:mid]), closest_pair(points[mid:]))
    strip = [p for p in points if abs(p[0] - mid_x) < d]
    return min(d, closest_strip(strip, d))


data = sys.stdin.read().split()
idx = 0
results = []

while idx < len(data):
    n = int(data[idx])
    idx += 1
    points = []
    for _ in range(n):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        points.append((x, y))

    points.sort(key=lambda p: p[0]) 
    results.append(f"{closest_pair(points):.6f}")

print('\n'.join(results))

