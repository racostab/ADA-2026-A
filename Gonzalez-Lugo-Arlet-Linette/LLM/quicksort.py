from sys import argv

if len(argv) != 2:
    print("Error: Debes proporcionar un argumento")
    exit(1)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    arr = quicksort(argv[1].split(','))
    print(','.join(map(str, arr)))