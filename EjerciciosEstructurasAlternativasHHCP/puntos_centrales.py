"""puntos_centrales
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y
las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas
Datos de entrada: x1,y1,x3,y2,r1,r2 (real)
Información de salida: Tipo de relación entre las circunferencias

Variables: x1,y1,x2,y2,r1,r2 (real), distancia (real)
"""

print("Calculo de los puntos centrales de 2 circunferencias")

import math

# Datos de entrada
x1 = float(input("Dime coordenada x1 de circunferencia1: "))
y1 = float(input("Dime coordenada y1 de circunferencia1: "))
r1 = float(input("Dime radio primera circunferencia: "))
x2 = float(input("Dime coordenada x2 de circunferencia2: "))
y2 = float(input("Dime coordenada y2 de circunferencia2: "))
r2 = float(input("Dime radio segunda circunferencia: "))
# Formula
distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

if distancia > (r1 + r2):
    print("Circunferencias exteriores")
elif (r1 + r2) > distancia > abs(r1 - r2):
    print("Circunferencias secantes")
elif 0 < distancia < abs(r1 - r2):
    print("Circunferencias interiores")
elif distancia == (r1 + r2):
    print("Circunferencias tangentes exteriores")
elif distancia == abs(r1 - r2):
    print("Circunferencias tangentes interiores")
elif distancia == 0:
    print("Circunferencias concéntricas")
else:
    print("Esta situación no se puede dar")
