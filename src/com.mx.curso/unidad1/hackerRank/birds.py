# Given an array of bird sightings where every element represents a bird type id, 
# determine the id of the most frequently sighted type. 
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

def migratoryBirds():
    print("=== PROGRAMA: Identificar el ave más vista ===")

    # Cantidad de avistamientos
    n = int(input("Ingresa el número total de avistamientos: "))

    # Lista de aves vistas
    print("Ingresa los IDs de las aves (separados por espacio):")
    arr = list(map(int, input().split()))

    # Contar frecuencias
    counts = {}
    for bird in arr:
        counts[bird] = counts.get(bird, 0) + 1

    # Máxima frecuencia
    max_freq = max(counts.values())

    # Filtrar las aves con esa frecuencia máxima
    candidates = [bird for bird, freq in counts.items() if freq == max_freq]

    # Elegir la de menor ID
    result = min(candidates)

    # Resultado final
    print("===================================")
    print("El ID del ave más frecuente es:", result)


# Llamar a la función
migratoryBirds()
