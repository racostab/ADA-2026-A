# Power set P(S) of a set S is the set of all subsets of S. If S has n elements in it then P(s) will have 2n elements. 
# For example S = {a, b, c} then |P(S)|=2^3=8 and P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}. 
# Given an array of size N, generate and print the power set P(S).
# Input
# The input contains only one test case as described below. The first line contains one integer N (1 <= N <= 1000) 
# specifying the number of elements. The second line contains the N elements which are separated by space.
# Output
# Output Output the list of all possible subsets of S, each subset on a line by itself. The list and its elements are 
# arranged from lowest to highest value -sorted ascending, using its position and the cardinality (in increasing order). 
# The empty set is not printed.
# Sample Input
# 3
# a b c
# Sample Output
# a
# b
# c
# a,b
# a c
# b c
# a b c

# Author: Donaji Pablo
# Date: 10/03/2026 
from itertools import combinations

def main():
    n = int(input())
    results = []
    elements = input().split()
    for subset in range(1,(2**n)-1):
         for c in combinations(elements, subset):
            results.append(c)
            print(*c)

if __name__ == "__main__":
     main()