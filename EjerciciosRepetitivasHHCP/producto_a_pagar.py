"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 €
y así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará
después de los 20 meses.
Algoritmo:
# Inicializamos las variables.
# month contiene el valor del pago del primer mes.
# Total es un acumulador de los importes mensuales.
# Ciclo for donde vamos a obtener el número de mes con el pago correspondiente.
# Total va acumulando la cantidad del mes anterior.
# month_pay lo multiplicamos por dos para darle el valor del mes siguiente.
# Pago total

- Variables: PAGO_
- Secuencias:
- Bucles:

autor: Héctor Cevallos
fecha: 04/11/2021
"""

month_pay = 10
total = 0
for month in range(1, 21):
    print(f"Pago mes {month:2d}: {month_pay:2d}€")
    total += month_pay
    month_pay *= 2
print(f"\n Total a pagar: {total: d}€")
