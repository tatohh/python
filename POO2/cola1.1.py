

class Cola:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def Encolar(self, item):
        self.__items.insert(0,item)

    def Desencolar(self):
        return self.__items.pop()

    def LeerPrimerElemento(self):
        return self.__items[len(self.__items)-1]

    def NumeroElemntos(self):
        return len(self.__items)

    def MostrarCola(self):
        print("Cola: ",self.__items, "Primer Elemento")