def radix_sort(arr):
    max_value = max(arr)
    exponent = 1
    while max_value >= 10:
        max_value //= 10
        exponent += 1

    buckets = [[[] for _ in range(10)] for _ in range(len(arr))]

    for i in range(exponent):
        for j, value in enumerate(arr):
            index = (value // (10 ** i)) % 10
            buckets[i][index].append(arr[j])
        arr.clear()
        for bucket in buckets[i]:
            arr.extend(bucket)
