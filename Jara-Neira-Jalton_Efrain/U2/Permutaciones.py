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

    visitado = [False]*n

    def permutacion(actual):
        if len(actual) == r:
            print(" ".join(actual))
            return
        
        for i in range(n):
            if not visitado[i]:
                visitado[i] = True
                actual.append(elementos[i])
                
                permutacion(actual)
                actual.pop()
                visitado[i] = False

    permutacion([])

if __name__ == "__main__":
    program_main()