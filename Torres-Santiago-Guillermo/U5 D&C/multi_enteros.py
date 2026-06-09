def mult(X, Y):
    n = max(len(X), len(Y))
    X = X.zfill(n)
    Y = Y.zfill(n)

    if n == 1: 
        return int(X[0])*int(Y[0])

    m = n//2
    m2 = n - m  

    a = X[:m]
    b = X[m:]
    c = Y[:m]
    d = Y[m:]

    e = mult(a,c)
    f = mult(b,d)
    g = mult(str(bin(int(a,2) + int(b,2))[2:]), str(bin(int(c,2) + int(d,2))[2:]))

    return (1<<(2*m2))*e + (1<<m2)*(g-e-f) + f


n_case = int(input())
datos = [""]*n_case
for i in range(n_case):
    datos[i] = input().split()

#print(datos)
for i in range(n_case):
    print(bin(mult(datos[i][0],datos[i][1]))[2:])
