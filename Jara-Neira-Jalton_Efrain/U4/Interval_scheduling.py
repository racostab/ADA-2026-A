# Author: Jalton Efrain Jara Neira
# Date: 10/05/2026 
import sys
sys.setrecursionlimit(5000)

def opt(tasks, last_ft, current_index, result):
    if current_index >= len(tasks):
        return
    st, ft, idx = tasks[current_index]

    if st >= last_ft:
        result.append(idx)
        opt(tasks, ft, current_index+1, result)
    else:
        opt(tasks, last_ft, current_index+1, result)

def main_program():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    
    while True:
        try:
            line = next(it)
            n = int(line)
            start_times = [int(next(it)) for a in range(n)]
            finish_times = [int(next(it)) for b in range(n)]
            
            tasks = []
            for i in range(n):
                tasks.append((start_times[i], finish_times[i], i+1))
            tasks.sort(key=lambda x: x[1])
            
            solution_ids = []
            opt(tasks, 0, 0, solution_ids)
            solution_ids.sort()
            print(len(solution_ids))
            print(*(solution_ids))
            
        except (StopIteration, ValueError):
            break

if __name__ == "__main__":
    main_program()