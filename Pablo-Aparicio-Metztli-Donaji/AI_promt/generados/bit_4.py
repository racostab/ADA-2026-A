import sys
n = len(sys.argv[1].split(','))
arr = [int(x) for x in sys.argv[1].split(',')]
def bitonic_sort(arr, direction):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n//2):
        for j in range(i, n-i-1):
            if (direction == 0 and arr[j] > arr[j+1]) or (direction == 1 and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def bitonic_merge(arr, direction):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n//2):
        left = arr[:n//2]
        right = arr[n//2:]
        left, right = bitonic_sort(left, direction), bitonic_sort(right, direction)
        arr = list(zip(*((j[0] if direction == 0 else j[1]) for j in zip(left, right))))[0]
    return arr
arr = bitonic_merge(arr, 0)
print(', '.join(map(str, arr)))