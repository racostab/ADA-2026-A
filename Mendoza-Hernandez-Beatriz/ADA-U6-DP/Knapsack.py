import sys

data = list(map(int, sys.stdin.read().split()))
idx = 0

while idx < len(data):
    n = data[idx]
    idx += 1

    W = data[idx]
    idx += 1

    values = [0] * (n + 1)
    weights = [0] * (n + 1)

    for i in range(1, n + 1):
        values[i] = data[idx]
        weights[i] = data[idx + 1]
        idx += 2

    # DP
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        v = values[i]
        wt = weights[i]

        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]

            if wt <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - wt] + v
                )

    # Máximo beneficio
    print(dp[n][W])

    # Reconstrucción de la solución
    selected = []
    w = W

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i]

    selected.reverse()

    print(*selected)