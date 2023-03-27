"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).
La pila permitira estas operaciones:
    Crear la pila con o sin valores iniciales o a partir de otra pila.
    Obtener el número de elementos almacenados (tamaño).
    Saber si la pila o la cola está vacía.
    Vaciar completamente la pila o la cola.
    Para el caso de la pila:
        Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
        Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
        Leer el elemento superior de la pila sin retirarlo (top)

Glosario:
__init Es el metodo constructor de la clase pila. Podemos proporcionar
una lista inicial al crear una nueva instancia de la clase o crear una pila vacia.
__len__ Este metodo devuelve el numero de elementos que hay en la pila
is_empty Este metodo devuelve un valor booleano True si la pila esta vacia o False en caso contrario
clear Este metodo vacia completamente la pila
push Este metodo añade un elemento a la pila
pop Este metodo saca yn devuelve un elemento de la pila
top Este metodo devuelve el elemento superior de la pila sin retirarlo
top.setter Este método establece el elemento superior de la pila.
También comprueba si el valor proporcionado es un entero mediante el uso de typecheck.
Si el valor no es un entero, se produce un error de tipo TypeError.

Añado un atributo de clase contador,

"""

class Stack:
    count = 0

    def __init__(self,*elements):
        Stack.count += 1
        if len(elements) == 1 and isinstance(elements[0], Stack):
            self.__elements = list(elements[0].__elements)
        else:
            self.__elements = list(elements)

    def size(self):
        return len(self.__elements)

    def is_empty(self):
        return not self.__elements    # return self.size == 0

    def clear(self):
        self.__elements = []

    def push(self, element):
        self.__elements.insert(0, element)

    def pop(self):
        self.__elements.pop(0)

    @property
    def top(self):
        return self.__elements[0]




"""
    @top.setter
    def top(self, value):
        if type(value) is not int:
            raise TypeError("El valor no es un entero")
        if self.is_empty():
            self.push(value)
        else:
            self.__elements[-1] = value"""
