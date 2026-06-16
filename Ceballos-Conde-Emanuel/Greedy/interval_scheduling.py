user_input = input()
numero_tareas = user_input

user_input = input()
inicio_tareas =list(map(int, user_input.split()))

user_input = input()
fin_tareas = list(map(int,user_input.split()))

tareas = list(zip(inicio_tareas,fin_tareas))
tareas_sort = sorted(tareas,key= lambda x: x[1])

schedule = []
schedule.append(tareas_sort.pop(0))


while len(tareas_sort) > 0:
    tarea_actual = tareas_sort.pop(0)

    if (tarea_actual[0] >= schedule[-1][1]):
        schedule.append(tarea_actual)

print(len(schedule))

s_index = []
for job in schedule:
    s_index.append(tareas.index(job)+1)

s_index.sort()
print(*s_index)


