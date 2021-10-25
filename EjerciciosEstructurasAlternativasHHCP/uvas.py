"""uvas
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se
clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo
y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo
siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice
un algoritmo para determinar la ganancia obtenida.
Datos de entrada
precio inicial kilo
kilos de uva
tipo de uva
Como el precio puede variar creo constantes solo del precio segun su tipo


"""
PRECIOA1 = 0.20
PRECIOA2 = 0.50
PRECIOB1 = -0.30
PRECIOB2 = -0.50

print("Programa que calcula el valor a pagar segun el tipo de uva")

precio_inicial_kilo = float(input("Introduce el precio Inicial del kilo de uva: "))
kilos_uva = float(input("Introduce total kilos: "))
tipo = input("Introduce A1,A2 o B1,B2 segun sea el tipo de uva: ")

if tipo == "A1":
    ganancia = (precio_inicial_kilo * kilos_uva) + (kilos_uva * PRECIOA1)
    print(f"La ganancia obtenida es, {ganancia} €.")
if type == "A2":
    ganancia = (precio_inicial_kilo * kilos_uva) + (kilos_uva * PRECIOA2)
    print(f"La ganancia obtenida es, {ganancia} €.")
if type == "B1":
    ganancia = (precio_inicial_kilo * kilos_uva) + (kilos_uva * PRECIOB1)
    print(f"La ganancia obtenida es, {ganancia} €.")
if type == "B2":
    ganancia = (precio_inicial_kilo * kilos_uva) + (kilos_uva * PRECIOB2)
    print(f"La ganancia obtenida es, {ganancia} €.")