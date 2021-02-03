import pandas as pd
import matplotlib.pyplot as plt

#crea el dataframe usando pandas
ligas = pd.read_csv ("./../CodigoRuby/datos.csv")

#borra elementos nan
ligas.dropna()

#nombra columnas
ligas.columns = ["Rank", "Squad", "MatchesPlayed", "Wins", "Draws", "Losses", "Points", "GoalDiference"]

#ligas[list("MatchesPlayed")] = ligas[list("MatchesPlayed")].astype(int)
#print(ligas[ligas.MatchesPlayed < 5])
#genera lista de equipos no repetidos
#equipos = ligas['Squad'].unique().tolist()
#cantidad = len(equipos)
#print(equipos)
#print("La cantidad de equipos diferentes en el mundo del futbol es: ", cantidad)

#descriptor = ligas['Points'].describe()
#media = ligas['Points'].mean()
#print("Datos estadisticos significativos para el analisis")
#print(descriptor)
#print("media aritmetica: ", media)

#maximo = ligas['Points'].max()
#diferencia = maximo - media
#print("La maxima cantidad de puntos es: ", maximo)
#print("La diferencia entre el maximo y la media aritmetica es: ", diferencia)
#print("Los equipos que exeden 62 puntos son: ")

#print(ligas[ligas.Points > 62])
#print(ligas[ligas.Squad == "CS Emelec"])
#print(ligas[ligas['Wins'].between(10, 12)])
#print(ligas[ligas.MatchesPlayed == 10])

#genera grafico
#ligas['Points'].plot(kind='bar')
#plt.show()

#genera top 5 en puntaje
#top5 = ligas.sort_values(by=['Points']).tail(6)
#top5.drop(top5.tail(1).index,inplace=True)
#print(top5)


def buscarPartidos():
    maximo = ligas['MatchesPlayed'].max()
    minimo = ligas['MatchesPlayed'].min()
    print("Determinar signo")
    print("1. =")
    print("2. >")
    print("3. <")
    print("4. Entre valores")
    signo=int(input("Escoja una signo: "))
    
    if signo==1:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.MatchesPlayed == numero])
    elif signo==2:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.MatchesPlayed < numero])
    elif signo==3:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.MatchesPlayed > numero])
    elif signo==4:
        print("Determinar rango")
        print("Ingrese el valor numerico inferior")
        numero1=int(input("Escoja un valor: ")) 
        print("Ingrese el valor numerico superior")
        numero2=int(input("Escoja un valor: "))
        if (numero1 < minimo or numero2 > maximo or numero1 > numero2):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas['MatchesPlayed'].between(numero1, numero2)])      

def buscarVictorias():
    maximo = ligas['Wins'].max()
    minimo = ligas['Wins'].min()
    print("Determinar signo")
    print("1. =")
    print("2. >")
    print("3. <")
    print("4. Entre valores")
    signo=int(input("Escoja una signo: "))
    
    if signo==1:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Wins == numero])
    elif signo==2:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Wins < numero])
    elif signo==3:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Wins > numero])
    elif signo==4:
        print("Determinar rango")
        print("Ingrese el valor numerico inferior")
        numero1=int(input("Escoja un valor: ")) 
        print("Ingrese el valor numerico superior")
        numero2=int(input("Escoja un valor: "))
        if (numero1 < minimo or numero2 > maximo or numero1 > numero2):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas['Wins'].between(numero1, numero2)])      

def buscarEmpates():
    maximo = ligas['Draws'].max()
    minimo = ligas['Draws'].min()
    print("Determinar signo")
    print("1. =")
    print("2. >")
    print("3. <")
    print("4. Entre valores")
    signo=int(input("Escoja una signo: "))
    
    if signo==1:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Draws == numero])
    elif signo==2:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Draws < numero])
    elif signo==3:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Draws > numero])
    elif signo==4:
        print("Determinar rango")
        print("Ingrese el valor numerico inferior")
        numero1=int(input("Escoja un valor: ")) 
        print("Ingrese el valor numerico superior")
        numero2=int(input("Escoja un valor: "))
        if (numero1 < minimo or numero2 > maximo or numero1 > numero2):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas['Draws'].between(numero1, numero2)])      

def buscarDerrotas():
    maximo = ligas['Losses'].max()
    minimo = ligas['Losses'].min()
    print("Determinar signo")
    print("1. =")
    print("2. >")
    print("3. <")
    print("4. Entre valores")
    signo=int(input("Escoja una signo: "))
    
    if signo==1:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Losses == numero])
    elif signo==2:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Losses < numero])
    elif signo==3:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Losses > numero])
    elif signo==4:
        print("Determinar rango")
        print("Ingrese el valor numerico inferior")
        numero1=int(input("Escoja un valor: ")) 
        print("Ingrese el valor numerico superior")
        numero2=int(input("Escoja un valor: "))
        if (numero1 < minimo or numero2 > maximo or numero1 > numero2):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas['Losses'].between(numero1, numero2)])      

def buscarPuntos():
    maximo = ligas['Points'].max()
    minimo = ligas['Points'].min()
    print("Determinar signo")
    print("1. =")
    print("2. >")
    print("3. <")
    print("4. Entre valores")
    signo=int(input("Escoja una signo: "))
    
    if signo==1:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Points == numero])
    elif signo==2:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Points < numero])
    elif signo==3:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.Points > numero])
    elif signo==4:
        print("Determinar rango")
        print("Ingrese el valor numerico inferior")
        numero1=int(input("Escoja un valor: ")) 
        print("Ingrese el valor numerico superior")
        numero2=int(input("Escoja un valor: "))
        if (numero1 < minimo or numero2 > maximo or numero1 > numero2):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas['Points'].between(numero1, numero2)])      

def buscarGoles():
    maximo = ligas['GoalDiference'].max()
    minimo = ligas['GoalDiference'].min()
    print("Determinar signo")
    print("1. =")
    print("2. >")
    print("3. <")
    print("4. Entre valores")
    signo=int(input("Escoja una signo: "))
    
    if signo==1:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.GoalDiference == numero])
    elif signo==2:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.GoalDiference < numero])
    elif signo==3:
        print("Determinar cantidad")
        print("Ingrese un valor numerico")
        numero=int(input("Escoja un valor: "))
        if (numero < minimo or numero > maximo):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas.GoalDiference > numero])
    elif signo==4:
        print("Determinar rango")
        print("Ingrese el valor numerico inferior")
        numero1=int(input("Escoja un valor: ")) 
        print("Ingrese el valor numerico superior")
        numero2=int(input("Escoja un valor: "))
        if (numero1 < minimo or numero2 > maximo or numero1 > numero2):
            print("Valor fuera de rango")
        else:
            print(ligas[ligas['GoalDiference'].between(numero1, numero2)])      


#"Rank", "Squad", "MatchesPlayed", "Wins", "Draws", "Losses", "Points", "GoalDiference"

def buscarEquipo():
    nombre=input("Ingresar nombre del equipo: ")
    print(ligas[ligas.Squad == nombre])

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

def menuBusqueda():
    print("Buscar por:")
    print("1. Partidos jugados")
    print("2. Victorias")
    print("3. Empates")
    print("4. Derrotas")
    print("5. Puntos")
    print("6. Diferencia de goles")
    print("7. Nombre equipo")
    print("8. regresar")
    op=int(input("Escoja una opcion: "))
    if op==1:
        buscarPartidos()
    elif op==2:
        buscarVictorias()
    elif op==3:
        buscarEmpates()
    elif op==4:
        buscarDerrotas()
    elif op==5:
        buscarPuntos()
    elif op==6:
        buscarGoles()
    elif op==7:
        buscarEquipo()
    elif op==8:
        menu()

def menu():
    while True:
        print("Analisis equipos de futbol")
        print("1. Estadisticas")
        print("2. Graficos")
        print("3. Busqueda")
        print("4. salir")
        op=int(input("Escoja una opcion: "))
        if op==1:
            menuEstadisticas()
        elif op==2:
            menuGraficos()
        elif op==3:
            menuBusqueda()
        elif op==4:
            break

menu()