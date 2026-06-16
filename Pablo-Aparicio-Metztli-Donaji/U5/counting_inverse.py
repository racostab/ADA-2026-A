# Given an array of integers A, find the Inversion Count in the array. Inversion Count: For an array, inversion count indicates 
# how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is 
# sorted in the reverse order then the inversion count is the maximum. Formally, two elements A[i] and A[j] form an inversion 
# if A[i] > A[j] and i < j.
# Input
# The input file contains several test cases, each of them as described below. The first line contains one integer TC (1 ≤ TC ≤ 100) 
# specifying the number of test cases. This is followed by TC lines with N (1 ≤ N ≤ 5*105) integers.
# Output
# For each test case, on a line by itself, display the number of inversions.
# Sample Input
# 2
# 2 4 1 3 5
# 2 3 4 5 6
# Sample Output
# 3
# 0

import sys
input = sys.stdin.readline

def merge_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inversions = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            # arr[i..mid] todos son mayores que arr[j]
            inversions += (mid - i + 1)
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inversions


def merge_sort(arr, temp, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort(arr, temp, left, mid)
        inversions += merge_sort(arr, temp, mid + 1, right)
        inversions += merge_count(arr, temp, left, mid, right)
    return inversions


def count_inversions(arr):
    temp = [0] * len(arr)
    return merge_sort(arr, temp, 0, len(arr) - 1)


def main():
    tc = int(input())
    arrs = []
    for _ in range(tc):
        arr = list(map(int, input().split()))
        arrs.append(count_inversions(arr))
    for i in arrs:
        print(i)

if __name__ == "__main__":
    main()