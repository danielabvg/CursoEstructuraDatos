import numpy as np

# Vector de entrada
entrada = np.array([1.0, 2.0, 3.0])

# Matriz de pesos (3x2)
pesos = np.array([[0.2, 0.8],
                  [0.5, 0.1],
                  [0.9, 0.4]])

# Producto punto para obtener la salida
salida = np.dot(entrada, pesos)

# Mostrar resultado
print("Valores de salida:", salida)
