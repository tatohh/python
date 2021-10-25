# mayor_o_no
# Programa que pida dos números e indique si el primero es mayor que el segundo o no.
# 17/10/2021
# Autor: Hector Cevallos Paredes

"""
Programa que pida dos números e indique si el primero es mayor que el segundo o no.
Analisis
Tenemos que pedir dos numeros y comprobar si el segundo es mayor que el primero
Datos de entrada: pedimos 2 numeros ( enteros)
Datos de salida: indicar si el primero es mayor que el segundo o no
Variables: number (entero)
Algoritmo
1º Leer los dos numeros
2º Si el segundo numero es menor que el primero indicar que el primero es mayor
3º en caso contrario decir que no
"""

print("Comprobacion si un numero es > o < que el segundo")
print("----------------------------")

num1 = float(input("Dime el primer numero: "))
num2 = float(input("Dime el segundo numero: "))

if num1 > num2 and num2 < num1:
    print("Es mayor")
elif num1 < num2 and num2 > num1:
    print("No lo es")
