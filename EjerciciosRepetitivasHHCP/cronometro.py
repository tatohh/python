"""
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.
Análisis
_______________________________________________________________________________________________________________________
- Pedimos al usuario que introduzca un carácter.
_______________________________________________________________________________________________________________________
Algoritmo
# Inicializamos contador para las horas, minutos y segundos.
# Hacemos un ciclo infinito y esperamos 1 segundo cada iteración
# 02 es para indicar que va a ocupar dos lugares.
# Mientras los segundos sean menor a 59 se incrementa en 1. Así se van contando los segundos.
# En caso contrario (segundos mayor que 59) hacemos que vuelvan a 0.
# Si en ese caso los minutos son menos que 59, incrementamos los minutos en 1.
# En caso contrario (minutos mayor 59) dejamos los minutos a 0 e incrementamos la hora en 1..
# ponemos el cursor al principio de la línea

_______________________________________________________________________________________________________________________
- Variables:
- Secuencias:
- Bucles:
autor:Héctor Cevallos
fecha:03/11/2021
"""
import time
hours = 0
minutes = 0
seconds = 0

while True:
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)
    if seconds < 59:
        seconds += 1
    else:
        seconds = 0
        if minutes < 59:
            minutes += 1
        else:
            minutes = 0
            hours += 1
    print(8 * "\b", end="")
