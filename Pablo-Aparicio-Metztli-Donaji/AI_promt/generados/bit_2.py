import sys
n = list(map(int, sys.argv[1].split(',')))
def bitonic_merge(left, right):
    for i in range(len(left)):
        if left[i] > right[-i-1]:
            left[i], right[-i-1] = right[-i-1], left[i]
def bitonic_sort(arr):
    for _ in range(len(arr) // 2):
        bitonic_merge(arr[:len(arr)//2], arr[len(arr)//2:])
        if (len(arr) & 1):
            bitonic_merge([arr[0]], arr[1:])
    print(','.join(map(str, arr)))