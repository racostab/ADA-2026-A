# Minimum Maximum Lateness (Greedy Algorithm)

while True:
    try:
        # Number of jobs
        N = int(input())

        # Processing times and deadlines
        t = list(map(int, input().split()))
        d = list(map(int, input().split()))

        jobs = []

        # Store as (deadline, processing_time, index)
        for i in range(N):
            jobs.append((d[i], t[i], i + 1))

        # Earliest Deadline First (EDF)
        jobs.sort()

        current_time = 0
        max_lateness = 0
        order = []

        # Schedule jobs
        for deadline, time_required, idx in jobs:

            current_time += time_required

            lateness = max(0, current_time - deadline)

            max_lateness = max(max_lateness, lateness)

            order.append(idx)

        # Output
        print(max_lateness)
        print(*order)

    except EOFError:
        break