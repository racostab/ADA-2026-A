def radix_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    size = len(str(max_value))
    buckets = [[] for _ in range(10)]

    for exp in range(1, size + 1):
        for i in arr:
            digit = (i // (10 ** (exp - 1))) % 10
            buckets[digit].append(i)

        index = 0
        for i in range(0, len(buckets)):
            for j in buckets[i]:
                arr[index] = j
                index += 1

        buckets = [[] for _ in range(10)]