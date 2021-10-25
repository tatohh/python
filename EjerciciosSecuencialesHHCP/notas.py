# notas
# Un programa que calcule la calificación del alumno
# autor: Héctor Cevallos
# fecha: 11/10/2021

"""
Realizamos un programa que calcule la calificación final
Porcentages a tener en cuenta
55% del promedio de sus tres calificaciones
30% de la calificación del examen final
15% de la calificacion de un trabajo

"""
# Variables
# 55% examen Parcial
# 30% examen final
# 15% trabajo final
print("Programa que calcula la calificacion final del alumno")
print("____________________________________________________________")

examen1 = float(input("Introduce nota examen 1: "))
examen2 = float(input("Introduce nota examen 2: "))
examen3 = float(input("Introduce nota examen 3: "))
examenparcial = float((examen1 + examen2 + examen3) // 5.5)
print(" Examen Parcial: ", examenparcial)
examenfinal = float(input("introduce la nota del examen final: "))
notafinal = float(examenfinal * 30 // 100)
print("Examen final: ", notafinal)
trabajofinal = float(input("Introduce nota trabajo final: "))
nota_trabajo = float(trabajofinal * 15 // 100)
print("Trabajo final: ", nota_trabajo)
notaalumno = float(examenparcial + notafinal + nota_trabajo)
print("La nota del alumno es: ", notaalumno)