"""Lista doblemente enlazada: NodoDoble y ListaDoble"""

from typing import Any, Iterator, Optional

class NodoDoble:
    def __init__(self, dato: Any) -> None:
        self.dato: Any = dato
        self.siguiente: Optional['NodoDoble'] = None
        self.anterior: Optional['NodoDoble'] = None

    def __repr__(self) -> str:
        return f"NodoDoble({self.dato!r})"

class ListaDoble:
    def __init__(self) -> None:
        self.head: Optional[NodoDoble] = None
        self.tail: Optional[NodoDoble] = None
        self._size: int = 0

    def insertar_inicio(self, dato: Any) -> None:
        nuevo = NodoDoble(dato)
        nuevo.siguiente = self.head
        if self.head:
            self.head.anterior = nuevo
        else:
            self.tail = nuevo
        self.head = nuevo
        self._size += 1

    def insertar_final(self, dato: Any) -> None:
        nuevo = NodoDoble(dato)
        if not self.tail:
            self.head = self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            nuevo.anterior = self.tail
            self.tail = nuevo
        self._size += 1

    def eliminar_por_valor(self, dato: Any) -> bool:
        cur = self.head
        while cur:
            if cur.dato == dato:
                if cur.anterior:
                    cur.anterior.siguiente = cur.siguiente
                else:
                    self.head = cur.siguiente
                if cur.siguiente:
                    cur.siguiente.anterior = cur.anterior
                else:
                    self.tail = cur.anterior
                self._size -= 1
                return True
            cur = cur.siguiente
        return False

    def obtener(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError('índice fuera de rango')
        # elegir dirección según cercanía (optimización)
        if index < self._size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.siguiente  # type: ignore
            return cur.dato  # type: ignore
        else:
            cur = self.tail
            for _ in range(self._size - 1, index, -1):
                cur = cur.anterior  # type: ignore
            return cur.dato  # type: ignore

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.dato
            cur = cur.siguiente

    def __repr__(self) -> str:
        return "ListaDoble([" + ", ".join(repr(x) for x in self) + "])"

# Ejemplo de uso
if __name__ == '__main__':
    ld = ListaDoble()
    ld.insertar_final('a')
    ld.insertar_final('b')
    ld.insertar_inicio('z')
    print(ld)
    ld.eliminar_por_valor('b')
    print(list(ld))