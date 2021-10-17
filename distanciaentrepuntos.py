# distancia entre dos numeros
# Pide al usuario dos números y muestra la "distancia" entre ellos
# autor: Héctor Cevallos
# fecha: 11/10/2021

"""
Programa que calcula la distancia entre dos puntos y muestra la distancia
entre ellos.
Variables
pares de puntos x1,y1,x2,y2
distancia
"""
# importamos tabla
import math

# Solicitamos datos

x1 = int(input("Dime la coordenada (x) del punto 1: "))
y1 = int(input("Dime la coordenada (y) del punto 1: "))
x2 = int(input("Dime la coordenada (x) del punto 2: "))
y2 = int(input("Dime la coordenada (y) del punto 2: "))

distancia = math.sqrt(math.pow(x2 - x1, 2) + (math.pow(y2 - y1, 2)))

print("La Distancia entre los 2 puntos es: ", distancia)

