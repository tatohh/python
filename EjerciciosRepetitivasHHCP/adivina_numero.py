"""
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A
continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado.
# Desglose:
Se genera una funcion para que el programa genere un numero aleatorio del 1 al 100
Pedimos al usuario que introduzca un número y comprobamos si el número introducido es mayor o menor que el introducido
y ademas va restando el número de intentos utilizados
Variables:
i = número que genera la aplicación del 1 al 100
número = número introducido por el usuario
intentos = número de intentos maximo en adivinar i, en este caso 10
Utilizaremos la biblioteca random importando solo la función randint()
#Intentare utilizar busqueda binaria
autor: Héctor Cevallos
fecha 03/11/2021
"""
import random
from random import randint

# menor = 0
# mayor = 100
# medio = (menor + mayor) / 2

i = random.randint(1, 100)
intentos = 10

while True:
    numero = int(input(f"Tienes {intentos} intentos para adivinar mi número, Introduce un número del 1 al 100: "))
    if numero < i:
        print(f"{numero} es menor que el número pensado")
    elif numero > i:
        print(f"{numero} es mayor que el número pensado")
    intentos -= 1
    if numero == i or intentos == 0:
        break
if numero == i:
    print(f"Has adivinado el numero en {10 - intentos} intentos")
else:
    print(f"Has agotado el numero maximo de intentos. el numero a adivinar era {i}")
