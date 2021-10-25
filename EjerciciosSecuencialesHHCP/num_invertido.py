# num_invertido
# Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
# autor: Héctor Cevallos
# fecha: 12/10/2021

"""
Dado dos numeros de caracter decimal se imprima dicho numero invertido
Variables
numero, digito1, digito2, invertido
"""

print("Programa que invierte el numero dado")
print("_______________________________________________-")

# pedimos datos
number = input("Dame un numero de dos cifras: ")

digito1 = number[0]
digito2 = number[1]
invertido = number[1] + number[0]

print("El numero invertido es:", number[::-1])
