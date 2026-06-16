nr = input().split()
n = int(nr[0])
r= int(nr[1])

numbers = input().split()
seen = set()
result = []

def printArray(arr, r):
    perm = tuple(arr[:r])
    if perm not in seen:
        seen.add(perm)
        result.append(perm)
        #print(" ".join(map(str, arr[:r])))


def permutacion(arr, size, r):
    if(size == 1):
        printArray(arr,r)
        return
    for i in range(size):
        permutacion(arr,size-1,r)
        if(size %2 == 1):
            arr[0], arr[size-1] = arr[size-1], arr[0]
        else:
            arr[i], arr[size-1] = arr[size-1], arr[i]
permutacion(numbers, n,r)
result.sort()
for p in result:
    print(*p)