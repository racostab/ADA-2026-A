def radix_sort(arr):
    max_value = max(arr)
    exponent = 1
    while max_value // exponent > 0:
        buckets = [[] for _ in range(10)]
        for i in arr:
            index = (i // exponent) % 10
            buckets[index].append(i)
        arr = []
        for i in buckets:
            arr.extend(i[::-1])
        exponent *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 340]
radix_sort(arr)
print(arr)