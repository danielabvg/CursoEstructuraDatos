# Crea una función recursiva que calcule y devuelva el enésimo número en la secuencia de Fibonacci
# utiliza un bucle simple para generar e imprimir los primeros 10 números de la serie
# La secuencia de Fibonacci es una sucesión infinita de números donde cada número se obtiene sumando 
# los dos anteriores, comenzando con 0 y 1

def fibonacci(n):
    """
    Calcula recursivamente el enésimo número de la secuencia de Fibonacci.
    Serie: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if n == 0:
        return 0  # Caso base 1
    elif n == 1:
        return 1  # Caso base 2
    else:
        # Caso recursivo: fib(n) = fib(n-1) + fib(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


# Imprimir los primeros 10 números de la serie
print("Primeros 10 números de la serie de Fibonacci:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Permitir al usuario obtener otro número de la serie
try:
    n = int(input("\n¿Quieres saber el valor de F(n)? Ingresa n: "))
    if n < 0:
        print("Por favor, ingresa un número positivo.")
    else:
        print(f"F({n}) = {fibonacci(n)}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")

