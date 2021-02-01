#numpy, pandas y xlrd
import  pandas as pd
import matplotlib.pyplot as plt

#1.Abrir el csv dentro de una variable
nba = pd.read_csv('NBA_RegularSeason.csv')


# Pregunta ¿Cuál es el mejor equipo ofensivo (mayor promedio de Puntos ) de las últimas temporadas y en que posiciones ha quedado en cada temporada regular?

#Extraer las temporadas que tiene el dataset
temporadas = nba['Temporada'].unique().tolist()
#Extraer los equipos que tiene el dataset
equipos = nba['Equipo'].str.rstrip("*").unique().tolist()
#sacar la media de PPG de cada equipo
estadisticas_por_equipo = [] #sirve para graficar la media de PPG por equipo
#recorro los equipos
for eq in equipos:
    equipo= nba[nba['Equipo'].str.contains(eq)]
    estadisticas_por_equipo.append(round(equipo['PuntosPorJuego'].mean(),3))
#extraigo el mejor PPG
mejor_PPG =max(estadisticas_por_equipo)
mejor_equipo_nombre = equipos[estadisticas_por_equipo.index(mejor_PPG)]
def imprimir_historial():
    datos_mejor_equipo = nba[nba['Equipo'].str.contains(mejor_equipo_nombre)]
    print(datos_mejor_equipo)
    for temporada in temporadas:
        pos = datos_mejor_equipo[datos_mejor_equipo['Temporada'] == temporada]['Poscicion'].tolist()
        print(f"Durante la temporada Regular  {temporada} el equipo quedó en la posicion: {pos[0]}.")
        if pos[0]<=8 :
            print(f"El quipo clasificó a los Playoffs {temporada}.\n")
        else:
            print(f"El equipo no clasificó a los PlayOffs {temporada}.\n")    
    #impresion de grafico
    plt.plot(datos_mejor_equipo['Temporada'].tolist(),datos_mejor_equipo['PuntosPorJuego'])
    plt.show()

print(f"\nEl equipo con mejor ofensiva en los ultimos 5 años fue \'{mejor_equipo_nombre}\' con un PPG promedio de  {mejor_PPG} \n")
imprimir_historial()

