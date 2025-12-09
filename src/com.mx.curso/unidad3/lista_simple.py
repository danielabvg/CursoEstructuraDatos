"""Lista simplemente enlazada: Nodo y Lista
Implementa operaciones básicas: insertar al inicio, insertar al final,
eliminar por valor, obtener por índice, iteración y representación.
"""

from typing import Any, Iterator, Optional

class Nodo:
    def __init__(self, dato: Any) -> None:
        self.dato: Any = dato
        self.siguiente: Optional['Nodo'] = None

    def __repr__(self) -> str:
        return f"Nodo({self.dato!r})"

class Lista:
    def __init__(self) -> None:
        self.head: Optional[Nodo] = None
        self._size: int = 0

    def insertar_inicio(self, dato: Any) -> None:
        nuevo = Nodo(dato)
        nuevo.siguiente = self.head
        self.head = nuevo
        self._size += 1

    def insertar_final(self, dato: Any) -> None:
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            cur = self.head
            while cur.siguiente:
                cur = cur.siguiente
            cur.siguiente = nuevo
        self._size += 1

    def eliminar_por_valor(self, dato: Any) -> bool:
        prev = None
        cur = self.head
        while cur:
            if cur.dato == dato:
                if prev is None:
                    self.head = cur.siguiente
                else:
                    prev.siguiente = cur.siguiente
                self._size -= 1
                return True
            prev = cur
            cur = cur.siguiente
        return False

    def obtener(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError('índice fuera de rango')
        cur = self.head
        for _ in range(index):
            cur = cur.siguiente  # type: ignore
        return cur.dato  # type: ignore

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.dato
            cur = cur.siguiente

    def __repr__(self) -> str:
        return "Lista([" + ", ".join(repr(x) for x in self) + "] )"

# Ejemplo de uso (puede quitarse cuando suba al repo):
if __name__ == '__main__':
    l = Lista()
    l.insertar_final(1)
    l.insertar_final(2)
    l.insertar_inicio(0)
    print(l)
    l.eliminar_por_valor(1)
    print(list(l))