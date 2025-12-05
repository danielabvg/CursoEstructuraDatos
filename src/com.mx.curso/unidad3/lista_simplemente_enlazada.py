class Nodo:
    def __init__(self, precision, error):
        self.precision = precision
        self.error = error
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, precision, error):
        nuevo = Nodo(precision, error)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(f"Precisión: {actual.precision}, Error: {actual.error}")
            actual = actual.siguiente

    def buscar(self, precision):
        actual = self.cabeza
        while actual:
            if actual.precision == precision:
                return actual
            actual = actual.siguiente
        return None

# Ejemplo de uso
historial = ListaEnlazada()
historial.agregar(0.80, 0.30)
historial.agregar(0.85, 0.25)
historial.agregar(0.90, 0.20)

historial.imprimir()
resultado = historial.buscar(0.85)
if resultado:
    print("Métrica encontrada:", resultado.precision, resultado.error)