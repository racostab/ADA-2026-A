def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        buckets = [[] for _ in range(10)]
        for i in arr:
            buckets[ (i // exp) % 10 ].append(i)
        arr.clear()
        for i in range(len(buckets)):
            for j in buckets[i]:
                arr.append(j * exp + i)
        exp *= 10

# prueba
arr = [23, 170, 31, 441, 7, 1]
radix_sort(arr)
print(arr)