# Ejercicio 5: Sistema de Recomendación de Películas con Matrices

# Ejemplo de matriz con 3 usuarios y 4 películas
matriz = [
    [5, 4, 3, 2],
    [4, 5, 4, 3],
    [3, 2, 5, 4]
]

print("Matriz de calificaciones:")
for fila in matriz:
    print(fila)

# Promedio de una película específica
pelicula = int(input("Ingresa el número de la película (0-3): "))
promedio = sum(matriz[i][pelicula] for i in range(len(matriz))) / len(matriz)
print("Promedio de la película", pelicula, ":", promedio)

# Calificaciones de un usuario específico
usuario = int(input("Ingresa el número del usuario (0-2): "))
print("Calificaciones del usuario", usuario, ":", matriz[usuario])
