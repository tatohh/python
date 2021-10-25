"""dos_vehiculos
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El
que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos
vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará
el vehículo más rápido al otro.
Hay que saber las dos Velocidades asumiendo q la v2 es mayor que la v1, y la distancia que los separa
Variables: velocidad1, velocidad2, distancia
Algoritmo
Leer las dos Velocidades y la distancia entre ellos
Calcular el tiempo real que tarda en alcanzar el vehiculo 2 al vehiculo 1, aplicando t=d/(v1-v2)
Mostrar tiempo
"""
print("Programa que calcula el tiempo de un vehiculo en alcanzar a otro")
print("_________________________________________________________________")

# Datos de entrada
v1 = float(input("Introduce la velocidad del vehiculo1 (km/h): "))
v2 = float(input("Introduce la velocidad del vehiculo2 (km/h): "))
distancia = float(input("Dime la distancia que hay entre los dos vehiculos (km): "))
# Calculos
tiempo = 60 * distancia / (v2 - v1)
if v2 > v1:
    print("El vehiculo2 tardara en alcanzar al vehiculo1: ", tiempo,  "minutos")
if v1 > v2:
    print("Pos que le pise que no lo alcanza ni de coña")
