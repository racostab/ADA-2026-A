def cocktail_shaker_sort(arr):
    start, end = 0, len(arr) - 1
    swaps = 0
    comparisons = 0

    while start < end:
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
            comparisons += 1
        end -= 1

        if start < end:
            for i in range(end, start, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swaps += 1
            start += 1

    return arr

def cocktail_shaker_sort_verbose(arr):
    start, end = 0, len(arr) - 1
    swaps = 0
    comparisons = 0
    passes = 0

    data = {'sorted': arr}

    while start < end:
        passes += 1
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
            comparisons += 1
        end -= 1

        if start < end:
            for i in range(end, start, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swaps += 1
            start += 1

    data['comparisons'] = comparisons
    data['swaps'] = swaps
    data['passes'] = passes

    return data
