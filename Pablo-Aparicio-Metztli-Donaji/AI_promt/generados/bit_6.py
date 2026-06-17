import sys
n = int(sys.argv[1].split(',')[0])
k = int(sys.argv[1].split(',')[1])

def bitonic_merge(arr, ascending):
    n = len(arr)
    for i in range(n//2):
        if (ascending):
            for j in range(0, n-i*2-1, 2):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        else:
            for j in range(0, n-i*2-1, 2):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

def bitonic_sort(arr, ascending):
    bitonic_merge(arr, ascending)

arr = list(map(int, sys.argv[1].split(',')))
bitonic_sort(arr, True)
print(','.join(map(str, arr)))