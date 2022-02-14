from unittest import result
from cv2 import add
import pandas as pd
import matplotlib.pyplot as plt


#PRIMER PASO: JUNTAR TODO LOS CSV EN UNO SOLO PARA QUE NO TENGAS QUE REPETIR ESTE PROCESO EN CADA CORRIDA

""" files = [file for file in os.listdir("./Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index=False) """

all_data = pd.read_csv("all_data.csv")

#LIMPIAR LA DATA

#print(all_data[all_data.isnull().any(axis=1)])                              #Para encontrar la data donde esta nan values

all_data = all_data.dropna(how='all')
#print(all_data.isnull().sum())                                              #Confirmar que se borraron todo los nan

#DESPUES DE ELIMINAR LOS NAN, SE ENCONTRO VALORES QUE ERAN LOS NOMBRES DE LAS COLUMNAS

#FIND 'OR' AND DELETE IT

all_data = all_data[all_data['Order Date'].str[:2] != 'Or']   

#CONVERSION DE STR A INT PARA REALIZAR OPERACIONES MATEMATICAS A ALGUNAS COLUMNAS

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

#UN PASO RECOMENDABLE SERIA AUMENTAR UNA COLUMNA PARA MESES, ASI SE PUEDE MOVER LA DATA POR EL MES

all_data['Month'] = all_data['Order Date'].str[:2]
all_data['Month'] = all_data['Month'].astype('int32')

#print(all_data.head())

#AÑADIR UNA COLUMNA DE VENTAS TOTALES AL DIA
all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
#print(all_data.head())

#AÑADIR UNA COLUMNA PARA LA CIUDAD PORQUE UNA PREGUNTA LO NECESITA
def get_state(address):
    return address.split(',')[2].split(' ')[1]

def get_city(address):
    return address.split(',')[1]


all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")
#print(all_data.head())


#Question 1: What was the best month for sales? How much was earned that month?

""" results = all_data.groupby('Month').sum()

months = range(1,13)

plt.bar(months, results['Sales'])

plt.xticks(months)

plt.ylabel('Sales in USD')

plt.xlabel('Month number')

plt.show() """

#Question 2: What city had the highest number of sales?

results = all_data.groupby('City').sum()

cities = [city for city, df in all_data.groupby('City')]

#print(results)

plt.bar(cities, results['Sales'])

plt.xticks(cities, rotation='vertical', size=8)

plt.ylabel('Sales in USD')

plt.xlabel('City name')

plt.show()