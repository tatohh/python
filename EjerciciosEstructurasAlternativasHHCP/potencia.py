"""
potencia
Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden
ocurrir tres cosas:
El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultadoes 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
Variables
base ; exponente ; potencia
Algoritmo
Introduce la base y el exponente
"""

print("Programa que te calcule la potencia pidiendote la base y el exponente")

# Calculos
base = float(input("Introduce la base de la potencia: "))
exponente = float(input("Introduce el exponente de la potencia: "))
potencia = pow(base, exponente)

if exponente > 0:
    print(f"La potencia es, {potencia}")
elif exponente == 0:
    print(f"La potencia es 1")
elif exponente < 0:
    potencia = pow(base, abs(exponente))
    print(f"La potencia es", (1/{potencia}))

