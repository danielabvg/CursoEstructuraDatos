import numpy as np
import time

# Matriz de pesos 3x2
pesos = np.array([[0.2, 0.7],
                  [0.5, 0.1],
                  [0.9, 0.4]])

# Vector de entrada
entrada = []
print("Ingresa 3 valores para el vector de entrada:")
for i in range(3):
    valor = float(input(f"Elemento {i+1}: "))
    entrada.append(valor)

entrada = np.array(entrada)

# --- Producto punto con numpy ---
inicio_numpy = time.time()  # tiempo inicial
salida_numpy = np.dot(entrada, pesos)
fin_numpy = time.time()     # tiempo final
tiempo_numpy = fin_numpy - inicio_numpy

print("\nVector de salida con numpy.dot:")
print(salida_numpy)
print(f"Tiempo de ejecución: {tiempo_numpy:.10f} segundos")

# --- Producto punto manual ---
inicio_manual = time.time()  # tiempo inicial

# Inicializar vector de salida con ceros
salida_manual = [0, 0]  # 2 neuronas de salida

# Calcular producto punto manualmente
for j in range(2):            # Para cada neurona de salida
    for i in range(3):        # Para cada neurona de entrada
        salida_manual[j] += entrada[i] * pesos[i][j]

fin_manual = time.time()       # tiempo final
tiempo_manual = fin_manual - inicio_manual

print("\nVector de salida calculado manualmente:")
print(salida_manual)
print(f"Tiempo de ejecución: {tiempo_manual:.10f} segundos")
