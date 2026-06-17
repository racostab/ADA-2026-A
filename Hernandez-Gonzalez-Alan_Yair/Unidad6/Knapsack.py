import sys


data = sys.stdin.read().split()
idx = 0

while idx < len(data):
    it = int(data[idx])
    idx += 1
    w  = int(data[idx])
    idx += 1

    values  = []
    weights = []
    for _ in range(it):
        value = int(data[idx])
        idx += 1
        weight_value = int(data[idx])
        idx += 1
        values.append(value)
        weights.append(weight_value)


    dp = [[0] * (w + 1) for _ in range(it + 1)]

    for i in range(1, it + 1):
        vi = values[i - 1]
        wi = weights[i - 1]
        for j in range(w + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= wi and dp[i - 1][j - wi] + vi > dp[i][j]:
                dp[i][j] = dp[i - 1][j - wi] + vi

    print(dp[it][w])

    selected = []
    j = w
    for i in range(it, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected.append(i) 
            j -= weights[i - 1]

    selected.sort()

    print(' '.join([str(x) for x in selected]))

