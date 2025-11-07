# Determinar si una fruta es una manzana
# Implementar preguntas ¿es roja? y ¿es redonda?
# Implementar función recursiva es_manzana
# Se debe identificar el caso base (cuando la fruta es o no es una manzana) y el caso recursivo (cuando se hace la siguiente pregunta)

def es_manzana(paso=1):
    # Caso base 1: preguntar si es roja
    if paso == 1:
        es_roja = input("¿La fruta es roja? (S/N): ").strip().upper()
        if es_roja == "S":
            # Caso recursivo: pasar al paso 2
            return es_manzana(paso + 1)
        else:
            print("No es manzana.")
            return False

    # Caso base 2: preguntar si es redonda
    elif paso == 2:
        es_redonda = input("¿La fruta es redonda? (S/N): ").strip().upper()
        if es_redonda == "S":
            print("¡Tu fruta es una manzana!")
            return True
        else:
            print("No es manzana.")
            return False


# Llamar a la función principal
es_manzana()
