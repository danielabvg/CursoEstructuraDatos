# Lista de alertas con valores de riesgo entre 0 y 1

alertas = [0.7, 0.3, 0.9, 0.4, 0.1, 0.8, 0.6, 0.2, 0.95, 0.5]

print(f'Alertas originales: {alertas}')

# Algoritmo Selection sort

for i in range(len(alertas)):
    max_index = i
    for j in range(i + 1, len(alertas)):
        if alertas[j] > alertas[max_index]:
            max_index = j
    alertas[i], alertas[max_index] = alertas[max_index], alertas[i]

print(f'Alertas ordenadas de mayor a menor riesgo: {alertas}')
