import time
import random

def burbuja(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i-1
        while j >= 0 and arr[j] > clave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = clave

tamaños = [100, 1000, 10000]
for n in tamaños:
    datos = [random.randint(0, 10000) for _ in range(n)]
    
    # Burbuja
    copia = datos[:]
    inicio = time.time()
    burbuja(copia)
    fin = time.time()
    print(f"Burbuja {n} elementos: {fin - inicio:.4f}s")
    
    # Inserción
    copia = datos[:]
    inicio = time.time()
    insercion(copia)
    fin = time.time()
    print(f"Inserción {n} elementos: {fin - inicio:.4f}s\n")
