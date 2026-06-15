# Author: Ronquillo Nunez Braulio
# Closest Pair of Points

import math
import sys
from collections import Counter


def distance(first, second):
    return math.hypot(first[0] - second[0], first[1] - second[1])


def brute_force(points):
    best = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            best = min(best, distance(points[i], points[j]))

    return best


def closest_pair_rec(points_x, points_y):
    n = len(points_x)

    if n <= 3:
        return brute_force(points_x)

    mid = n // 2
    mid_x = points_x[mid][0]

    left_x = points_x[:mid]
    right_x = points_x[mid:]
    left_counter = Counter(left_x)

    left_y = []
    right_y = []
    for point in points_y:
        if left_counter[point] > 0:
            left_y.append(point)
            left_counter[point] -= 1
        else:
            right_y.append(point)

    best = min(closest_pair_rec(left_x, left_y), closest_pair_rec(right_x, right_y))
    strip = [point for point in points_y if abs(point[0] - mid_x) < best]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            best = min(best, distance(strip[i], strip[j]))

    return best


def closest_pair(points):
    if len(points) < 2:
        return 0.0

    points_x = sorted(points)
    points_y = sorted(points, key=lambda point: (point[1], point[0]))
    return closest_pair_rec(points_x, points_y)


def solve():
    data = sys.stdin.buffer.read().split()
    pos = 0
    output = []

    while pos < len(data):
        points_count = int(data[pos])
        pos += 1

        if pos + 2 * points_count > len(data):
            break

        points = []
        for _ in range(points_count):
            x = int(data[pos])
            y = int(data[pos + 1])
            pos += 2
            points.append((x, y))

        output.append(f"{closest_pair(points):.6f}")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
