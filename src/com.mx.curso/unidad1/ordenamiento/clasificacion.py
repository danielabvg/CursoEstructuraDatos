# MergeSort + Recomendación top 5

import random

# MergeSort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    fusion = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            fusion.append(izq[i])
            i += 1
        else:
            fusion.append(der[j])
            j += 1
    fusion.extend(izq[i:])
    fusion.extend(der[j:])
    return fusion

# Lista de productos
productos = [random.randint(0, 100) for _ in range(100)]

# Ordenar productos
ordenados = merge_sort(productos)

# Top 5 productos más relevantes
top5 = ordenados[-5:][::-1]
print("Top 5 productos más relevantes:", top5)
