# Author: Jalton Efrain Jara Neira
# Date: 13/03/2026 
import sys

def program_main():
    linea1 = sys.stdin.readline().split()
    if not linea1:
        return
    n = int(linea1[0])
    r = int(linea1[1])
    elementos = sys.stdin.readline().split()
    if not elementos:
        return

    def combinatoria(inicio, actual):
        if len(actual) == r:
            print(" ".join(actual))
            return
        
        for i in range(inicio, n):
            actual.append(elementos[i])
            combinatoria(i + 1, actual)
            actual.pop()

    combinatoria(0, [])

if __name__ == "__main__":
    program_main()