#hipotenusa_triangulo_rectangulo
#Programa que calcula la hipotenusa de un triángulo rectángulo
# autor: Héctor Cevallos
# fecha: 22/09/2021

"""
Solitamos datos
lado_1 del triangulo
lado_2 del triangulo

Calculos
La hipotenusa de un triángulo rectángulo es igual a la raiz cuadrada de la suma del cuadrado de los catetos.
Mostrar resultado
"""
import math
lado_1 = int (input("introduce el lado_1: "))
lado_2 = int (input("introduce el lado_2: "))

hipotenusa = math.sqrt((lado_1**2)+(lado_2**2))
print ("la hipotenusa del triangulo es ", hipotenusa )

