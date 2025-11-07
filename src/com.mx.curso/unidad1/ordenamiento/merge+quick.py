import time
import random

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

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

for n in [1000, 10000]:
    datos = [random.randint(0, 10000) for _ in range(n)]
    
    inicio = time.time()
    merge_sort(datos[:])
    print(f"MergeSort {n}: {time.time() - inicio:.4f}s")
    
    inicio = time.time()
    quick_sort(datos[:])
    print(f"QuickSort {n}: {time.time() - inicio:.4f}s\n")
