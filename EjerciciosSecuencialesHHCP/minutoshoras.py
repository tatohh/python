# minutoshoras
# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde
# autor: Héctor Cevallos
# fecha: 08/10/2021

"""
Programa que convierte los minutos a horas y nos muestra por pantalla a cuantas horas y minutos corresponde
Solicitud de Datos
pedimos al Usiario los minutos
Calculos
Hacemos los calculos para poder pasar de minutos a horas
Mostramos resultado por pantalla
"""
#Variables a crear
#horas
#minutos
import math
minutos = int(input("Dime los minutos: ") )
#Calculos
horas = minutos // 60
total_minutos = minutos % 60

print("Horas:%d - Minutos:%d"  % (minutos//60,minutos%60))

