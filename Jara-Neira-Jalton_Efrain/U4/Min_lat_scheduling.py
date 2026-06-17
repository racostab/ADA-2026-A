# Author: Jalton Efrain Jara Neira
# Date: 10/05/2026 
import sys
sys.setrecursionlimit(2000)

def opt(tasks, current_time, max_lateness, current_index):
    if current_index >= len(tasks):
        return max_lateness
    
    duration, deadline, idx = tasks[current_index]
    ft = current_time + duration
    current_lateness = max(0, ft-deadline)
    new_max_lateness = max(max_lateness, current_lateness)
    
    return opt(tasks, ft, new_max_lateness, current_index+1)

def main_program():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    
    while True:
        try:
            line = next(it)
            n = int(line)
            durations = [int(next(it)) for a in range(n)]
            deadlines = [int(next(it)) for b in range(n)]
            
            tasks = []
            for i in range(n):
                tasks.append((durations[i], deadlines[i], i+1))

            tasks.sort(key=lambda x: (x[1], x[2]))
            max_L = opt(tasks, 0, 0, 0)
            sequence = [job[2] for job in tasks]
            print(max_L)
            print(*(sequence))
            
        except (StopIteration, ValueError):
            break

if __name__ == "__main__":
    main_program()
 