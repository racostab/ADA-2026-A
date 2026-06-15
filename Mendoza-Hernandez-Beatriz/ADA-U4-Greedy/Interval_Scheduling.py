# Activity Selection Problem (Greedy)

while True:
    try:
        # Number of jobs
        N = int(input())

        # Start and finish times
        start = list(map(int, input().split()))
        finish = list(map(int, input().split()))

        jobs = []

        # Store as (finish_time, start_time, index)
        for i in range(N):
            jobs.append((finish[i], start[i], i + 1))

        # Sort by finish time
        jobs.sort()

        selected = []

        # Select first job
        last_finish = -1

        for f, s, idx in jobs:

            # Non-overlapping condition
            if s >= last_finish:
                selected.append(idx)
                last_finish = f

        # Output
        print(len(selected))
        print(*selected)

    except EOFError:
        break