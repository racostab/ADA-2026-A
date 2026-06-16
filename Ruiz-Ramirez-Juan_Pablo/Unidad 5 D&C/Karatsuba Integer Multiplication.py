def MULTIPLY_KARATSUBA(x, y, n): 
   if n <= 1 or x == 0 or y == 0:
    return x * y 
   else: 
      m = n // 2 
      a,b = x // 2**m, x %  2**m 
      c,d = y // 2**m, y %  2**m

      e = MULTIPLY_KARATSUBA(a, c, m) # 1. Calcula ac 
      f = MULTIPLY_KARATSUBA(b, d, m) # 2. Calcula bd

      ab = a + b
      cd = c + d
      np = max(ab.bit_length(), cd.bit_length())
      p = MULTIPLY_KARATSUBA(ab, cd, np)

      k = p - e - f # Truco: equivale a (ad + bc)
      return 2**(2*m) * e + 2**m * k + f
   
n = int(input())
for _ in range(n): 
   x_bin, y_bin = input().replace("_"," ").split()
   x = int(x_bin, 2) 
   y = int(y_bin, 2) 
   bits = max(x.bit_length(), y.bit_length())
   resultado = MULTIPLY_KARATSUBA(x, y, bits)
   print(bin(resultado)[2:])

#EJERCICIO APROBADO POR COUCH