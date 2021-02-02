import pandas as pd
import matplotlib.pyplot as plt

ligas = pd.read_csv ("./../CodigoRuby/datos.csv")
ligas.dropna()
ligas.columns = ["Rank", "Squad", "MatchesPlayed", "Wins", "Draws", "Losses", "Points", "GoalDiference"]

print("Analisis y estadisticas sobre los diferentes equipos en sus respectivas ligas")

equipos = ligas['Squad'].unique().tolist()
cantidad = len(equipos)
print(equipos)
print("La cantidad de equipos diferentes en el mundo del futbol es: ", cantidad)


top5 = ligas.sort_values(by=['Points']).tail(6)
top5.drop(top5.tail(1).index,inplace=True)
ligas['Points'].plot(kind='bar')
plt.show()
print(top5)