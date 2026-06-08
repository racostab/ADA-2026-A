import math

def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def par_mas_cercano(puntos):
    min_dist = float('inf')
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia_euclidiana(puntos[i], puntos[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def main():
    n = int(input().strip())
    puntos = []
    for _ in range(n):
        x, y = map(int, input().split())
        puntos.append((x, y))
    
    resultado = par_mas_cercano(puntos)
    print(f"{resultado:.6f}")

if __name__ == "__main__":
    main()