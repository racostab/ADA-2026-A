def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_split = merge(left, right)
    return merged, inv_left + inv_right + inv_split

def merge(left, right):
    i = j = 0
    merged = []
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

tc = int(input())
resultados = []

for _ in range(tc):
    arr = list(map(int, input().split()))
    _, inv = merge_sort(arr)
    resultados.append(inv)  
for r in resultados:
    print(r)