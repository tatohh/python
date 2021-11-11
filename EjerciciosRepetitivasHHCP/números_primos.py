"""
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

Analisis:

1.- Leer cantidad de número primos a mostrar, debe ser positivo
2.- Muestro el primer número primo, el 2.
3.- Inicializo el contador de número mostrados a 1.
4.- Inicializo la variable donde guardo el número a probar -> num=3
4.- Mientras no haya mostrado la cantidad de número indicados
5.- Considero que es primo. Inicializo el indicador -> es_primo=Verdadero
6.- desde el 3 hasta la raíz cuadrada del número
7.- Si es divisible -> Ya no es primo -> es_primo=Falso
8.- Si es primo
9.- Incremento el contador de números mostrados
10.- Escribo el número primo
11.- Como son impares, incremento en 2 el número a probar
autor: Héctor Cevallos
fecha:04/11/2021
"""
import math
while True:
    cantidad_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if cantidad_a_mostrar > 0:
        break
print("1: 2")
cantidad_mostrados = 1
num = 3
while cantidad_mostrados < cantidad_a_mostrar:
    es_primo = True
    divisor = 3
    while divisor <= math.sqrt(num) and es_primo:
        if num % divisor == 0:
            es_primo = False
        divisor += 2
    if es_primo:
        cantidad_mostrados += 1
        print(f"{cantidad_mostrados}: {num}")
    num += 2

