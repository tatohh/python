"""
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo
si el carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula,
minúscula o acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No
es un carácter» si el usuario ha introducido más de un carácter.
Algoritmo:
Pedimos un caracter por teclado y combrobamos
si es un digito mostramos mensaje: es un digito
si no lo es combrobar si es una letra: si la es mostramos mensaje de es una letra
si tampoco lo es comprobamos si es un numero. si lo es mostramos mensaje es un numero
si tampoco lo es . mostramos mensaje es otro caracter.
fin si
"""
print("Programa que comprueba que tipo de caracter es")

caracter = (input("Introduce un caracter: "))
if len(caracter) == 1:
    if caracter in ".:;()[]¡!¿?'\,-/— ":
        print("Es un signo de puntuacion")
    elif caracter.isalpha():
        print("Es una letra")
    elif caracter.isdigit():
        print("Es un digito")
    else:
        print("Es otro carácter")
else:
    print("No es un carácter")
