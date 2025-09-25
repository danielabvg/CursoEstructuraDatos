import numpy as np

# Crear un conjunto de datos como matriz NumPy
# Cada fila es un registro y cada columna una característica
# La última columna será la "irrelevante" 

datos = np.array([
    [25, 175, 70, 999],   # [edad, altura, peso, columna irrelevante]
    [30, 180, 80, 999],
    [22, 165, 55, 999],
    [28, 170, 65, 999]
])

print("Matriz original:")
print(datos)

# Eliminar la última columna (índice 3)
# axis=1 indica columnas

datos_limpios = np.delete(datos, 3, axis=1)

print("\nMatriz limpia (columna irrelevante eliminada):")
print(datos_limpios)
