# operaciones con matrices utilizando numpy

import numpy as np

matriz_A = [ [1,2,3],
            [4,5,6],
            [7,8,9]]

matriz_B = [ [1,2,3],
            [4,5,6],
            [7,8,9]]

# suma de matrices
suma = np.add(matriz_A, matriz_B)
print("Suma de matrices:\n", suma)

# multiplicación de matrices
multiplicacion = np.dot(matriz_A, matriz_B)
print("Multiplicación de matrices:\n", multiplicacion)

# producto punto (elemento a elemento)
vectorE = np.array([1,2,3])
resultado = np.dot(matriz_A, vectorE)
print("Producto punto de matriz_A con vectorE:\n", resultado)