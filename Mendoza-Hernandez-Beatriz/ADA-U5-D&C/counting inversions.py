import sys

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr, 0

    mid = n // 2

    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    inv_count = inv_left + inv_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count


def main():
    data = sys.stdin.read().strip().splitlines()

    tc = int(data[0])

    for i in range(1, tc + 1):
        arr = list(map(int, data[i].split()))
        _, inversions = merge_sort(arr)
        print(inversions)

if __name__ == "__main__":
    main()