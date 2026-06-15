import sys
import math

def main():
    data = sys.stdin.read().strip().splitlines()

    n = int(data[0])

    points = []
    for i in range(1, n + 1):
        x, y = map(int, data[i].split())
        points.append((x, y))

    min_dist = float('inf')

    for i in range(n):
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]

            dx = x1 - x2
            dy = y1 - y2

            dist = math.sqrt(dx * dx + dy * dy)

            if dist < min_dist:
                min_dist = dist

    print(f"{min_dist:.6f}")

if __name__ == "__main__":
    main()