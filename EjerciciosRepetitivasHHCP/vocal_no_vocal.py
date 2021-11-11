"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina
cuando se introduce un espacio.
Analisis:
Pediremos al usuario un caracter
comprobaremos si es vocal o no

autor: Héctor Cevallos
fecha: 04/11/2021

"""

VOCALES = "AEIOUaeiou"

print("Programa que reconoce si el caracter introducido es Vocal o no")

caracter = input("Introduce un caracter: ")
while caracter != " ":
    if len(caracter) == 1:
        if VOCALES.find(caracter) >= 0:
            print("Es una vocal")
        else:
            print("No es una vocal")
        caracter = input("Introduce un nuevo caracter: ")
    else:
        caracter = input("Error:Introduce un solo caracter: ")
print("Has introducido un espacio. Fin DEL PROGRAMA")

