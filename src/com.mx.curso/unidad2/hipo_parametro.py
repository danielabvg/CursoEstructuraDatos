def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio  # Elemento encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Elemento no encontrado

# Ejemplo de uso: búsqueda de un hiperparámetro óptimo
hiperparametros = [0.001, 0.01, 0.1, 0.2, 0.3, 0.5, 1.0]  # Lista ordenada
valor_objetivo = 0.2

indice = busqueda_binaria(hiperparametros, valor_objetivo)

if indice != -1:
    print(f"Hiperparámetro óptimo encontrado: {hiperparametros[indice]} en la posición {indice}")
else:
    print("Hiperparámetro no encontrado")
