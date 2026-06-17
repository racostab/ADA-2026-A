import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    izq, inv_izq = merge_sort(arr[:mid])
    der, inv_der = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    inversiones = inv_izq + inv_der

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            merged.append(izq[i])
            i += 1
        else:
            merged.append(der[j])
            inversiones += len(izq) - i
            j += 1

    merged.extend(izq[i:])
    merged.extend(der[j:])

    return merged, inversiones


def main():
    input = sys.stdin.readline

    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))

        _, inv = merge_sort(arr)

        print(inv)

main()