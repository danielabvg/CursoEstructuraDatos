class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):  # O(1)
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self, dato):  # O(n)
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo
