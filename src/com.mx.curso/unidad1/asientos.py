# Ejercicio 3 - Mapa de Asientos de un Cine

# Matriz 4x5 con asientos libres (0)
cine = [[0 for _ in range(5)] for _ in range(4)]

# Mostrar mapa inicial
print("Mapa de asientos (0=libre, 1=ocupado):")
for fila in cine:
    print(fila)

# Pedir asiento al usuario
fila = int(input("\nIngrese la fila (0-3): "))
col = int(input("Ingrese el asiento (0-4): "))
cine[fila][col] = 1

# Mostrar mapa actualizado
print("\nMapa actualizado:")
for fila in cine:
    print(fila)

# Contar asientos libres
libres = sum(fila.count(0) for fila in cine)
print(f"\nAsientos libres: {libres}")
