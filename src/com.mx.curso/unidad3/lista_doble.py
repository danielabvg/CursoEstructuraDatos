class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.previo = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None  # Para insertar al final en O(1)

    def insertar_al_inicio(self, dato):  # O(1)
        nuevo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.previo = nuevo
            self.cabeza = nuevo

    def insertar_al_final(self, dato):  # O(1)
        nuevo = NodoDoble(dato)
        if self.cola is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.previo = self.cola
            self.cola = nuevo
