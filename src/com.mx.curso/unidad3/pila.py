"""Implementación de Pila (Stack) en Python.
Decisión: se utiliza la lista nativa `list` para la pila.
Justificación: `list.append()` y `list.pop()` al final son operaciones amortizadas O(1)
y presentan la implementación más simple y eficiente para LIFO en Python.
"""

from typing import Any, List, Optional

class Pila:
    def __init__(self) -> None:
        self._datos: List[Any] = []

    def push(self, item: Any) -> None:
        self._datos.append(item)

    def pop(self) -> Any:
        if not self._datos:
            raise IndexError('pop from empty stack')
        return self._datos.pop()

    def peek(self) -> Optional[Any]:
        return self._datos[-1] if self._datos else None

    def is_empty(self) -> bool:
        return len(self._datos) == 0

    def size(self) -> int:
        return len(self._datos)

    def __repr__(self) -> str:
        return f"Pila({self._datos!r})"

# Ejemplo de uso
if __name__ == '__main__':
    s = Pila()
    s.push(10)
    s.push(20)
    print(s.pop())
    print(s.peek())