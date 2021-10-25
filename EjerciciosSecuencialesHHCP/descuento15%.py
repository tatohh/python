# descuento15%
# Programa que calcula el 15% de descuento
# autor: Héctor Cevallos
# fecha: 07/10/2021


"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
finalmente por su compra.
Variables
importe compras
"""
print("Programa que calcula el 15% de descuento de una tienda")
print("__________________________________________________________")

# Variables
venta_total = float(input("Importe total de compra: "))

# Calculos
Descuento = float(0.15 * venta_total)
total_compra = float(venta_total - Descuento)

# Mostrar resultados
print("Total a pagar:", total_compra)
