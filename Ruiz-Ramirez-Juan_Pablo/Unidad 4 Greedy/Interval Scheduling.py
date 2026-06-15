##Entrada de Datos##
n = int(input())
ST = list(map(int, input().split()))
FT = list(map(int, input().split()))

#Creación de tupla para manejo de datos
actividades = []
for i in range(n):
    actividades.append((i+1, ST[i], FT[i]))
#Ordenamiento de datos en tupla
actividades.sort(key=lambda x: x[2])

ft_ultimo = 0
Trabajos = []

for actividad in actividades:
    I, st, ft = actividad
    if st >= ft_ultimo:
        Trabajos.append(I)
        ft_ultimo = ft

print(len(Trabajos))
Trabajos.sort()
print(*Trabajos)