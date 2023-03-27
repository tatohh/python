"""
Muestra un menú con las siguientes opciones:

Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa.
Si no se introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida (se ha ejecutado la opción anterior),
si no la hay mostrará un mensaje de error.
Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
Añadir años a la fecha. El mismo procedimiento que la opción 2.
Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior,
igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
Terminar.
Consideraciones a tener en cuenta:

El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger alguna opción.
Las fechas las manejaremos con la clase datetime.date.
"""

class Date:

    def __init__(self, day, month, year):
        if not all(map(lambda x: isinstance(x, int), [day, month, year])):
            raise ValueError("Los valores de día, mes y año deben ser números enteros")
        if not (1 <= day <= 31) or not (1 <= month <= 12):
            raise ValueError("El día y el mes deben estar entre 1 y 31, y el mes entre 1 y 12")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                  "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        return f"{self.day} de {months[self.month - 1]} de {self.year}"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.day == other.day and self.month == other.month and self.year == other.year
        return False

    def __lt__(self, other):
        if isinstance(other, Date):
            if self.year < other.year:
                return True
            elif self.year == other.year and self.month < other.month:
                return True
            elif self.year == other.year and self.month == other.month and self.day < other.day:
                return True
            else:
                return False
        raise TypeError("Se puede comparar solo con objetos de la clase Date")

    def __le__(self, other):
        return self < other or self == other

    def is_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        return False

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.is_leap_year() and self.month == 2:
            return 29
        else:
            return 28

    def add_days(self, days):
        self.day += days
        while self.day > self.days_in_month():
            self.day -= self.days_in_month()
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def sub_days(self, days):
        self.day -= days
        while self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.month = 12
                self.year -= 1
            self.day += self.days_in_month()

    def days_between(self, other):
        if not isinstance(other, Date):
            raise TypeError("Se puede calcular la diferencia solo entre objetos de la clase Date")
        days = 0
        current = Date(self.day, self.month, self.year)
        while current < other:
            current.add_days(1)
            days += 1
        while current > other:
            current.sub_days(1)
            days -= 1
        return days



"""
# Creación de fechas
f1 = Date(1, 10, 2020)
f2 = Date(f1)
f3 = Date(2, 10, 2020)

# Sumar y restar días
f1.add_days(5)
print(f1) # 6 de octubre de 2020
f1.sub_days(10)
print(f1) # 26 de septiembre de 2020

# Restar fechas
dif = f3 - f2
print(dif) # 1

# Comparar fechas
print(f1 < f3) # True
print(f1 > f3) # False
print(f1 == f2) # False
print(f1 != f2) # True

# Determinar si un año es bisiesto
print(f1.is_leap_year()) # False

# Obtener día de la semana
print(f1.day_of_week()) # martes

"""

