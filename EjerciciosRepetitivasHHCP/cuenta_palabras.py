"""
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por
espacios), realiza un programa que cuente cuantas palabras tiene.
autor: Hector Cevallos
fecha:04/11/2021
"""
print("Contador de palabras")
print("--------------------")

cadena = input("Introduce una frase: ")
estoy_en_palabra = False
contador_palabras = 0
for c in cadena:
    if c != " ":
        if not estoy_en_palabra:
            estoy_en_palabra = True
            contador_palabras += 1
    else:
        estoy_en_palabra = False
print("Número de palabras:", contador_palabras)