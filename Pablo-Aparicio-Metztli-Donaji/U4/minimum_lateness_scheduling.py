# We have a single resource and a set of n jobs to use the resource for an interval of time. Each job j has a deadline dj and time required to finish the job tj. 
# Each job j must be assigned an interval of time tj which must not overlap with other accepted jobs. You must note that since we are scheduling the jobs on one 
# resource, we could find the starting (sj) and finishing time (fj) of each job by the relation fj = sj + tj.

# We are willing to schedule maximum jobs before their respective deadlines or at least in a way to decrease the time lag in finish time and deadline of the chosen 
# job (i.e., lateness). We define lateness L = max {0, fj - dj } for all j. The goal is to minimize the maximum lateness L.

# Input
# The input file contains several test cases, each of them as described below. The first line contains one integer N (1 ≤ N ≤ 1000) specifying the number of jobs 
# that are considered as 1-indexed array. This is followed by two lines: i) the first line contains the time required to finish the job, an integer tj (1 ≤ tj ≤ 1000), 
# and ii) the second line contains the deadline of job, an integer dj (1 ≤ dj ≤ 1000).

# Output
# For each test case, on a line by itself, display the number of maximal lateness L. This is followed by one line with the sequence of numbers that identifies the jobs.
# Sample Input
# 6
# 3 2 1 4  3  2
# 6 8 9 9 14 15

# Sample Output
# 1
# 1 2 3 4 5 6
def order(n, t, d):
    jobs = [(d[i], t[i], i+1) for i in range(n)]
    jobs.sort()
    return jobs

def entrada():
    n = int(input())
    t = list(map(int, input().split()))
    d = list(map(int, input().split()))
    return n, t, d

def lateness(jobs):
    t = 0
    lmax = 0
    job = []
    for i in jobs:
        d, tf, I = i
        fj = t + tf
        t = t + tf
        lj = max(0, fj - d)
        lmax = max(lmax, lj)
        job.append(I)
    return lmax, job

def main(): 
    n, t, d = entrada()
    jobs = order(n, t, d)
    lat, job = lateness(jobs)
    print(lat)
    print(*job)

if __name__ == "__main__":
    main()