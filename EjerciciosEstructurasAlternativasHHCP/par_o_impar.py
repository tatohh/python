# par_o_impar
# Escribe un programa que lea un número e indique si es par o impar.
# Autor: Héctor Cevallos
# 18/10/2021

"""
Programa que pide un numero entero por pantalla y te indica si espar o impar
Datos de entrada: Pedir un numero (entero) por pantalla
Datos de salida: Indicar si el numero es par o impar
Variables: number (entero)
Algoritmo.
Leer numero por pantalla
Comprobar si es par
Caso contrario indicar que no
"""

print("Programa que comprueba si un numero espar o no")
print("---------------------------------------------")

number = int(input("Dime un numero: "))

if number % 2 == 0:
    print("Es par")
else:
    print("Es impar")
