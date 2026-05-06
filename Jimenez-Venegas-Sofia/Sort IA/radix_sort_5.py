def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        bucket = [[] for _ in range(10)]
        for i in arr:
            bucket[ (i // exp) % 10 ].append(i)
        arr.clear()
        for i in range(len(bucket)):
            arr.extend(bucket[i])
        exp *= 10
    return arr