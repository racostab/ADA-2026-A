# Array
# En Python no existe un “array” real como en C; lo que se usa son listas.
# Cada elemento es un objeto independiente → sobrecarga alta.
#
print("Ejemplos de Array")

data = ['apple', 'banana', 'cherry']
data.append("orange")
print("Data: {}".format(data))

data2 = ["Ford", "BMW", "Volvo"]
data.append(data2)
print("Data: {}".format(data))
      
data.clear()
print("Data: {}".format(data))

data = [2] * 5
print("Data: {}".format(data))

data = []
print("Data: {}".format(data))

D1 = [1,2,3]
print("D1: {}".format(D1))

D2 = [[1,2,3],[4,5,6],[7,8,9]]
print("D2: {}".format(D2))

D3 = [
  [ [1,2,3],[4,5,6],[7,8,9] ],
  [ [10,11,12],[13,14,15],[16,17,18] ],
  [ [19,20,21],[22,23,24],[25,26,27] ],
]
print("D3: {}".format(D3))

print("D3: {}".format(D3[1][1][1]))