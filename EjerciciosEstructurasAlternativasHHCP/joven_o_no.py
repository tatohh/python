"""joven_o_no
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Planteamiento:
Solicitaremos las Variables del enunciado que en este caso son las edades de persona1 y persona2 y mostraremos por pan_
talla quien es mas joven o si tienen la misma edad
"""

print("Programa que indica que edad es mas joven o si tienen la misma edad")

persona1 = int(input("Dime tu edad persona1: "))
persona2 = int(input("Dime tu edad persona2: "))

if persona1 > persona2:
    print("persona2 es mas joven ")
if persona2 > persona1:
    print("persona1 es mas joven")
if persona1 == persona2:
    print("Sois igual de jovenzuelos")

# Segun respuestas se puede hacer con (if, elif, else), pero como me funciono asi asi lo deje
