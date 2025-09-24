#Análisis de complejidad de algoritmos

import time

def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

starTime = time.time()
endTime = time.time()
mi_lista = [1,2,3,4,5]
elemento = 5
encontrado = buscar_elemento(mi_lista, elemento)

if encontrado:
    print("El elemento {elemento} fue encontrado en la lista.")
else:
    print("El elemento {elemento} no fue encontrado en la lista.")

print(f"Tiempo de ejecución: {endTime - starTime} segundos")