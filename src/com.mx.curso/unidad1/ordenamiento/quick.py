# QuickSort: Ordenar por similaridad

import random

puntuaciones = [random.randint(1, 100) for _ in range(10)]
print("Puntuaciones originales:", puntuaciones)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x > pivote]
    menores = [x for x in lista[1:] if x <= pivote]
    return quicksort(mayores) + [pivote] + quicksort(menores)

ordenadas = quicksort(puntuaciones)
print("Puntuaciones ordenadas de mayor a menor:", ordenadas)
