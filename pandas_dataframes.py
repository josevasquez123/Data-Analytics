import pandas as pd
import numpy as np

#El dataframe es parecido una hoja de datos de excel
#Tambien puede ser interpretado como una combinacion de series


if __name__=="__main__":
    df = pd.DataFrame({
        'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
        'GDP': [
            1785387,
            2833687,
            3874437,
            2167744,
            4602367,
            2950039,
            17348075
        ],
        'Surface Area': [
            9984670,
            640679,
            357114,
            301336,
            377930,
            242495,
            9525067
        ],
        'HDI': [
            0.913,
            0.888,
            0.916,
            0.873,
            0.891,
            0.907,
            0.915
        ],
        'Continent': [
            'America',
            'Europe',
            'Europe',
            'Europe',
            'Asia',
            'Europe',
            'America'
        ]
    }, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

    df.index = [
        'Canada',
        'France',
        'Germany',
        'Italy',
        'Japan',
        'United Kingdom',
        'United States',
    ]

    #print(df.describe())
    #print(df)

    #Llamar una fila mediante loc['Nombre index']
    #print(df.loc['Canada'])

    #Llamar una fila mediante iloc[], aca lo llamas mediante el numero del index
    #print(df.iloc[1])

    #Llama una columna 
    #print(df['Population'])

    #Se puede pedir filas y columnas especificas
    #print(df.iloc[1:3, 3])

    #Se puede filtrar datos con condicionales, pero solo con columnas
    print(df.loc[df['Population']>70])

    #Se pueden combinar con pd.series
    crisis = pd.Series([-1000, -0.5], index=['GDP','HDI'])
    print(df[['GDP','HDI']]+crisis)

    #Se puede eliminar filas
    df.drop('Canada')

    #Se puede agregar filas
    langs = pd.Series(['Germany', 'French', 'Italy'], index=['Germany','France','Italy'])
    df['languages'] = langs
    #print(df)

    df['languages'] = 'English'
    print(df)

    df['GDP Per Capita'] = df['GDP']/df['Population']
    print(df)

    #FUNCIONES EXTRAS
    df.describe()
    df.head()
    df.tail()
    population = df['Population']
    population.mean()
    population.sum()
    population.min()
    population.std()
