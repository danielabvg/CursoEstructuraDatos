from collections import deque

cola = deque()
cola.append("Analizar texto 1")
cola.append("Analizar texto 2")
cola.append("Analizar texto 3")

while cola:
    tarea = cola.popleft()
    print("Procesando:", tarea)