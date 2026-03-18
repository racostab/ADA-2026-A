def shell_sort(arr):
    # Choose the gap size
    gap = len(arr) // 2

    # Repeat the process for each gap size
    while gap > 0:
        # Compare elements with the gap size
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                # Swap elements if they are in the wrong order
                arr[j] = arr[j - gap]
                j -= gap
            # Place the element in its correct position
            arr[j] = temp
        # Decrease the gap size
        gap //= 2

    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", shell_sort(arr))