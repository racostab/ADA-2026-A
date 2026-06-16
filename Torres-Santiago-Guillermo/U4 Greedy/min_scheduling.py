def plan_inter():
    jobs = sorted(req, key=lambda x: x[2])
    plan = []

    t = 0
    lat_max = 0

    for i in range(n_jobs):
        t_i = t
        t_f = t + jobs[i][1]
        t += jobs[i][1]
        plan.append((jobs[i][0],t_i,t_f))
        lat = t_f - jobs[i][2]
        if lat >= lat_max:
            lat_max = lat

    return plan,lat_max


n_jobs = int(input())
t_j = list(map(int,input().split()))
d_j = list(map(int,input().split()))

req = []
for n in range(n_jobs):
     req.append((n+1,t_j[n],d_j[n]))

plan_f,lat_max = plan_inter()

print(lat_max)
for p in range(n_jobs):
        if p == n_jobs-1:
            print(f"{plan_f[p][0]}")
        else:
            print(f"{plan_f[p][0]}", end=" ")
