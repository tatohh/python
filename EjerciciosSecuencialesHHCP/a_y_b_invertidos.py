"""a_y_b_invertidos
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo
que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
autor: Héctor Cevallos Paredes
20/10/2021
"""
print("Programa que invierte el valor de dos puntos")
print("________________________________________________")

x = int(input("La primer variable es: "))
y = int(input("La segunda variable es: "))

# Intercambio de valores

x, y = y, x
# Salida de datos
print("La primera variable es", x, (" y la segunda", y))
