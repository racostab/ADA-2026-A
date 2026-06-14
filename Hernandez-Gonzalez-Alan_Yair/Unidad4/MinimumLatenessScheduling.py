import sys

input_data = sys.stdin.read().split()
idx = 0

while idx < len(input_data):
    jobs_number = int(input_data[idx])
    idx += 1
    time_required = [int(input_data[idx + j]) for j in range(jobs_number)]
    idx += jobs_number
    deadline = [int(input_data[idx + j]) for j in range(jobs_number)]
    idx += jobs_number

    # se ordenan los jobs por el deadline
    jobs = sorted(range(jobs_number), key=lambda j: deadline[j])

    time = 0
    max_lateness = 0
    for j in jobs:
        time += time_required[j]
        #calculamos el retraso
        lateness = max(0, time - deadline[j])
        #si el retrasp actual es más gramde se almacena
        max_lateness = max(max_lateness, lateness)

    print(max_lateness)
    print(" ".join(str(j+1) for j in jobs))