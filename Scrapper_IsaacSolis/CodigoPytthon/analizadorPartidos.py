import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

#leemos el archivo y lo convertimos en dataframe
jugadores = pd . read_csv ("./../CodigRuby/informeResultados.csv")

#definomos las columnas
jugadores.columns = ["Liga","Jornada","Equipo1","Equipo2", "Goles1", "Goles2"]

#Filtros para analizar los resultados de los partidos de futball de cada liga

print("Analisis de Partidos por Liga")
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
#agregamos un campo nuevo llamado diferecnia de goles
 

filtro1[['Goles1', 'Goles2']] =  filtro1[['Goles1', 'Goles2']].astype(int)
filtro1['Diferencia'] = filtro1['Goles1'] - filtro1['Goles2']

 #filtro ganadores
equiposGanadoresL = filtro1[filtro1['Diferencia'] >0]
print("Ganadores Locales\n")
listaGanadoresL = equiposGanadoresL[['Equipo1', 'Goles1']]
print(listaGanadoresL)

equiposGanadoresV = filtro1[filtro1['Diferencia'] <0]

print("Ganadores Visitantes")
listaGanadoresV = equiposGanadoresV[['Equipo2', 'Goles2']]
print(listaGanadoresV)



print("\n")
maxGoleadorL = listaGanadoresL['Goles1'].max()
maxGoleadorV = listaGanadoresV['Goles2'].max()

equipoGoleadorL = listaGanadoresL[listaGanadoresL['Goles1'] == maxGoleadorL]
equipoGoleadorV = listaGanadoresV[listaGanadoresV['Goles2'] == maxGoleadorV]


print("Equipo con maximo goles de la liga")
print("Local")
print(equipoGoleadorL)
print("Visitante")
print(equipoGoleadorV)

print("Cuantos partidos quedaron empates")
equipoEmpate = filtro1[filtro1['Diferencia'] ==0]
countEmpate = len(filtro1.index)
print(countEmpate)








