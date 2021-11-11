"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el
resultado de la potencia. No se puede utilizar el operador de potencia ni la función. Análisis
- Pedimos al usuario que introduzca un carácter.
 Algoritmo
 # Inicializamos variables
# Esta variable, será uno elevado al exponente y luego lo multiplicamos por la base introducida.
# Usamos guión porque la variable no será necesaria, solo necesitamos que el ciclo se ejecute.
# La variable _ coge el valor absoluto del exponente.
# La potencia se multiplica por la base, el número de veces que indique el exponente.
# Exponente negativo es 1 partido por la potencia.
# Salida.
  _____________________________________________________________________________________________________________
 - Variables:
 - Secuencias:
 - Bucles:
 autor: Héctor Cevallos
 fecha:04/11/2021
 """
potencia = 1
base = float(input('Introduce la base: '))
exponent = int(input('Introduce el exponente: '))
for _ in range(abs(exponent)):
    potencia *= base
if exponent < 0:
    potencia = 1/potencia
print(f"\n{base} elevado a {exponent} es {potencia}")
