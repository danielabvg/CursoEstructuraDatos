# Ejercicio 7: Tablero de Juego con Matriz

tablero = []
for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Ingrese valor para celda ({i},{j}) [0 o 1]: "))
        fila.append(valor)
    tablero.append(fila)

print("Tablero de juego:")
for fila in tablero:
    print(fila)

# Conteo de obstáculos
total_obstaculos = sum(sum(fila) for fila in tablero)
print("Total de obstáculos:", total_obstaculos)

fila_usuario = int(input("Ingrese el número de la fila a analizar (0-4): "))
print("Obstáculos en la fila", fila_usuario, ":", sum(tablero[fila_usuario]))
