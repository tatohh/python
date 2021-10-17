# GradosCelsius
# Programa que calcula la media de 3 numeros
# autor: Héctor Cevallos
# fecha: 08/10/2021

"""
Este programa suma y calcula media de tres numeros pedidos por teclado
Solicitud de Datos
numero 1
numero 2
numero 3

Calculos
Sumaremos los 3 numeros dados por pantalla y los dividiremos entre 3 para sacar la media
"""

numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))
numero3 = float(input("Introduce el tercer numero: "))

import statistics as stats

media = [numero1,numero2,numero3]
print ("La media es:",(stats.mean(media)))