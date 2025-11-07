#  Implementar una función recursiva que imprima los pasos necesarios para mover una torre 
#  de N discos de un poste de origen a un poste de destino, usando un poste auxiliar.
#  La solución debe mostrar el pensamiento recursivo al descomponer el problema en subproblemas más pequeños, como mover sólo un disco.

def imprimir_hanoi(n, origen="A", destino="C", auxiliar="B"):
    """
    Imprime los pasos para mover n discos de 'origen' a 'destino' usando 'auxiliar'.
    Además muestra el "pensamiento" recursivo: indica cuándo se descompone el problema
    y cuándo se ejecuta el caso base (mover un único disco).
    """
    # contador en lista para poder modificarlo desde la función interna
    contador = [1]

    def _hanoi(k, o, d, a, profundidad):
        indent = "    " * profundidad  # sangría para visualizar recursión
        if k == 0:
            # No hay discos que mover 
            print(f"{indent}No hay discos que mover (k=0).")
            return

        if k == 1:
            # Caso base: mover un disco directamente de origen a destino
            print(f"{indent}Caso base: mover 1 disco de {o} -> {d} (mov {contador[0]})")
            contador[0] += 1
            return

        # Paso recursivo: explicar la descomposición del problema
        print(f"{indent}Para mover {k} discos de {o} a {d}:")
        print(f"{indent}  1) Mover {k-1} discos de {o} a {a} usando {d}.")
        _hanoi(k-1, o, a, d, profundidad + 1)

        # Mover el disco más grande (k) al destino
        print(f"{indent}  2) Mover disco {k} de {o} -> {d} (mov {contador[0]}).")
        contador[0] += 1

        # Última parte: mover los k-1 discos desde auxiliar al destino
        print(f"{indent}  3) Mover {k-1} discos de {a} a {d} usando {o}.")
        _hanoi(k-1, a, d, o, profundidad + 1)

    # Llamamos al procedimiento recursivo principal
    _hanoi(n, origen, destino, auxiliar, profundidad=0)
    print(f"Total de movimientos: {contador[0] - 1}")

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        n = int(input("¿Cuántos discos quieres mover? Ingresa un entero positivo: ").strip())
        if n < 0:
            raise ValueError("Número negativo")
    except ValueError:
        print("Por favor ingresa un número entero positivo.")
    else:
        imprimir_hanoi(n, origen="A", destino="C", auxiliar="B")
