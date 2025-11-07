import numpy as np
import pandas as pd

# 1. Cargar datos en una matriz numpy (tipo float)
file_path = '/mnt/data/processed.cleveland.data'
data = np.loadtxt(file_path, delimiter=',', dtype=float)

# Copia de la matriz original
data_original = data.copy()

# 2. Introducir valores np.nan en dos posiciones aleatorias
np.random.seed(42)  # para reproducibilidad
rows, cols = data.shape
rand_positions = [(np.random.randint(0, rows), np.random.randint(0, cols)) for _ in range(2)]
for r, c in rand_positions:
    data[r, c] = np.nan

print("Posiciones con np.nan introducidas:", rand_positions)

# 3. Identificar valores faltantes
missing_positions = np.argwhere(np.isnan(data))
print("\nValores faltantes en posiciones:\n", missing_positions)

# 4. Reemplazar np.nan por la mediana de la columna correspondiente
for col in range(cols):
    col_data = data[:, col]
    if np.isnan(col_data).any():
        median_value = np.nanmedian(col_data)
        col_data[np.isnan(col_data)] = median_value
        data[:, col] = col_data

# 5. Análisis descriptivo antes y después de la limpieza
def descriptive_stats(matrix):
    df = pd.DataFrame(matrix)
    stats = pd.DataFrame({
        'Media': df.mean(),
        'Mediana': df.median(),
        'Desv. Estándar': df.std()
    })
    return stats

stats_before = descriptive_stats(data_original)
stats_after = descriptive_stats(data)

print("\n--- Estadísticas antes de limpieza ---")
print(stats_before)

print("\n--- Estadísticas después de limpieza ---")
print(stats_after)
