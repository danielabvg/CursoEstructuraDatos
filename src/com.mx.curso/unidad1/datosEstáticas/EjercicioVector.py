# Crea un arreglo que represente un vector de características de un objeto (por ejemplo; altura, peso, edad)

# Vector de características: [altura(m), peso(kg), edad(años)]
vector = [1.70, 65.0, 22]

# Mostrar vector inicial
print("Vector inicial:", vector)

# Acceso a un elemento (por índice)
indice = int(input("Ingrese el índice del elemento a acceder (0=altura, 1=peso, 2=edad): "))
print(f"Elemento en índice {indice}: {vector[indice]}")

# Modificación de un valor
nuevo_valor = float(input(f"Ingrese el nuevo valor para el índice {indice}: "))
vector[indice] = nuevo_valor
print("Vector modificado:", vector)

# Cálculo de la media
media = sum(vector) / len(vector)
print("Media de los elementos:", media)
