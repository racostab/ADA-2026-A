import sys
n = len(sys.argv) - 1
if n < 1:
    print("Error: falta la lista de enteros")
elif not all(arg.isdigit() for arg in sys.argv[1].split(',')):
    print("Error: la lista debe ser de enteros separados por comas")
else:
    a = [int(x) for x in sys.argv[1].split(',')]
    def bitonic_merge(a, down):
        if len(a) <= 1:
            return
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        if down:
            bitonic_merge(left, True)
            bitonic_merge(right, False)
            for i in range(len(left)):
                for j in range(i+1, len(left)):
                    if left[i] > left[j]:
                        left[i], left[j] = left[j], left[i]
            for i in range(len(right)):
                for j in range(i+1, len(right)):
                    if right[i] < right[j]:
                        right[i], right[j] = right[j], right[i]
            a[:mid] = sorted(left + [x for x in right])
        else:
            bitonic_merge(left, False)
            bitonic_merge(right, True)
            for i in range(len(left)):
                for j in range(i+1, len(left)):
                    if left[i] < left[j]:
                        left[i], left[j] = left[j], left[i]
            for i in range(len(right)):
                for j in range(i+1, len(right)):
                    if right[i] > right[j]:
                        right[i], right[j] = right[j], right[i]
            a[:mid] = sorted(left + [x for x in right])
    def bitonic_sort(a):
        bitonic_merge(a, True)
    bitonic_sort(a)
    print(','.join(map(str, a)))