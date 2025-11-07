def revertir_cadena(cadena):
    # Caso base: cadena vacía
    if len(cadena) == 0:
        return ""
    # Llamada recursiva: invertir el resto y añadir el primer carácter al final
    return revertir_cadena(cadena[1:]) + cadena[0]

# Ejemplo de uso
texto = "IA_es_genial"
texto_revertido = revertir_cadena(texto)
print("Texto original:", texto)
print("Texto revertido:", texto_revertido)
