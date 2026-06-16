# Given two integer A and B of n bits, find their multiplication (C = A B) using the Karatsuba’s algorithm.

# For instance if A = 264 = 18,446,744,073,709,551,616 and its binary representation (grouped by 10 bits) is:
# 1000000000 0000000000 0000000000 0000000000 0000000000 0000000000 00000

# and B = A +1 , then C is
# C = 34,028,236,692,0938,463,481,821,351,505,477,763,072 and its binary representation is:
# 00010000000000000000000000000000000000000000000000000000000000000001000000000000000000000 0000000000000000000000000000000000000000000

# Input
# The input file contains several test cases, each of them as described below. The first line contains one integer N (1 ≤ N ≤ 1000) 
# specifying the number of test cases. This is followed by N lines with two integer numbers ai and bi , wher i (1 ≤ i ≤ N) in binary 
# representation which are separated by one space (when necesary is represented by ‘_’).
# Output
# For each test case, on a line by itself, display the multiplication of ai and bi. Only print significant zeros.
# Sample Input
# 2
# 1000000000000000000000000000000000000000000000000000000000000000 1000000000000000000000000000000000000000000000000000000000000001
# 101 100
# Sample Output
# 100000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000
# 10100

import sys
input = sys.stdin.readline

def entry(n):
    pairs = []
    for _ in range(n):
        a, b = input().split()
        a = a.replace('_', '')
        b = b.replace('_', '')
        pairs.append((a, b))
    return pairs

def karatsuba(x, y):
    if x < 2 or y < 2:
        return x * y

    n = max(x.bit_length(), y.bit_length())
    half = n // 2

    mask = (1 << half) - 1
    x1, x0 = x >> half, x & mask
    y1, y0 = y >> half, y & mask

    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0

    return (z2 << (2 * half)) + (z1 << half) + z0

def main():
    n = int(input())
    pairs = entry(n)

    for a_bin, b_bin in pairs:
        a = int(a_bin, 2)
        b = int(b_bin, 2)

        c = karatsuba(a, b)

        if c == 0:
            print(0)
        else:
            print(bin(c)[2:])

if __name__ == "__main__":
    main()