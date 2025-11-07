# QuickSort + Búsqueda Binaria

import random

# QuickSort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Búsqueda Binaria
def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Datos de ejemplo
clientes = [random.randint(1000, 2000) for _ in range(500)]
ordenados = quick_sort(clientes)

# Buscar un cliente
objetivo = ordenados[250]
posicion = busqueda_binaria(ordenados, objetivo)
print(f"Cliente {objetivo} encontrado en posición {posicion}")
