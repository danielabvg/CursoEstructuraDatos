class Nodo:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.siguiente = None

class HistorialChatbot:
    def __init__(self):
        self.cabeza = None

    def agregar(self, mensaje):
        nuevo = Nodo(mensaje)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.siguiente:
                aux = aux.siguiente
            aux.siguiente = nuevo

    def imprimir(self):
        aux = self.cabeza
        print("Historial del chatbot:")
        while aux:
            print("-", aux.mensaje)
            aux = aux.siguiente

# Ejemplo de uso
historial = HistorialChatbot()
historial.agregar("Hola")
historial.agregar("¿Cómo estás?")
historial.agregar("Muy bien, gracias.")
historial.imprimir()
