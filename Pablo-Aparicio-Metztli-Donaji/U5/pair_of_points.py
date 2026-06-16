# Given n points in the plane, find a pair of points with the smallest Euclidean distance between them.
# Input
# The input file contains several test cases, each of them as described below. The first line contains one 
# integer N (1 ≤ N ≤ 1000) specifying the number of points. This is followed by N lines with the coordinates 
# of the points xi and yi (1 ≤ xi, yi ≤ 10000) integers.
# Output
# For each test case, on a line by itself, display the euclidean distance with an absolute or relative error 
# of at most 10-6.
# Sample Input
# 6
# 2 3
# 12 30
# 40 50
# 5 1
# 12 10
# 3 4
# Sample Output
# 1.414214
import math

def entry(n):
    points = []
    for _ in range(n):
        x , y = map(int, input().split())
        points.append((x , y))
    return points

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def strip_closest(strip, d):
    min_d = d
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_d:
            min_d = min(min_d, dist(strip[i], strip[j]))
            j += 1
    return min_d

def closest_pair(points):
    n = len(points)

    if n == 2:
        return dist(points[0], points[1])
    if n == 1:
        return float('inf')

    mid = n // 2
    mid_point = points[mid]

    left  = points[:mid]
    right = points[mid:]

    d_left  = closest_pair(left)
    d_right = closest_pair(right)
    d = min(d_left, d_right)
    strip = [p for p in points if abs(p[0] - mid_point[0]) < d]

    return min(d, strip_closest(strip, d))

def main():
    n = int(input())
    points = entry(n)
    points.sort()
    p = closest_pair(points)
    print(f"{p:.6f}")

if __name__ == "__main__":
    main()