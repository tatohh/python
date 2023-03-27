"""
6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase (el resultado es otro objeto).
Sumar y restar segundos, minutos y/o horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
Glosario:
En esta clase, creamos un objeto Duration que almacena una duración de tiempo en horas, minutos y segundos.

Comenzamos a definir el método __init__que se ejecuta cuando se crea un objeto de la clase.
Aquí podemos especificar los valores iniciales para las horas, minutos y segundos. Si no se proporcionan valores,
se utilizan los valores predeterminados de 0.

Luego, definimos el método __str__ para devolver una cadena que representa los valores de horas,
minutos y segundos en un formato legible.

Después, definimos los getters y setters para las propiedades hours, minutesy second con las anotaciones @propertyy setter.
Estos permiten acceder y modificar los valores de las propiedades de manera segura y controlada.

Luego, agregamos métodos para sumar y restaurar objetos de la clase, así como para sumar y restaurar segundos,
minutos y horas individualmente.

"""

class Duration:
    def __init__(self, hours=0, minutes=0, second=0):
        self.hours = hours
        self.minutes = minutes
        self.second = second


    @property
    def hours(self):
        return self._hours


    @hours.setter
    def hours(self, value):
        self._hours = value


    @property
    def minutes(self):
        return self._minutes


    @minutes.setter
    def minutes(self, value):
        self._minutes = value


    @property
    def seconds(self):
        return self._seconds


    @seconds.setter
    def seconds(self, value):
        self._seconds = value


    def add(self, duration):
        self.hours += duration.hours
        self.minutes += duration.minutes
        self.seconds += duration.seconds


    def subtract(self, duration):
        self.hours -= duration.hours
        self.minutes -= duration.minutes
        self.seconds -= duration.seconds


    def add_seconds(self, seconds):
        self.seconds += seconds


    def add_minutes(self, minutes):
        self.minutes += minutes


    def add_hours(self, hours):
        self.hours += hours


    def subtract_seconds(self, seconds):
        self.seconds -= seconds


    def subtract_minutes(self, minutes):
        self.minutes -= minutes


    def subtract_hours(self, hours):
        self.hours -= hours

    def __str__(self):
        return "{}h {}m {}s".format(self.hours, self.minutes, self.second)