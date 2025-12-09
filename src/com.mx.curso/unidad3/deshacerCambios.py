pila = []

def agregar_cambio(c):
    if len(pila) == 5:
        pila.pop(0)
    pila.append(c)

def deshacer():
    if pila:
        return pila.pop()
    return None

agregar_cambio("Cambio 1")
agregar_cambio("Cambio 2")
agregar_cambio("Cambio 3")
agregar_cambio("Cambio 4")
agregar_cambio("Cambio 5")
agregar_cambio("Cambio 6")  # elimina el 1

print("Deshacer:", deshacer())
