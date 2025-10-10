# Ejercicio: Registro de intensidades de luz
# Matriz que almacene las intensidades de luz 4x4
# Imprimir la matriz completa
# Consultar la intensidad en una posición específica
# Modificar su valor
# Calcular el promedio general de iluminación en la cuadrícula (matriz)
# Cambios

matriz = []

# Llenar la matriz 4x4
for i in range(4):
    fila = []
    for j in range(4):
        valor = int(input(f"Ingrese valor para celda ({i},{j}): "))
        fila.append(float(valor))
    matriz.append(fila)

# Imprimir la matriz completa
print("\nMatriz de intensidades:")
for fila in matriz:
    print(fila)

# Calcular promedio general
total = sum(sum(fila) for fila in matriz)
promedio = total / 16
print("\nPromedio general de iluminación:", promedio)

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

# Cálculo de la media nuevamente
total_modificado = sum(sum(fila) for fila in matriz)
media = total_modificado / 16
print("\nNueva media de iluminación:", media)
