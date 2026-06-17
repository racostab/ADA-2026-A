from bisect import bisect_right
import sys

data = list(map(int, sys.stdin.read().split()))
pos = 0

while pos < len(data):

    n = data[pos]
    pos += 1

    jobs = []

    for i in range(n):
        s = data[pos]
        f = data[pos + 1]
        p = data[pos + 2]
        pos += 3

        jobs.append((s, f, p, i + 1))

    jobs.sort(key=lambda x: x[1])

    finishes = [job[1] for job in jobs]

    parent = [-1] * n

    for i in range(n):
        parent[i] = bisect_right(
            finishes,
            jobs[i][0]
        ) - 1

    dp = [0] * n

    for i in range(n):

        take = jobs[i][2]

        if parent[i] != -1:
            take += dp[parent[i]]

        skip = dp[i - 1] if i else 0

        dp[i] = max(take, skip)

    selected = []

    i = n - 1

    while i >= 0:

        take = jobs[i][2]

        if parent[i] != -1:
            take += dp[parent[i]]

        skip = dp[i - 1] if i else 0

        if take > skip:
            selected.append(jobs[i][3])
            i = parent[i]
        else:
            i -= 1

    selected.sort()

    print(dp[n - 1])

    if selected:
        print(*selected)
    else:
        print()