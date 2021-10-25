# Raiz cuadrada y raiz cubica
# Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
# Python no tiene ninguna función predefinida que permita calcular la raíz cúbica,
# ¿cómo se puede calcular?

"""
Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

"""
# Solicitamos datos

numero = float(input("Introduce un numero: "))

# Calculos
print("La raiz cuadrada del numero es: ", numero ** (1 / 2))
print("La raiz cubica del numero es: ", numero ** (1 / 3))

###
# Tambien podemos hacer el calculo importando la libreria math
import math

# print("La raiz cuadrada del numero es: ", math.sqrt(numero))
# print(f"La raiz cubica del numero es: {math.pow(numero, 1 / 3)}")
