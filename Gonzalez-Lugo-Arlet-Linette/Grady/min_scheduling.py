def resolver():
    N = int(input(""))
    #print("Ingrese los tiempos t:")
    t = list(map(int, input().split()))
    #print("Ingrese los deadlines d:")
    d = list(map(int, input().split()))
    
    trabajos = []
    for i in range(N):
        trabajos.append((t[i], d[i], i + 1))
    
    trabajos.sort(key=lambda x: x[1])
    
    tiempo_actual = 0
    max_lateness = 0
    secuencia = []
    
    for duracion, deadline, indice in trabajos:
        tiempo_actual += duracion
        latencia = max(0, tiempo_actual - deadline)
        if latencia > max_lateness:
            max_lateness = latencia
        secuencia.append(indice)
    
    print(max_lateness)
    print(" ".join(map(str, secuencia)))

if __name__ == "__main__":
    resolver()
