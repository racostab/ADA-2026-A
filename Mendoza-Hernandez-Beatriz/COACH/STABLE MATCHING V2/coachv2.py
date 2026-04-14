def gs(P,R):
    f=list(P);e={};c={p:0 for p in P}
    rk={r:{x:i for i,x in enumerate(R[r])}for r in R}
    while f:
        p=f[0];r=P[p][c[p]];c[p]+=1
        if r not in e:e[r]=p;f.pop(0)
        else:
            q=e[r]
            if rk[r][p]<rk[r][q]:e[r]=p;f.pop(0);f.append(q)
            else:f.append(f.pop(0))
    return e

n,f=input().split();n=int(n)
mp,wp={},{}
for _ in range(n):
 d=input().split();mp[d[0]]=d[1:]
for _ in range(n):
 d=input().split();wp[d[0]]=d[1:]

if f=='m':
 e=gs(mp,wp);m={v:k for k,v in e.items()}
 for x in sorted(mp):print(x,m[x])
else:
 e=gs(wp,mp);m={v:k for k,v in e.items()}
 for x in sorted(wp):print(x,m[x])