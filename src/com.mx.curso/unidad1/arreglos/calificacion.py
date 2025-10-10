# Pregunta cuántos estudiantes hay
num_estudiantes = int(input("Número de estudiantes: "))

# Crea una lista vacía para guardar las calificaciones
calificaciones = []

# Pide la calificación de cada estudiante
for i in range(num_estudiantes):
    # Ingresa la calificación y la convierte a número decimal
    valor = float(input(f"Ingresar calificación del estudiante {i+1}: "))
    # Agrega la calificación a la lista
    calificaciones.append(valor)

# Muestra todas las calificaciones del grupo
print("\nCalificaciones del grupo:", calificaciones)

# Pregunta qué estudiante quieres consultar usando su índice
# Los índices van de 0 al número de estudiantes - 1
indice = int(input("Ingrese el índice del estudiante a consultar (0 a {}): ".format(num_estudiantes-1)))
# Muestra la calificación del estudiante elegido
print(f"Calificación del estudiante {indice}: {calificaciones[indice]}")

# Pregunta si quieres cambiar alguna calificación
modificar = input("¿Desea modificar alguna calificación? (s/n): ").lower()
if modificar == "s":
    # Pide el índice del estudiante que quieres cambiar
    indice_mod = int(input("Ingrese el índice del estudiante a modificar: "))
    # Pide la nueva calificación
    nuevo_valor = float(input("Ingrese la nueva calificación: "))
    # Actualiza la calificación en la lista
    calificaciones[indice_mod] = nuevo_valor
    # Muestra las calificaciones actualizadas
    print("Calificaciones actualizadas:", calificaciones)

# Calcula el promedio sumando todas las calificaciones y dividiendo entre el total
promedio = sum(calificaciones) / len(calificaciones)
# Muestra el promedio general del grupo
print(f"Promedio general del grupo: {promedio:.2f}")
