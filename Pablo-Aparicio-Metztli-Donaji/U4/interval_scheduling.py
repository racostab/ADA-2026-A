# We have a collection of jobs (tasks) to schedule on some machine, and each job j has a given start time stj and a given finish time ftj . 
# If two jobs overlap, we can’t schedule them both. Our goal is to schedule as many non-overlapping jobs as possible SJ on our machine.
# Input
# The input file contains several test cases, each of them as described below. The first line contains one integer N (1 ≤ N ≤ 1000) specifying 
# the number of jobs that are considered as 1-indexed array. This is followed by two lines: i) the first line contains the start time of jobs, 
# an integer stj (1 ≤ stj ≤ 1000), ii) the second line contains the finish time of jobs, an integer ftj (1 ≤ ftj ≤ 1000).
# Output
# For each test case, on a line by itself, display the number of scheduled jobs SJ. This is followed by SJ numbers that identifies the jobs of the solutions.
# Sample Input
# 9
# 1 2 4 1 5  6  9 11 13
# 3 5 7 8 9 10 11 14 16
# Sample Output
# 4
# 1 3 6 8

def entrada():
    n = int(input())
    st = []
    ft = []
    st = list(map(int, input().split()))
    ft = list(map(int, input().split()))
    return n,st,ft

def print_output(c):
    print(len(c))
    print(*c)

def order(n,st,ft):
    jobs = [(ft[i],st[i], i+1) for i in range(n)]
    jobs.sort()

    s = []
    last_finished = 0
    for finish, start, job in jobs:
        if start >= last_finished:
            s.append(job)
            last_finished = finish
    
    return s

def main():
    n,st,sf = entrada()
    r = order(n,st,sf)
    r.sort()
    print_output(r)

if __name__ == "__main__":
    main()