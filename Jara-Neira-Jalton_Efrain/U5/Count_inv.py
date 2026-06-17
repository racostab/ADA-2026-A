# Author: Jalton Jara Neira
# Date: 15/06/2026 
import sys

sys.setrecursionlimit(300000)

def merge_and_count(arr, temp, left, mid, right):
    i = left
    j = mid+1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += (mid-i+1)
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right+1):
        arr[idx] = temp[idx]

    return inv_count


def merge_sort(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = left + (right-left)//2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid+1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)
    return inv_count


def main_program():
    lines = sys.stdin.read().splitlines()
    
    if not lines:
        return

    tc = int(lines[0].strip())
    line_idx = 1
    for _ in range(tc):
        if line_idx >= len(lines):
            break
            
        current_line = lines[line_idx].strip()
        line_idx += 1

        if not current_line:
            continue

        arr = [int(x) for x in current_line.split()]
        
        if len(arr) > 0:
            temp = [0]*len(arr)
            resultado = merge_sort(arr, temp, 0, len(arr)-1)
            print(resultado)
        else:
            print(0)

if __name__ == '__main__':
    main_program()