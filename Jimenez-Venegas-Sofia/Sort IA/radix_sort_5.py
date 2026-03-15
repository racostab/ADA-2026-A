def radix_sort(arr):
    max_value = max(arr)
    places = len(str(max_value))

    for place in range(places):
        buckets = [[] for _ in range(10)]

        for value in arr:
            bucket = int(str(value)[place]) if str(value)[place] != '-' else 9
            buckets[bucket].append(value)

        idx = 0
        for b in buckets:
            for v in b:
                arr[idx] = v
                idx += 1
