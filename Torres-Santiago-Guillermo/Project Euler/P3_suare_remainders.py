# -------------------- Residuo maximo ------------------
def r_max(a):
    max_r = 0
    mod = a*a
    
    for n in range(1, 2*a+1):
        r = (pow(a-1, n, mod) + pow(a+1, n, mod)) % mod
        if r > max_r:
            max_r = r
    return max_r

#------------------------ MAIN -------------------------
suma = 0
for a in range(3,1000+1):
    suma += r_max(a)
print(suma)
