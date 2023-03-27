"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:
Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
Obtener el número de elementos almacenados (tamaño).
Saber si la pila o la cola está vacía.
Vaciar completamente la pila o la cola.
Para el caso de la cola:
Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

"""
class Queue:

    def __init__(self, elements = None):
        if elements:
            self.elements = elements
        else:
            self.elements = []

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return not self.elements

    def clear(self):
        self.elements = []

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)

    @property
    def size(self):
        return len(self.elements)

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0]