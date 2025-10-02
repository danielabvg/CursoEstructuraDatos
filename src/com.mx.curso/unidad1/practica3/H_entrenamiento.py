# Ejercicio 4: Historial de Entrenamiento de un Modelo

precisiones = []

while True:
    entrada = input("Ingresa la precisión de la época (o escribe 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    try:
        valor = float(entrada)
        precisiones.append(valor)
    except ValueError:
        print("Por favor, ingresa un número válido.")

if len(precisiones) > 0:
    print("Precisión final:", precisiones[-1])
    print("Precisión más alta:", max(precisiones))
else:
    print("No se ingresaron precisiones.")
