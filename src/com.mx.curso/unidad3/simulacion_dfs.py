class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

pila = Pila()
pila.push("Nodo A")
pila.push("Nodo B")
pila.push("Nodo C")

print(pila.pop())
print(pila.pop())
print(pila.pop())