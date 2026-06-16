# Author: Ronquillo Nunez Braulio
# Optional task: trichotomy and asymptotic notation

import math
import sys


def scan_counterexample(limit):
    minimum_ratio = float("inf")
    maximum_ratio = 0.0
    minimum_n = 1
    maximum_n = 1

    for n in range(1, limit + 1):
        first = n
        second = n ** (1.0 + math.sin(n))
        ratio = first / second

        if ratio < minimum_ratio:
            minimum_ratio = ratio
            minimum_n = n

        if ratio > maximum_ratio:
            maximum_ratio = ratio
            maximum_n = n

    return minimum_ratio, minimum_n, maximum_ratio, maximum_n


def solve():
    text = sys.stdin.read().strip()
    limit = int(text) if text else 1000

    if limit < 1:
        print("N debe ser positivo")
        return

    minimum_ratio, minimum_n, maximum_ratio, maximum_n = scan_counterexample(limit)

    print("f(n) = n")
    print("g(n) = n^(1 + sin(n))")
    print(f"min f/g = {minimum_ratio:.6f} en n = {minimum_n}")
    print(f"max f/g = {maximum_ratio:.6f} en n = {maximum_n}")
    print("conclusion = no hay tricotomia asintotica")


if __name__ == "__main__":
    solve()
