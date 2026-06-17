import sys

def solve(n, starts, finishes):
    jobs = [(i+1, starts[i], finishes[i]) for i in range(n)]
    
    jobs.sort(key=lambda x: x[2])

    dp = [0]*n
    next_idx = [-1]*n
    
    for i in range(n):
        for j in range(i+1, n):
            if jobs[j][1] >= jobs[i][2]:
                next_idx[i] = j
                break
    
    for i in range(n-1, -1, -1):
        take = 1
        if next_idx[i] != -1:
            take += dp[next_idx[i]]
        
        skip = dp[i+1] if i+1 < n else 0
        
        dp[i] = max(take, skip)
    
    res = []
    i = 0
    while i < n:
        take = 1
        if next_idx[i] != -1:
            take += dp[next_idx[i]]
        
        skip = dp[i+1] if i+1 < n else 0
        
        if take >= skip:
            res.append(jobs[i][0])
            i = next_idx[i] if next_idx[i] != -1 else n
        else:
            i += 1
    
    return res


def main():
    data = list(map(int, sys.stdin.read().split()))
    i = 0
    
    while i < len(data):
        n = data[i]
        i += 1
        
        starts = data[i:i+n]
        i += n
        
        finishes = data[i:i+n]
        i += n
        
        result = solve(n, starts, finishes)
        
        print(len(result))
        result.sort()
        print(*result)


if __name__ == "__main__":
    main()