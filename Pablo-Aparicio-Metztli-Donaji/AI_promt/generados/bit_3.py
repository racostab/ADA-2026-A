import sys
from functools import cmp_to_key

def compare(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0

def bitonic_merge(bitonic_list, order):
    n = len(bitonic_list)
    for k in range(n // 2):
        for i in range(0, n - 2 * k - 1, 2):
            j = i + 1
            if (order == 1 and bitonic_list[i] <= bitonic_list[j]) or (order == 0 and bitonic_list[i] >= bitonic_list[j]):
                bitonic_list[i], bitonic_list[j] = bitonic_list[j], bitonic_list[i]
    return bitonic_list

def bitonic_sort(bitonic_list, order):
    n = len(bitonic_list)
    for k in range(n // 2):
        left = bitonic_merge(bitonic_list[:n // 2], order)
        right = bitonic_merge(bitonic_list[n // 2:], order)
        bitonic_list = list(left) + list(right)
    return bitonic_list

def main():
    num_list = [int(x) for x in sys.argv[1].split(',')]
    sorted_list = list(map(lambda x: x, bitonic_sort(num_list, 0)))
    print(','.join(map(str, sorted_list)))

if __name__ == '__main__':
    main()