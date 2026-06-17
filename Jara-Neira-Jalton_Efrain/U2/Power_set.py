# Author: Jalton Efrain Jara Neira
# Date: 13/03/2026 
import sys

def program_main():

    def powerset(S, k, inicio, actual):
        if len(actual) == k:
            print(" ".join(actual))
            return
    
        for i in range(inicio, len(S)):
            actual.append(S[i])
            powerset(S, k, i + 1, actual)
            actual.pop()

    lineas = sys.stdin.readlines()
    if len(lineas) >= 2:
        N = int(lineas[0].strip())
        S1 = lineas[1].split()

        for tamano in range(1, N + 1):
            powerset(S1, tamano, 0, [])

if __name__ == "__main__":
    program_main()