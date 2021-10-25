"""
Bisiesto
Escribir un programa que lea un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
excepto que también sea divisible por 400.
Variables
año
bisiesto

"""
print("Programa que pregunta un año y te dice si es bisiesto o no")

año = int(input("Introduce un año: "))
if (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0)):
    print(f"El año, {año} es bisiesto aprovecha ese dia de más")
else:
    print(f"El año, {año} no lo es tienes que seguir esperando")
