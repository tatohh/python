# 10%sueldo
# Programa que convierte un valor dado en grados Fahrenheit a grados Celsius.
# autor: Héctor Cevallos
# fecha: 07/10/2021

"""
Este programa calcula el sueldo de un vendedor  que recibe un sueldo base mas un 10% extra por comisión de sus
ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en
el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
Variables:
preguntamos sueldo base que recibe
importe venta 1,2 y 3
Caculos a realizar:
sacamos el 10% del valor de cada una de las ventas y lo sumamos al sueldo base

"""
# Peticion de datos
sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce importe venta1: "))
venta2 = float(input("Introduce importe venta2: "))
venta3 = float(input("Introduce importe venta3: "))

# calculos

comisiones = (venta1 + venta2 + venta3) * 0.1
sueldo_mes = float(comisiones + sueldo_base)
# muestra de resultados
print("Sueldo_mes: ", sueldo_mes)
print("Total comisiones: ", comisiones)
