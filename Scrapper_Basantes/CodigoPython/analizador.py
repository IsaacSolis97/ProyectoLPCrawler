import pandas as pd
import matplotlib.pyplot as plt

#crea el dataframe usando pandas
ligas = pd.read_csv ("./../CodigoRuby/datos.csv")

#borra elementos nan
ligas.dropna()

#nombra columnas
ligas.columns = ["Rank", "Squad", "MatchesPlayed", "Wins", "Draws", "Losses", "Points", "GoalDiference"]

#genera lista de equipos no repetidos
#equipos = ligas['Squad'].unique().tolist()
#cantidad = len(equipos)
#print(equipos)
#print("La cantidad de equipos diferentes en el mundo del futbol es: ", cantidad)

descriptor = ligas['Points'].describe()
media = ligas['Points'].mean()
print("Datos estadisticos significativos para el analisis")
print(descriptor)
print("media aritmetica: ", media)

maximo = ligas['Points'].max()
diferencia = maximo - media
print("La maxima cantidad de puntos es: ", maximo)
print("La diferencia entre el maximo y la media aritmetica es: ", diferencia)
print("Los equipos que exeden 62 puntos son: ")
print(ligas[ligas.Points > 62])



#genera grafico
#ligas['Points'].plot(kind='bar')
#plt.show()

#genera top 5 en puntaje
#top5 = ligas.sort_values(by=['Points']).tail(6)
#top5.drop(top5.tail(1).index,inplace=True)
#print(top5)



def estadisticasPartidos():
    descriptor = ligas['MatchesPlayed'].describe()
    print(descriptor)

def estadisticasVictorias():
    descriptor = ligas['Wins'].describe()
    print(descriptor)

def estadisticasEmpates():
    descriptor = ligas['Draws'].describe()
    print(descriptor)

def estadisticasDerrotas():
    descriptor = ligas['Losses'].describe()
    print(descriptor)

def estadisticasPuntos():
    descriptor = ligas['Points'].describe()
    print(descriptor)

def estadisticasGolesDif():
    descriptor = ligas['GoalDiference'].describe()
    print(descriptor)

def menuEstadisticas():
    print("Datos estadisticos")
    print("1. Partidos jugados")
    print("2. Victorias")
    print("3. Empates")
    print("4. Derrotas")
    print("5. Puntos")
    print("6. Diferencia de goles")
    print("7. regresar")
    op=int(input("Escoja una opcion: "))
    if op==1:
        estadisticasPartidos()
    elif op==2:
        estadisticasVictorias()
    elif op==3:
        estadisticasEmpates()
    elif op==4:
        estadisticasDerrotas()
    elif op==5:
        estadisticasPuntos()
    elif op==6:
        estadisticasGolesDif()
    elif op==7:
        menu()
#"Rank", "Squad", "MatchesPlayed", "Wins", "Draws", "Losses", "Points", "GoalDiference"
def menuGraficos():
    print("Graficos")
    print("1. Partidos jugados")
    print("2. Victorias")
    print("3. Empates")
    print("4. Derrotas")
    print("5. Puntos")
    print("6. Diferencia de goles")
    print("7. regresar")
    op=int(input("Escoja una opcion: "))
    if op==1:
        ligas['MatchesPlayed'].plot(kind='bar')
        plt.show()
    elif op==2:
        ligas['Wins'].plot(kind='bar')
        plt.show()
    elif op==3:
        ligas['Draws'].plot(kind='bar')
        plt.show()
    elif op==4:
        ligas['Losses'].plot(kind='bar')
        plt.show()
    elif op==5:
        ligas['Points'].plot(kind='bar')
        plt.show()
    elif op==6:
        ligas['GoalDiference'].plot(kind='bar')
        plt.show()
    elif op==7:
        menu()

def menu():
    while True:
        print("Analisis equipos de futbol")
        print("1. Estadisticas")
        print("2. Graficos")
        print("3. salir")
        op=int(input("Escoja una opcion: "))
        if op==1:
            menuEstadisticas()
        elif op==2:
            menuGraficos()
        elif op==3:
            break

menu()