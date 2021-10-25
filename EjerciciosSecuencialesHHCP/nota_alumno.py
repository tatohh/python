"""
nota_alumno
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada
respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el
estudiante.
autor: Hector Cevallos
Variables
res_correctas, res_incorrectas_, res_blanco, nota_examen, nota_final, total_nota
"""

VALOR_PREGUNTA = 5  # Valor que tiene cada pregunta acertada
print("Este programa calcula la nota final de un alumno considerando que cada respuesta correcta suma 5 puntos, "
      "cada incorrecta resta un punto, y las no contestadas no se valoran.")

# Datos entrada
res_correctas = int(input("Numero de respuestas correctas: "))
res_incorrectas = int(input("Numero de respuestas incorrectas: "))
res_en_blanco = int(input("Numero depreguntas en blanco: "))

# Calculos
nota_examen = (res_correctas + res_incorrectas + res_en_blanco) * VALOR_PREGUNTA
nota_final = (res_correctas * VALOR_PREGUNTA) + (res_incorrectas * (-1))
total_nota = (nota_final * 10) / nota_examen
print(total_nota)
