"""Implementación de Cola (Queue) en Python usando collections.deque
Justificación: deque permite append y popleft en O(1) garantizado, manteniendo FIFO
con complejidad óptima para ENQUEUE y DEQUEUE.
"""

from collections import deque
from typing import Any, Deque, Optional

class Cola:
    def __init__(self) -> None:
        self._datos: Deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._datos.append(item)

    def dequeue(self) -> Any:
        if not self._datos:
            raise IndexError('dequeue from empty queue')
        return self._datos.popleft()

    def peek(self) -> Optional[Any]:
        return self._datos[0] if self._datos else None

    def is_empty(self) -> bool:
        return len(self._datos) == 0

    def size(self) -> int:
        return len(self._datos)

    def __repr__(self) -> str:
        return f"Cola({list(self._datos)!r})"

# Ejemplo de uso
if __name__ == '__main__':
    q = Cola()
    q.enqueue('x')
    q.enqueue('y')
    print(q.dequeue())
    print(q.peek())