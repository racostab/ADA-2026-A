import sys
n = len(list(map(int, sys.argv[1].split(','))))
def compare(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0
def bitonicMerge(n, ascending):
    for i in range(n//2):
        for j in range(0, n-i*2-1, 2):
            if (ascending and compare(int(sys.argv[1].split(',')[j]), int(sys.argv[1].split(',')[j+1])) > 0) or \
               (not ascending and compare(int(sys.argv[1].split(',')[j]), int(sys.argv[1].split',[j+1])) < 0):
                temp = int(sys.argv[1].split(',')[j])
                int(sys.argv[1].split(',')[j]) = int(sys.argv[1].split,[j+1])
                int(sys.argv[1].split ,[j+1]) = temp
    return 0
def bitonicSort(n, ascending):
    bitonicMerge(n, ascending)
    bitonicMerge(n, not ascending)
print(', '.join(map(str, sorted(map(int, sys.argv[1].split(',')))))
