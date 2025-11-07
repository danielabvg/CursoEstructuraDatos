# Lista de puntuaciones de comentarios 
puntuaciones = [0.8, -0.3, 0.1, -0.9, 0.5, -0.1, 0.9, -0.6]

# Implementación de QuickSort (ordenar de menor a mayor)
def quicksort(lista):
    if len(lista) <= 1:     # Caso base: ya está ordenada
        return lista
    
    pivote = lista[len(lista) // 2]  # Elegir el elemento central como pivote
    
    menores = [x for x in lista if x < pivote]     # valores menores al pivote
    iguales = [x for x in lista if x == pivote]    # valores iguales al pivote
    mayores = [x for x in lista if x > pivote]     # valores mayores al pivote
    
    # Ordenar recursivamente y unir resultados 
    return quicksort(menores) + iguales + quicksort(mayores)


# Ordenar la lista
puntuaciones_ordenadas = quicksort(puntuaciones)

# Resultado
print("Puntuaciones ordenadas de menor a mayor (negativo → positivo):")
print(puntuaciones_ordenadas)
