import sys
input = sys.stdin.readline

def merge_count(array):
    if len(array) <= 1:
        return array, 0
    mid = len(array) // 2

    #dividomos el arreglo en dos mitades
    left, inversion_left = merge_count(array[:mid])
    right, inversion_right = merge_count(array[mid:])
    inversion = inversion_left + inversion_right

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            inversion += len(left) - i
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversion



data = sys.stdin.read().split('\n')
tc = int(data[0])
for i in range(1, tc + 1):
    if i < len(data) and data[i].strip():
        array = list(map(int, data[i].split()))
        _, inversions = merge_count(array)
        print(inversions)

