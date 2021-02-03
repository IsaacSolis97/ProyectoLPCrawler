import pandas as pd
import matplotlib.pyplot as plt

#crea el dataframe usando pandas
ligas = pd.read_csv ("./../CodigoRuby/datos.csv")

#borra elementos nan
ligas.dropna()

#nombra columnas
ligas.columns = ["Rank", "Squad", "MatchesPlayed", "Wins", "Draws", "Losses", "Points", "GoalDiference"]

print("Analisis y estadisticas sobre los diferentes equipos en sus respectivas ligas")

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
