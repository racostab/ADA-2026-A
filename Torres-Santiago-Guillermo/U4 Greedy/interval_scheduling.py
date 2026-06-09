def plan_inter():
    jobs = sorted(req, key=lambda x: x[2])
    plan = []

    j_1 = jobs[0]
    plan.append(j_1)
    for i in range(1, n_jobs):
        j_a = jobs[i]
        
        if int(j_a[1]) >= int(j_1[2]):
            plan.append(j_a)
            j_1 = j_a

    plan_f = sorted(plan, key=lambda x: x[0])
    return plan_f
    
n_jobs = int(input())
t_i = list(map(int,input().split()))
t_f = list(map(int,input().split()))

req = []
for n in range(n_jobs):
     req.append((n+1,t_i[n],t_f[n]))

plan_f = plan_inter()

n_plan = len(plan_f)
print(n_plan)
for p in range(n_plan):
        if p == n_plan-1:
            print(f"{plan_f[p][0]}")
        else:
            print(f"{plan_f[p][0]}", end=" ")
