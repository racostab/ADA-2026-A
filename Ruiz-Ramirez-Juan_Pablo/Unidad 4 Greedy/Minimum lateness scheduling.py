##Entrada de Datos##
n = int(input())
time_finish = list(map(int, input().split()))
deadline = list(map(int, input().split()))

#Creación de tupla para manejo de datos
actividades = []
for i in range(n):
    actividades.append((i+1, time_finish[i], deadline[i]))
#Ordenamiento de datos en tupla
actividades.sort(key=lambda x: x[2])

f = 0
L_max = 0
Trabajos = []

for actividad in actividades:
    I, time_finish, deadline = actividad
    sj = f
    fj = f + time_finish
    f =  f + time_finish
    lj = max(0,fj - deadline)
    L_max = max(L_max,lj) 
    Trabajos.append(I)

print(L_max)
print(*Trabajos)