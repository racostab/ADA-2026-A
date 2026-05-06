from itertools import combinations

# Read N and R
n, r = map(int, input().split())

# Read the N objects
objects = input().split()

# Generate and print all combinations of R elements
for combo in combinations(objects, r):
    print(' '.join(combo))
