# Array
# Un ndarray es un arreglo numérico homogéneo implementado en C.
# Características
#	Todos los elementos del mismo tipo
#	Memoria contigua
#	Operaciones vectorizadas
#	Muchísimo más rápido
print("Ejemplos con NumPy")

# pip install numpy
import numpy as np

#data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
data = np.array([[1, 2, 3], [4, 5, 6]])
#type(data)
print( type(data) )

print("data: {}".format(data))

data = np.zeros((2, 3))
print("data: {}".format(data))
data = np.ones((2, 3))
print("data: {}".format(data))
data = np.random.rand(2, 3)
print("data: {}".format(data))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
# array([5, 7, 9])
