# Author: Ronquillo Nunez Braulio
# Counting Inversions

import sys


def count_inversions(values):
    n = len(values)
    if n <= 1:
        return 0

    source = values[:]
    target = [0] * n
    width = 1
    inversions = 0

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if source[i] <= source[j]:
                    target[k] = source[i]
                    i += 1
                else:
                    target[k] = source[j]
                    inversions += mid - i
                    j += 1
                k += 1

            while i < mid:
                target[k] = source[i]
                i += 1
                k += 1

            while j < right:
                target[k] = source[j]
                j += 1
                k += 1

        source, target = target, source
        width *= 2

    return inversions


def parse_cases(lines):
    if not lines:
        return []

    test_cases = int(lines[0].split()[0])
    remaining = [line.split() for line in lines[1:] if line.split()]

    if len(remaining) >= test_cases:
        return [[int(value) for value in remaining[i]] for i in range(test_cases)]

    return [[int(value) for value in parts] for parts in remaining]


def solve():
    lines = sys.stdin.buffer.readlines()
    cases = parse_cases(lines)
    output = []

    for case in cases:
        output.append(str(count_inversions(case)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
