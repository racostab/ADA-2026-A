import sys
from typing import List

def bitonic_merge(arr: List[int], ascending: bool) -> None:
    if len(arr) <= 1:
        return

    n = len(arr)

    for i in range(n // 2):
        for j in range(0, n - 2 * i - 1, 2 * i + 1):
            a = arr[j]
            b = arr[j + i + 1]
            if (ascending and a > b) or (not ascending and a < b):
                arr[j], arr[j + i + 1] = arr[j + i + 1], arr[j]

    return

def bitonic_sort(arr: List[int]) -> None:
    bitonic_merge(arr, True)
    bitonic_merge(arr, False)

def main() -> None:
    arr = list(map(int, sys.argv[1].split(',')))
    bitonic_sort(arr)
    print(','.join(map(str, arr)))

if __name__ == '__main__':
    main()