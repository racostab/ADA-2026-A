for a in range(1,1000):
    for b in range(a+1,1000):
        c=1000-a-b
        
        if b<c and a*a + b*b == c*c:
            producto=a*b*c
            print(producto)