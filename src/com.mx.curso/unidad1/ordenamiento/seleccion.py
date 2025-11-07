# Ordenamiento por Selección: Selección de Características

caracteristicas = [0.56, 0.89, 0.32, 0.74, 0.65, 0.90, 0.41, 0.77]
print("Importancia original:", caracteristicas)

n = len(caracteristicas)
for i in range(n):
    max_idx = i
    for j in range(i + 1, n):
        if caracteristicas[j] > caracteristicas[max_idx]:
            max_idx = j
    caracteristicas[i], caracteristicas[max_idx] = caracteristicas[max_idx], caracteristicas[i]
    print(f"Selección paso {i+1}: {caracteristicas}")

print("Ordenadas de mayor a menor importancia:", caracteristicas)
