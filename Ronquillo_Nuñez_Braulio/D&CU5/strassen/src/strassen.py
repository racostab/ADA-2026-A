# Author: Ronquillo Nunez Braulio
# Strassen Matrix Multiplication

import sys

THRESHOLD = 32


def next_power_of_two(value):
    size = 1
    while size < value:
        size *= 2
    return size


def pad_matrix(matrix, size):
    padded = [[0] * size for _ in range(size)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            padded[i][j] = matrix[i][j]

    return padded


def add_matrix(first, second):
    n = len(first)
    return [[first[i][j] + second[i][j] for j in range(n)] for i in range(n)]


def subtract_matrix(first, second):
    n = len(first)
    return [[first[i][j] - second[i][j] for j in range(n)] for i in range(n)]


def standard_multiply(first, second):
    n = len(first)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for k in range(n):
            value = first[i][k]
            if value == 0:
                continue
            for j in range(n):
                result[i][j] += value * second[k][j]

    return result


def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2

    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_left = [row[:mid] for row in matrix[mid:]]
    bottom_right = [row[mid:] for row in matrix[mid:]]

    return top_left, top_right, bottom_left, bottom_right


def join_quadrants(top_left, top_right, bottom_left, bottom_right):
    n = len(top_left)
    result = []

    for i in range(n):
        result.append(top_left[i] + top_right[i])
    for i in range(n):
        result.append(bottom_left[i] + bottom_right[i])

    return result


def strassen(first, second):
    n = len(first)

    if n <= THRESHOLD:
        return standard_multiply(first, second)

    a11, a12, a21, a22 = split_matrix(first)
    b11, b12, b21, b22 = split_matrix(second)

    m1 = strassen(add_matrix(a11, a22), add_matrix(b11, b22))
    m2 = strassen(add_matrix(a21, a22), b11)
    m3 = strassen(a11, subtract_matrix(b12, b22))
    m4 = strassen(a22, subtract_matrix(b21, b11))
    m5 = strassen(add_matrix(a11, a12), b22)
    m6 = strassen(subtract_matrix(a21, a11), add_matrix(b11, b12))
    m7 = strassen(subtract_matrix(a12, a22), add_matrix(b21, b22))

    c11 = add_matrix(subtract_matrix(add_matrix(m1, m4), m5), m7)
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(subtract_matrix(add_matrix(m1, m3), m2), m6)

    return join_quadrants(c11, c12, c21, c22)


def multiply_matrices(first, second):
    original_size = len(first)
    size = next_power_of_two(original_size)

    first_padded = pad_matrix(first, size)
    second_padded = pad_matrix(second, size)
    product = strassen(first_padded, second_padded)

    return [row[:original_size] for row in product[:original_size]]


def solve():
    data = sys.stdin.buffer.read().split()

    if not data:
        return

    pos = 0
    size = int(data[pos])
    pos += 1

    first = []
    for _ in range(size):
        row = [int(data[pos + j]) for j in range(size)]
        pos += size
        first.append(row)

    second = []
    for _ in range(size):
        row = [int(data[pos + j]) for j in range(size)]
        pos += size
        second.append(row)

    product = multiply_matrices(first, second)
    output = [" ".join(map(str, row)) for row in product]
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
