# Ejercicio: Registro de temperaturas
# Matriz que almacene las temperaturas en una ciudad 3x3
# Imprimir la matriz completa
# Consultar la intensidad en una posición específica
# Modificar su valor
# Calcular el promedio general de iluminación en la cuadrícula (matriz)

matriz = []

# Llenar la matriz 3x3
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese valor para celda ({i},{j}): "))
        fila.append(float(valor))
    matriz.append(fila)

# Imprimir la matriz completa
print("\nMatriz de temperaturas:")
for fila in matriz:
    print(fila)


# Acceso a un elemento (por índice)
indicef = int(input("\nIngrese el índice de la fila a acceder: "))
indicec = int(input("Ingrese el índice de la columna a acceder: "))
print(f"Elemento en posición ({indicef}, {indicec}): {matriz[indicef][indicec]}")

# Modificación de un valor
nuevo_valor = int(input(f"Ingrese el nuevo valor para ({indicef}, {indicec}): "))
matriz[indicef][indicec] = nuevo_valor
print("\nMatriz modificada:")
for fila in matriz:
    print(fila)


