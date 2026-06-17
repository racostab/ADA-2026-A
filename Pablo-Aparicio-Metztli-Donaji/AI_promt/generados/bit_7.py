import sys
n = len(sys.argv[1].split(','))
nums = [int(x) for x in sys.argv[1].split(',')]
merge = lambda l,r: sorted((x for pair in zip(l,r) for x in pair), key=lambda x:x[0])

def bitonic_merge(a, d):
    if len(a)<2:
        return a
    n=len(a)//2
    if d:
        left=bitonic_merge(a[:n], d)
        right=bitonic_merge(a[n:], d)
        for i in range(n): 
            left[i],right[i]=right[i],left[i]
        return left+left[-1:]+[x for x in right if x<left[-1]]
    else:
        left=bitonic_merge(a[:n], d)
        right=bitonic_merge(a[n:], d)
        for i in range(n): 
            left[i],right[i]=right[i],left[i]
        return [x for x in right if x>left[-1]]+left

def bitonic_sort(nums, descending):
    n = len(nums)
    if n<2:
        return nums
    half=n//2
    #main bitonic sort loop
    bitonic_merge(nums, descending)

print(','.join(map(str,bitonic_sort(nums, 0))))