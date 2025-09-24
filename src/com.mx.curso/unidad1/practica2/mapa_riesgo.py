# Mapa de riesgo 8x8
mapa = [
    [0, 1, 0, 2, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 2, 0],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [2, 1, 0, 0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 2],
    [1, 0, 0, 2, 0, 0, 1, 0],
    [0, 2, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 2, 0, 0]
]

# Imprimir mapa original
print("Mapa original:")
for fila in mapa:
    print(fila)

# Contadores
precaucion = sum(fila.count(1) for fila in mapa)
alto_riesgo = sum(fila.count(2) for fila in mapa)

print("\nÁreas de precaución:", precaucion)
print("Áreas de alto riesgo:", alto_riesgo)

# Actualizar mapa: cambiar 2 por 1
for i in range(8):
    for j in range(8):
        if mapa[i][j] == 2:
            mapa[i][j] = 1

# Imprimir mapa actualizado
print("\nMapa actualizado:")
for fila in mapa:
    print(fila)
