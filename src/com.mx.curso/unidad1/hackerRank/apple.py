# Datos de entrada:
# s y t → inicio y fin de la casa de Sam.
# a → posición del manzano.
# b → posición del naranjo.
# m → cantidad de manzanas.
# n → cantidad de naranjas.
# Lista con distancias de las manzanas.
# Lista con distancias de las naranjas.
# Cómo calcular la posición real donde cae la fruta:
# Para cada manzana: posición final = a + distancia.
# Para cada naranja: posición final = b + distancia.
# Contar cuántas caen dentro de la casa: Revisar si la posición final está en el rango [s, t].

def countApplesAndOranges():
    print("=== PROGRAMA: Contar manzanas y naranjas ===")

    # Rango de la casa de Sam
    s = int(input("Ingresa el inicio de la casa de Sam (s): "))
    t = int(input("Ingresa el final de la casa de Sam (t): "))

    # Posición de los árboles
    a = int(input("Ingresa la posición del manzano (a): "))
    b = int(input("Ingresa la posición del naranjo (b): "))

    # Cantidad de frutas
    m = int(input("Ingresa cuántas manzanas hay (m): "))
    n = int(input("Ingresa cuántas naranjas hay (n): "))

    # Distancias de las manzanas
    apples = []
    print("=== Distancias de las manzanas ===")
    for i in range(m):
        valor = int(input(f"Distancia de la manzana {i+1}: "))
        apples.append(valor)

    # Distancias de las naranjas
    oranges = []
    print("=== Distancias de las naranjas ===")
    for j in range(n):
        valor = int(input(f"Distancia de la naranja {j+1}: "))
        oranges.append(valor)

    # Contar cuántas caen en la casa
    count_apples = sum(1 for d in apples if s <= a + d <= t)
    count_oranges = sum(1 for d in oranges if s <= b + d <= t)

    # Resultados
    print("===================================")
    print("Manzanas que cayeron en la casa:", count_apples)
    print("Naranjas que cayeron en la casa:", count_oranges)


# Llamar la función
countApplesAndOranges()

