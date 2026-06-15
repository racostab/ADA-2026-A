# Author: Ronquillo Nunez Braulio
# Karatsuba Integer Multiplication

import sys


def binary_to_int(bits):
    value = 0
    for bit in bits:
        value = value * 2 + (bit == "1")
    return value


def karatsuba(first, second):
    if first < 2 or second < 2:
        return first * second

    bits = max(first.bit_length(), second.bit_length())
    if bits <= 32:
        return first * second

    half = bits // 2
    mask = (1 << half) - 1

    first_low = first & mask
    first_high = first >> half
    second_low = second & mask
    second_high = second >> half

    z0 = karatsuba(first_low, second_low)
    z2 = karatsuba(first_high, second_high)
    z1 = karatsuba(first_low + first_high, second_low + second_high) - z2 - z0

    return (z2 << (2 * half)) + (z1 << half) + z0


def solve():
    raw_input = sys.stdin.read().replace("_", " ")
    data = raw_input.split()

    if not data:
        return

    test_cases = int(data[0])
    pos = 1
    output = []

    for _ in range(test_cases):
        if pos + 1 >= len(data):
            break

        first = binary_to_int(data[pos])
        second = binary_to_int(data[pos + 1])
        pos += 2

        result = karatsuba(first, second)
        output.append("0" if result == 0 else bin(result)[2:])

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
