def quick_sort(arr):
    if len(arr) <= 2:
        return arr
    piv = arr[len(arr) // 2]
    left = [x for x in arr if x < piv]
    middle = [x for x in arr if x == piv]
    right = [x for x in arr if x > piv]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([3,6,8,10,1,2,1]))