import sys
n = list(map(int,sys.argv[1].split(',')))
def bitonic_merge(ascending,a,b):
    if ascending:
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[j]>a[i]:
                    a[i],a[j]=a[j],a[i]
                    b[i^1],b[j^1]=b[j^1],b[i^1]
    else:
        for i in range(len(a)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if a[j]<a[i]:
                    a[i],a[j]=a[j],a[i]
                    b[i^1],b[j^1]=b[j^1],b[i^1]
    return a,b
def bitonic_sort(ascending,a):
    n = len(a)
    if n <= 1:
        return a,a
    mid = n//2
    left, lsign = bitonic_sort((ascending!=ascending and (a[:mid]) or ascending),a[:mid])
    right,rsign = bitonic_sort((not ascending) or ascending, a[mid:])
    left,right = bitonic_merge(ascending,left,lsign+right)
    return left,right
def main():
    n = list(map(int,sys.argv[1].split(',')))
    asc = 0
    if len(sys.argv)>2:
        if sys.argv[2]=="-o":
            asc=1
        elif sys.argv[2]=="-d":
            asc=0
    else:
        asc=1
    n.sort()
    left,right = bitonic_sort(asc,n)
    print(','.join(map(str,left)))
if __name__ == "__main__":
    main()