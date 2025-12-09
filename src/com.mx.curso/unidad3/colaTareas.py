from collections import deque

cola = deque()

cola.append("Entrenar modelo A")
cola.append("Entrenar modelo B")
cola.append("Entrenar modelo C")

while cola:
    print("Procesando:", cola.popleft())
