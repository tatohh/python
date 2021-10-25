# distancia entre dos numeros
# Pide al usuario dos números y muestra la "distancia" entre ellos
# autor: Héctor Cevallos
# fecha: 11/10/2021

"""
Programa que calcula la distancia entre dos numeros dados por el usuario
Variables
num1 y num2
"""
# Solicitud de datos
num1 = int(input("Dime el numero 1: "))
num2 = int(input("Dime el numero 2: "))

# Calculos
print("Distancia: ", abs(num1 - num2))
