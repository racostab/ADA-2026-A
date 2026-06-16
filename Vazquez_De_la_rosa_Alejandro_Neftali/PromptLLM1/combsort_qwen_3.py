def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap > 1 or swapped:
        if gap > 1:
            gap = int(gap / 1.25)
        else:
            gap = 1
        swapped = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr