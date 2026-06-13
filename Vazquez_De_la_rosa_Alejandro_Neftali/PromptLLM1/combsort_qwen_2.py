def comb_sort(arr):
    n = len(arr)
    gap = n - 1
    shrink_factor = 1.3
    while gap > 1:
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
        gap = int(gap / shrink_factor)
    return arr