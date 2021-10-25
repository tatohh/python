"""
es_mayuscula
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
"""
print("Programa que comprueba si la cadena introducida es una mayuscula")

cadena = str(input("Introduce la cadena: "))

if len(cadena) == 1 and "A" <= cadena <= "Z":
    print("La cadena es mayuscula")
else:
    print("no lo es")
