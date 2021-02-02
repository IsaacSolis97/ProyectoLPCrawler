import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

#leemos el archivo y lo convertimos en dataframe
jugadores = pd . read_csv ("./../CodigRuby/informeJugadores.csv")

#definomos las columnas
jugadores.columns = ["Liga","Jornada","Equipo","Nombre Jugador", "Puntos"]

#Filtros para obtener los mejores jugadores con su equipo por liga

print("Analisis de Jugadores por Liga")
nombreLigas = jugadores['Liga'].unique()
contador = 0
for liga in nombreLigas:
    contador= contador +1
    print(contador ,": " ,liga)
print(contador+1 ,":  Todas las ligas")

idliga= int(input("Ingrese el número que con en el que quiere filtrar: "))

if idliga >= 6:
    filtro1 = jugadores
else:
    if idliga == 1:
        filtro1 = jugadores[jugadores['Liga'] == "Liga Santander"]
    if idliga == 2:
        filtro1 = jugadores[jugadores['Liga'] == "Premier League"]
    if idliga == 3:
        filtro1 = jugadores[jugadores['Liga'] == "Europa League"]
    if idliga == 4:
        filtro1 = jugadores[jugadores['Liga'] == "Champions"]
    if idliga == 5:
        filtro1 = jugadores[jugadores['Liga'] == "Liga 1|2|3"]

filtro1Agrupar = filtro1.groupby(['Nombre Jugador', 'Equipo']).mean()
maxFiltro1 = filtro1Agrupar["Puntos"].max()

input("Enter para continuar")
print("\n")


print("Datos de la consulta")
print(filtro1Agrupar)
filtro1Agrupar['Puntos'].plot ( kind = 'hist' , title = 'Resultados' )
plt.show()

print("\n")


print("Jugadores con maximo puntos")
print("El puntaje maximo es: " , maxFiltro1)
jugadormax = filtro1Agrupar[filtro1Agrupar['Puntos'] == maxFiltro1 ]
print(jugadormax)

print("\n")
print("\n")

print("Busqueda de Mejores jugadores por Equipo")
nombreEquipo = jugadores['Equipo'].unique()
contador2 = 0
for equipo in nombreEquipo:
    contador2= contador2 +1
    print(contador2 ,": " ,equipo)
print("Ingrese 0, para hacer la budqueda en todos los equipos")
equipo= input("Ingrese el equipo que desea buscar:  ")
if equipo == "0":
    filtro1Equipo = jugadores
else:
    filtro1Equipo = jugadores[jugadores['Equipo'] == equipo]

filtro1EquipoAgrupado = filtro1Equipo.groupby(['Nombre Jugador', 'Equipo']).mean()
plt.hist(filtro1EquipoAgrupado)
plt.show()
print(filtro1EquipoAgrupado)

