import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

jobs = []

for i in range(n):
    jobs.append((d[i], i + 1, t[i]))

jobs.sort()

tiempo_actual = 0
lateness_max = 0
orden = []

for deadline, i, t in jobs:
    tiempo_actual += t
    lateness = max(0, tiempo_actual - deadline)
    lateness_max = max(lateness_max, lateness)
    orden.append(i)

print(lateness_max)
print(*orden)