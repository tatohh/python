"""triangulos
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un
triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
Pediremos mediadas de los lados
y haremos los calculos para saber si es Equilatero, isósceles, escaleno o triangulo rectangulo
Datos de entrada: los tres lados del triángulo (flotante).
Información de salida: Tipo de rectángulo.
Variables: ladoA, ladoB, ladoC (flotante)
"""
print("Programa que te dice que tipo de triangulo es: ")
# Datos de entrada

lado1 = float(input("Dime lado 1: "))
lado2 = float(input("Dime lado 2: "))
lado3 = float(input("Dime lado 3: "))

# Calculos
if lado1 == lado2 and lado2 == lado3:
    print("Es un triangulo Equilatero")
else:
    if lado1 ** 2 == (lado2 ** + lado3 ** 2) or lado2 ** 2 == (lado1 ** 2 + lado3 ** 2) or lado3 ** 2 == (
            lado2 ** 2 + lado1 ** 2):
        print("El cachondo de Pitagoras tenia razon es un triangulo Rectangulo")
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triangulo Isoceles")
    else:
        print("Es un triangulo Escaleno")
