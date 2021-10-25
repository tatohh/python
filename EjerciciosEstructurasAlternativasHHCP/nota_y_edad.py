"""
nota_y_edad
Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es
mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo,
pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
autor: Héctor Cevallos
fecha: 22/10/2021
Variables:
edad
nota
sexo
"""
print("Programa que pide nota edad y sexo y muestra mensaje de Aceptada o Posible")

edad = float(input("dime tu edad: "))
nota = float(input("dime tu nota: "))
sexo = input("dime tu sexo: ")

if edad >= 18 and nota >= 5:
    if sexo.upper() == "F":
        print("ACEPTADA")
    else:
        print("POSIBLE")
else:
    print("NO ACEPTADA")
