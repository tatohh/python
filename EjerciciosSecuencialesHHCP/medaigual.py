# Ejercicio 01 de secuenciales en Python
# Programa que pregunta al usuario su nombre y lo saluda. o lo manda a la mierda
# autor: Héctor Cevallos
# fecha: 08/10/2021

"""
El día dia de mes del año anyo nació nombre, hoy tendría x años
# Variables
pedimos dia , mes y año al usuario
pedimos nombre usuario
Realizamos calculos
Mostramos resultados
"""

dia = int(input("Dime el dia que naciste: "))
mes = input("Dime el mes que naciste: ")
anyo = int(input("Dime el año que naciste: "))
nombre = input("Dime tu nombre: ")
x = 2021 - anyo
# Calculos
print(f"El día {dia} de {mes} del año {anyo} nació {nombre}, hoy tendría {x} años ")
