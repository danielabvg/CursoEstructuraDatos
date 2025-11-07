# Lista de productos con su puntuación de relevancia
productos = [
    ("Audífonos", 4.5),
    ("Laptop", 8.7),
    ("Mouse", 3.2),
    ("Teclado", 6.0),
    ("Monitor", 7.3)
]

# Ordenamiento por selección (de menor a mayor puntuación)
for i in range(len(productos)):
    min_index = i  # asumir que el primer elemento es el menor
    
    # buscar el menor en el resto de la lista
    for j in range(i + 1, len(productos)):
        if productos[j][1] < productos[min_index][1]:
            min_index = j
    
    # intercambiar el elemento actual con el menor encontrado
    productos[i], productos[min_index] = productos[min_index], productos[i]

# Resultado
print("Productos ordenados de menor a mayor relevancia:")
for producto, puntuacion in productos:
    print(f"{producto}: {puntuacion}")
