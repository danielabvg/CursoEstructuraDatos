# MergeSort: Fusión de dos listas ordenadas

modelo1 = [1, 5, 10, 20, 25, 30, 35, 40, 45, 50]
modelo2 = [2, 6, 15, 22, 28, 33, 38, 42, 48, 55]
fusion = []

i = j = 0
while i < len(modelo1) and j < len(modelo2):
    if modelo1[i] < modelo2[j]:
        fusion.append(modelo1[i])
        i += 1
    else:
        fusion.append(modelo2[j])
        j += 1

fusion.extend(modelo1[i:])
fusion.extend(modelo2[j:])

print("Lista combinada:", fusion)
