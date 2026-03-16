def radix_sort(arr):
    max_value = max(arr)
    smallest_digit = 1
    while max_value >= smallest_digit:
        buckets = [[] for _ in range(10)]
        for i in arr:
            digit = (i // smallest_digit) % 10
            buckets[digit].append(i)
        idx = 0
        for b in buckets:
            for i in b:
                arr[idx] = i
                idx += 1
        smallest_digit *= 10
    return arr
