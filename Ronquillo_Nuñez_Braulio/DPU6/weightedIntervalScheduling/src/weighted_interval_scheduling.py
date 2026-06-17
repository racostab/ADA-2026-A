# Author: Ronquillo Nunez Braulio
# Weighted Interval Scheduling

import bisect
import sys


def better(first, second):
    first_profit, first_jobs = first
    second_profit, second_jobs = second

    if first_profit != second_profit:
        return first if first_profit > second_profit else second

    return first if first_jobs < second_jobs else second


def solve_case(jobs):
    ordered_jobs = sorted(jobs, key=lambda job: (job[1], job[0], job[3]))
    finish_times = [job[1] for job in ordered_jobs]

    best = [(0, tuple()) for _ in range(len(ordered_jobs) + 1)]

    for i, (start_time, _, profit, original_index) in enumerate(ordered_jobs, start=1):
        compatible = bisect.bisect_right(finish_times, start_time, 0, i - 1)
        selected_jobs = tuple(sorted(best[compatible][1] + (original_index,)))
        take_current = (best[compatible][0] + profit, selected_jobs)
        skip_current = best[i - 1]

        best[i] = better(take_current, skip_current)

    return best[-1]


def solve():
    data = sys.stdin.buffer.read().split()
    pos = 0
    output = []

    while pos < len(data):
        job_count = int(data[pos])
        pos += 1

        if pos + 3 * job_count > len(data):
            break

        jobs = []
        for original_index in range(1, job_count + 1):
            start_time = int(data[pos])
            finish_time = int(data[pos + 1])
            profit = int(data[pos + 2])
            pos += 3

            jobs.append((start_time, finish_time, profit, original_index))

        max_profit, selected_jobs = solve_case(jobs)
        output.append(str(max_profit))
        output.append(" ".join(map(str, selected_jobs)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()
