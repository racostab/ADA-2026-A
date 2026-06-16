import sys

input_data = sys.stdin.read().split()
idx = 0

while idx < len(input_data):
    job_number = int(input_data[idx])
    idx += 1    
    start_time_jobs = []
    end_time_jobs = []

    for i in range(job_number):
        start_time_jobs.append(int(input_data[idx]))
        idx += 1
    for i in range(job_number):
        end_time_jobs.append(int(input_data[idx]))
        idx += 1

    jobs = []
    #se ordenan los jobs por tiempo de finalización
    jobs = sorted([(end_time_jobs[i], start_time_jobs[i],i+1) for i in range(job_number)], key=lambda x: x[0])

    selected = []
    last_finish = -1
    for finish_time, start_time, orig_idx in jobs:
        #si el tiempo de finalización dle job es mayor al último resgistrado, se agrega a la selección
        if start_time >= last_finish:
            selected.append(orig_idx)
            last_finish = finish_time
    selected.sort()

    print(len(selected))
    print(" ".join(str(j) for j in sorted(selected)))