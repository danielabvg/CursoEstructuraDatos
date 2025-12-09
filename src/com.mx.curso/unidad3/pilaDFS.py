pila = []

pila.append("A")
pila.append("B")
pila.append("C")

print("Procesando DFS:")
while pila:
    nodo = pila.pop()
    print("Visitando:", nodo)
