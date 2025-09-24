# Ejercicio 2 - Inventario de Productos en un Almacén

# Matriz: [ID, cantidad, precio]
inventario = [
    [101, 50, 20],   # Producto 1
    [102, 30, 15],   # Producto 2
    [103, 20, 40]    # Producto 3
]

# Mostrar inventario
print("Inventario:")
for fila in inventario:
    print(f"ID: {fila[0]}, Cantidad: {fila[1]}, Precio: ${fila[2]}")

# Calcular valor total del producto 2 (índice 1)
cantidad = inventario[1][1]
precio = inventario[1][2]
valor_total = cantidad * precio
print(f"\nValor total del producto 2: ${valor_total}")

# Actualizar stock después de vender 10
inventario[1][1] -= 10
print(f"Nuevo stock del producto 2: {inventario[1][1]}")
