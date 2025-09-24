# limpieza de datos con numpy

import numpy as np

# simular una matriz de datos 5 * 5

np.random.seed(5,5) * 100
datos = np.random.rand(5,5) * 100

# simular datos erroneos

datos[0,0] = -99
datos[2,3] = 1000

print("Datos originales:")
print(datos)

indices_erroneos = [0,2]

datos_limpios = np.delete(datos, indices_erroneos, axis = 0)
print("\nDatos limpios:")
print(datos_limpios)



