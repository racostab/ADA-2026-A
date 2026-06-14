user_input = input()
numero_tareas = user_input

user_input = input()
jobs_time =list(map(int, user_input.split()))

user_input = input()
deadlines = list(map(int,user_input.split()))

jobs = list(zip(jobs_time,deadlines))
jobs_sort = sorted(jobs,key= lambda x: x[1])

total_time = 0
max_lateness = 0
schedule = []

for job in jobs_sort:
    total_time = total_time + job[0]
    lateness = total_time -  job[1]

    schedule.append(jobs.index(job)+1)

    if lateness > max_lateness:
        max_lateness = lateness

print(max_lateness)
print(*schedule)
    


    