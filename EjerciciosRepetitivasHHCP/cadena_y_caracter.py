"""
Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
autor:Héctor Cevallos
fecha:03/11/2021

"""
cadena = input("Introduce una cadena de caracteres: ")
caracter = input("Introduce un carácter: ")
acumulador = 0

for i in range(len(cadena)):
    if cadena[i] == caracter:
        acumulador += 1  # 0 -> 1

print(f" En {cadena} el caractacter {caracter} aparace {acumulador} veces.")
