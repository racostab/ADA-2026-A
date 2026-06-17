test_cases = []
while True:
    try:
        user_input = input()
        if not user_input.strip():
            continue
        num_jobs = int(user_input.strip())
        tc = []
        for _ in range(num_jobs):
            job_input = input()
            tc.append(list(map(int, job_input.split())))
        test_cases.append(tc)
    except EOFError:
        break

def buscar_binaria(finish_times, st, n):
    low = 0
    high = n - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if finish_times[mid] <= st:
            ans = mid + 1
            low = mid + 1
        else:
            high = mid - 1
    return ans

def trabajos(lista_trabajos):
    trabajos_lista = []
    for i in range(len(lista_trabajos)):
        st = lista_trabajos[i][0]
        ft = lista_trabajos[i][1]
        pro = lista_trabajos[i][2]
        trabajos_lista.append((st, ft, pro, i + 1))
        
    trabajos_lista.sort(key=lambda x: x[1])
    finish_times = [t[1] for t in trabajos_lista]
    
    num_jobs = len(trabajos_lista)
    dp = [0] * (num_jobs + 1)
    eleccion = [False] * (num_jobs + 1)
    prev_job = [0] * (num_jobs + 1)
    
    for i in range(1, num_jobs + 1):
        st = trabajos_lista[i - 1][0]
        pro = trabajos_lista[i - 1][2]
        
        mejor_previo = buscar_binaria(finish_times, st, i - 1)
        prev_job[i] = mejor_previo
        
        if dp[mejor_previo] + pro > dp[i - 1]:
            dp[i] = dp[mejor_previo] + pro
            eleccion[i] = True
        else:
            dp[i] = dp[i - 1]
            eleccion[i] = False
            
    ganancia_maxima = dp[num_jobs]
    curr = num_jobs
    lista_ordenada = []
    
    while curr > 0:
        if eleccion[curr]:
            lista_ordenada.append(trabajos_lista[curr - 1][3])
            curr = prev_job[curr]
        else:
            curr -= 1
            
    lista_ordenada.sort()
    return ganancia_maxima, lista_ordenada

for tc in test_cases:
    ganancia, lista = trabajos(tc)
    print(ganancia)
    if lista:
        print(" ".join(map(str, lista)))
    else:
        print()