def cocktail_shaker_sort(arr):
    start, end = 0, len(arr) - 1
    swaps = comparisons = 0

    while start < end:
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                comparisons += 2
        end -= 1

        if start < end:
            for i in range(end, start, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swaps += 1
                    comparisons += 2
            start += 1

    return arr

def cocktail_shaker_sort_verbose(arr):
    sorted_, swaps, comparisons, passes = arr[:], 0, 0, 0
    start, end = 0, len(arr) - 1

    while start < end:
        for i in range(start, end):
            if sorted_[i] > sorted_[i + 1]:
                swaps += 1
                comparisons += 2
                sorted_[i], sorted_[i + 1] = sorted_[i + 1], sorted_[i]
        end -= 1
        passes += 1

        if start < end:
            for i in range(end, start, -1):
                if sorted_[i] < sorted_[i - 1]:
                    swaps += 1
                    comparisons += 2
                    sorted_[i], sorted_[i - 1] = sorted_[i - 1], sorted_[i]
            start += 1
        passes += 1

    return {'sorted': sorted_, 'comparisons': comparisons, 'swaps': swaps, 'passes': passes}