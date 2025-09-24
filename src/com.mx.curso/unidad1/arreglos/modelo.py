# Ejercicio 4: Historial de Entrenamiento de un Modelo

# Crear lista vacía llamada precisiones
precisiones = []

# Mensajes iniciales
print("=== Registro de precisión por época ===")
print("Ingresa la precisión de cada época (escribe 'fin' para terminar)")

# Repetir hasta que el usuario escriba "fin"
while True:
    entrada = input("Precisión: ")   # Leer entrada

    if entrada.lower() == "fin":     # Si entrada = "fin" entonces salir del bucle
        break
    try:
        # Convertir entrada a número
        precision = float(entrada)
        # Agregar número a la lista precisiones
        precisiones.append(precision)
    except ValueError:
        # Si no es válido, mostrar mensaje de error
        print("Ingresa un número válido o 'fin' para terminar.")

# Después de salir del bucle:
# Si la lista precisiones no está vacía
if len(precisiones) > 0:
    # precision_final ← último elemento de la lista
    precision_final = precisiones[-1]
    # precision_maxima ← valor máximo de la lista
    precision_maxima = max(precisiones)

    # Mostrar resultados
    print("\n Resultados del entrenamiento:")
    print(f"➤ Precisión final: {precision_final}")
    print(f"➤ Precisión más alta: {precision_maxima}")
else:
    # Sino, mostrar mensaje de lista vacía
    print("No se registraron precisiones.")
