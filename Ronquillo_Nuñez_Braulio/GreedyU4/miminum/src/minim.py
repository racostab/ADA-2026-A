# Author: Ronquillo Nunez Braulio
# Minimum Lateness Scheduling

import sys


def minimum_lateness(times, deadlines):
    n = len(times)

    jobs = []
    for i in range(n):
        jobs.append((deadlines[i], i + 1, times[i]))

    jobs.sort(key=lambda job: (job[0], job[1]))

    current_time = 0
    max_lateness = 0
    sequence = []

    for deadline, index, time_required in jobs:
        current_time += time_required
        lateness = max(0, current_time - deadline)
        max_lateness = max(max_lateness, lateness)
        sequence.append(index)

    return max_lateness, sequence


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))

    pos = 0
    output = []

    while pos < len(data):
        n = data[pos]
        pos += 1

        if n == 0:
            break

        if pos + 2 * n > len(data):
            break

        times = data[pos : pos + n]
        pos += n

        deadlines = data[pos : pos + n]
        pos += n

        max_lateness, sequence = minimum_lateness(times, deadlines)

        output.append(str(max_lateness))
        output.append(" ".join(map(str, sequence)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
