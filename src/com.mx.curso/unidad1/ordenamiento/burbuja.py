# Ordenamiento de Burbuja: Clasificación de Muestras de Spam

puntuaciones = [45, 12, 67, 23, 89, 34, 56, 10, 78, 50]
print("Puntuaciones originales:", puntuaciones)

n = len(puntuaciones)
for i in range(n - 1):
    for j in range(n - i - 1):
        if puntuaciones[j] > puntuaciones[j + 1]:
            # Intercambio
            puntuaciones[j], puntuaciones[j + 1] = puntuaciones[j + 1], puntuaciones[j]
            print(f"Intercambio: {puntuaciones}")

print("Puntuaciones ordenadas:", puntuaciones)
