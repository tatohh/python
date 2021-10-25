"""division_cero
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
o un mensaje de aviso en caso contrario.
autor. Héctor Cevallos
fecha: 21/10/2021
Entrada datos: pedimos number1 y number2 al usuario
Salida datos: mostrar division si y solo si el segundo numero no es cero caso contrario mostrar mensaje
Usaremos las condiciones if - else
"""

print("Programa que realiza una división de dos numeros solo si el segundo no es cero")

number1 = int(input("Introduce el primer numero: "))
number2 = int(input("Introduce el segundo numero: "))


if number2 != 0:
    print(f"El total de la division es: {number1 / number2}")
else:
    print("La division no se puede realizar")






