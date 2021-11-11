"""
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
siguientes informaciones: La suma de los números que están dentro del intervalo (intervalo abierto). Cuantos números
están fuera del intervalo. Informa si hemos introducido algún número igual a los límites del intervalo.

Análisis
_______________________________________________________________________________________________________________________
- Pedimos al usuario que introduzca un carácter.
_______________________________________________________________________________________________________________________
Algoritmo
_______________________________________________________________________________________________________________________
- Variables:
- Secuencias:
- Bucles:
autor: Héctor Cevallos
fecha: 03/11/2021
"""
cnt_out = 0
same_limits = False
cnt_in = 0

lim_inf = int(input("Introduce el límite inferior del intervalo: "))
lim_sup = int(input("Introduce el límite superior del intervalo. Este número debe ser mayor al anterior: "))
while lim_inf > lim_sup:
    print("El límite inferior no puede ser mayor al superior. Introduce los valores en el orden solicitado.\n")
    lim_inf = int(input("Introduce el límite inferior del intervalo: "))
    lim_sup = int(input("Introduce el límite superior del intervalo. Este número debe ser mayor al anterior: "))
num = int(input("\nIntroduce 0 para salir: "))
while num != 0:
    if lim_inf < num < lim_sup:  # Pertenece al intervalo
        cnt_in += num
    else:  # No pertenece al intervalo
        cnt_out += 1
        if num == lim_inf or num == lim_sup:
            same_limits = True
        num = int(input("Introduce un número (0, para salir): "))
print("\nRESULTADOS:")
print(f"La suma de los números dentro del intervalo es {cnt_in}")
print(f"La cantidad de números fuera del intervalo es {cnt_out}")
if same_limits:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")