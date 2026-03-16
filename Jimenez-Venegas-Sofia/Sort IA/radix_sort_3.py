def radix_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    base = 1
    while max_value >= base:
        buckets = [[] for _ in range(10)]
        for i in arr:
            bucket = (i // base) % 10
            buckets[bucket].append(i)
        arr = []
        for i in range(len(buckets)):
            for j in buckets[i]:
                arr.append(j * base + i)
        base *= 10
    return arr