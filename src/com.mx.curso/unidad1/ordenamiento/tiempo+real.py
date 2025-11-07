# Ordenamiento por Inserción: Lecturas en tiempo real

lecturas = [12, 25, 40, 55, 70]
nueva_lectura = 35
print("Lecturas originales:", lecturas)
print("Nueva lectura:", nueva_lectura)

# Insertar manteniendo orden
i = len(lecturas) - 1
lecturas.append(nueva_lectura)
while i >= 0 and lecturas[i] > nueva_lectura:
    lecturas[i + 1] = lecturas[i]
    i -= 1
lecturas[i + 1] = nueva_lectura

print("Lecturas ordenadas:", lecturas)
