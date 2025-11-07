# MergeSort con visualización paso a paso

def merge_sort_visual(lista, nivel=0):
    print("  " * nivel + f"Dividiendo: {lista}")
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort_visual(lista[:medio], nivel + 1)
    der = merge_sort_visual(lista[medio:], nivel + 1)
    
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
    print("  " * nivel + f"Fusionando: {fusion}")
    return fusion

# Lista de ejemplo
lista = [8, 3, 7, 4, 9, 2, 6, 5]
resultado = merge_sort_visual(lista)
print("Resultado final:", resultado)
