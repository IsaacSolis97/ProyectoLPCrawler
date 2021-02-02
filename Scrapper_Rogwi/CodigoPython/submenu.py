
import  pandas as pd
import matplotlib.pyplot as plt
#funciones
def imprimir_historial(nba,mejor_equipo_nombre,temporadas):
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

def mejor_equipo_ofensivo():
    #1.Abrir el csv dentro de una variable
    nba = pd.read_csv('NBA_RegularSeason.csv')
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
    
    print(f"\nEl equipo con mejor ofensiva en los ultimos 5 años fue \'{mejor_equipo_nombre}\' con un PPG promedio de  {mejor_PPG} \n")
    imprimir_historial(nba,mejor_equipo_nombre,temporadas)



while True:
    print("             Analisis NBA                ")
    print("1. Mejor equipo ofensivo ultimas temporadas:")
    print("2. salir")
    op=int(input("Escoja una opcion"))
    if op==1:
        mejor_equipo_ofensivo()
    elif op==2:
        break
    


