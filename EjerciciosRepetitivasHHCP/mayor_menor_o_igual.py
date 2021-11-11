"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa
debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Algoritmo:
Pedimos al usuario que introduzca el número por teclado
Se pediria que el usuario introduzca numeros
Y tendriamos que comprobar cuales son > 0, < 0, =0,
autor: Héctor Cevallos
fecha:04/11/2021
"""

# Variables cantidad = número de veces que se va a repetir la operación
# dependiendo del numero de veces se ira preguntando tantos numeros como veces ha puesto el usuario
# y se evaluara cuantos numeros introducidos son mayores, iguales o menores que 0

mayor = 0  # almacena la cantidad de números mayores que 0 introducidos por el usuario
menor = 0  # almacena la cantidad de números menos que 0 introducidos por el usuario
igual = 0  # almacena la cantidad de números iguales que 0 introducidos por el usuario

print("Programa que te indica si los numeros introducidos son: >0, <0, =0 ")

cantidad = int(input("Introduce el número de veces que se va a repetir la operación: "))

for numero in range(1, cantidad + 1):
    numero = int(input(f"número, {numero}: "))
    if numero > 0:
        mayor += 1
    elif numero < 0:
        menor += 1
    else:
        igual += 1

print(f"Numeros mayores: {mayor} ")
print(f"Numeros menores: {menor} ")
print(f"Numeros iguales: {igual} ")
