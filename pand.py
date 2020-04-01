from datetime import date
import pandas as pd

# ______ OPTION AVEC NOM DE COLUMNS_____ ##

# cree une variable avec la date du jour dans le format que tu veux
today = date.today().strftime("%#m/%d/%y")
print(today)

# lit ton ficher et prend seulement les colonnes que tu veux par nom
covid19Confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'
                               '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
                               usecols=['Country/Region', today])
print(covid19Confirmed)

# _____________________________________________________________________________________________________________________#

# ______ OPTION AVEC INDEX DE COLONNES_____ ##

# lit la premiere ligne seulement pour utiliser moin de ressource
covid19Confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'
                               '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
                               nrows=1)
# cree une variable avec le nombre de colonnes - 1 car les index commence a zero mais pas le nombre des colonnes
nombresDeColumns = len(covid19Confirmed.columns) -1

# lit tous le fichier mais le dans ta variable (prend plus de temps et de memoires)
covid19Confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'
                               '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

# utilise seulement les collonnes qui t'interresse
print(covid19Confirmed.iloc[:, [1, nombresDeColumns]])
