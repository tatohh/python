# Programa para la resolucion de la ecuacion a x + b =0
# Autor: Hector Cevallos Paredes
# 18/10/2021

print ("Programa para la resolucion de la ecuacion a x + b = 0")

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

if  a != 0:
    x = -b / a
    print("Solucion:  ", x)

if a == 0:
    if b != 0:
        print("La ecuacion no tiene solucion")
    if b == 0:
        print("La ecuacion tiene infinitas soluciones")


