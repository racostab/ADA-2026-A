#print("Ingrese el número de trabajos N:")
N = int(input())
#print(f"\nIngrese los {N} tiempos de inicio (separados por espacio):")
inicios = list(map(int, input().split()))
#print(f"\nIngrese los {N} tiempos de finalización (separados por espacio):")
finales = list(map(int, input().split()))

trabajos = []
for i in range(N):
    trabajos.append((inicios[i], finales[i], i + 1))
trabajos.sort(key=lambda x: x[1])
seleccionados = []
ultimo_fin = 0

for inicio, fin, idx in trabajos:
    if inicio >= ultimo_fin:
        seleccionados.append(idx)
        ultimo_fin = fin

seleccionados.sort()
print(len(seleccionados))
print(' '.join(map(str, seleccionados)))
