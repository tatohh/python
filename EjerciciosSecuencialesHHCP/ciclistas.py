"""ciclistas
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta
llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
autor: Héctor Cevallos Paredes
fecha: 20/10/2021
Algoritmo
-Pedimos hora minutos y segundos de partida
-Pedimos el tiempo que tarda hasta llegar a la otra ciudad




"""
# Datos
horadesalida = int(input("Dime la hora de partida: "))
minutosdesalida = int(input("Dime los minutos: "))
segundosdesalida = int(input("Dimelos segundos: "))
segundosllegada = int(input("Dime el tiempo que tarda en el viaje: "))

# Calculos
segundostotales = horadesalida * 3600 + minutosdesalida * 60 + segundosdesalida + segundosllegada
horas_finales = segundostotales // 3600
minutos_finales = (segundostotales % 3600) // 60
segundos_finales = (segundostotales % 3600) % 60
# Salida
print("La hora de la llegada a la otra ciudad es: " + str(horas_finales % 24) + "horas" + str(
    minutos_finales) + "minutos" +
      str(segundos_finales) + "segundos")
