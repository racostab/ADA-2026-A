def radix_sort(arr):
    max_value = max(arr)
    place_values = len(str(max_value))

    for place in range(place_values):
        buckets = [[] for _ in range(10)]
        output = []

        for i in arr:
            digit = (i // (10 ** place)) % 10
            buckets[digit].append(i)

        for i in range(len(buckets)):
            for j in buckets[i]:
                output.append(j)

        arr = output

    return arr