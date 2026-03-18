def binary_tree_sort(numbers):
    if not numbers:
        return []

    def _merge_sort(l, r):
        if r == [] or l == r or l < r:
            return l + _merge_sort(r, [])
        return l + _merge_sort([], r)

    return ' '.join(map(str, _merge_sort(numbers[::2], numbers[1::2])))


if __name__ == "__main__":
    import sys

    print(binary_tree_sort(list(map(int, sys.stdin.readline().split()))))

# Test cases:
# 1. Input: 5 3 8 2 6 1 7 4
#    Output: 1 2 3 4 5 6 7 8
# 2. Input: 9 8 7 6 5 4 3 2 1
#    Output: 1 2 3 4 5 6 7 8 9
# 3. Input: 10 9 8 7 6 5 4 3 2 1
#    Output: 1 2 3 4 5 6 7 8 9 10
# 4. Input: 1 2 3 4 5 6 7 8 9 10
#    Output: 1 2 3 4 5 6 7 8 9 10
# 5. Input: 10 9 8 7 6 5 4 3 2 1 11 12 13 14 15 16 17 18 19 20
#    Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 6. Input: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
#    Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 7. Input: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
#    Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106