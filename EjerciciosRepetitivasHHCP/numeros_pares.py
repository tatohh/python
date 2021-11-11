"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Análisis
- Pedimos al usuario que introduzca un carácter.
- Variables:
- Secuencias:
- Bucles:
autor: Héctor Cevallos
fecha:04/11/2021
"""

print('Introduce dos números para que el programa imprima todos los pares entre esos números: ')

n1 = int(input("Introduce el número 1: "))
n2 = int(input("Introduce el número 2: "))

if n1 > n2:
    n1, n2 = n2, n1
if n1 % 2 == 1:
    n1 += 1
for n in range(n1, n2 + 1, 2):
    print(f"{n} ", end="")
