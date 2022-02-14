import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    """ print(pd.isnull(np.nan))                #pd.isna es otro metodo que realiza la misma funcion
    print(pd.notnull(np.nan))               #pd.notna es sinonimo

    print(pd.isnull(pd.Series([1, np.nan, 5])))

    print(pd.notnull(pd.Series([1, np.nan, 5])).sum())              #Te retorna la cantidad de no nan values dentor de tu serie

    s = pd.Series([5, np.nan, 8, 6, 5, np.nan])

    print(s.notnull())

    print(s[s.isnull()])

    print(s.dropna()) """

    #Ahora con pd.Dataframe

    """ df = pd.DataFrame({
        'Column A': [1, np.nan, 30, np.nan],
        'Column B': [2, 8, 31, np.nan],
        'Ccolumn C': [np.nan, 9, 32, 100],
        'Column D': [5, 8, 34, 100]
    })

    print(df.isnull())

    print(df.isnull().sum())

    print(df.info())

    print(df.dropna(thresh=2))

    print(df.fillna(0))                                       #elimina todo los nan y los cambia por el valor que introduces """

    #Metodos para limpiar data erronea

    """ df = pd.DataFrame({
        'Sex': ['M', 'F', 'F', 'D', '?'],
        'Age': [29, 30, 24, 290, 25],
    })

    print(df['Sex'].unique())                                       #Observas datas unicas 
    print(df['Sex'].value_counts())                                 #Observas la cantidadd de datos unicos
    print(df['Sex'].replace('D', 'F'))

    print(df[df['Age']<100])

    df.loc[df['Age']>100, 'Age'] = df.loc[df['Age']>100, 'Age']/10

    print(df) """

    #Duplicate values

    """ ambassadors = pd.Series([
        'France',
        'United Kingdom',
        'United Kingdom',
        'Italy',
        'Germany',
        'Germany',
        'Germany',
    ], index=[
        'Gérard Araud',
        'Kim Darroch',
        'Peter Westmacott',
        'Armando Varricchio',
        'Peter Wittig',
        'Peter Ammon',
        'Klaus Scharioth '
    ])

    print(ambassadors.duplicated())

    print(ambassadors.drop_duplicates()) """

    #print(ambassadors.drop_duplicates(keep='last'))                    Si hay 2 duplicados, toma como duplicado el primero y el ultimo lo deja como el original
    #print(ambassadors.drop_duplicates(keep=false))                     Mantiene todo los duplicados como true

    #Ver los duplicados por columna especifica

    """ players = pd.DataFrame({
        'Name': [
            'Kobe Bryant',
            'LeBron James',
            'Kobe Bryant',
            'Carmelo Anthony',
            'Kobe Bryant',
        ],
        'Pos': [
            'SG',
            'SF',
            'SG',
            'SF',
            'SF'
        ]
    })

    print(players)

    print(players.duplicated(subset=['Name'])) """

    df = pd.DataFrame({
        'Data': [
            '1987_M_US _1',
            '1990?_M_UK_1',
            '1992_F_US_2',
            '1970?_M_   IT_1',
            '1985_F_I  T_2'
    ]})

    print(df['Data'].str.split('_'))

    df= df['Data'].str.split('_', expand=True)

    df.columns = ['Year', 'Sex', 'Country', 'Children']

    df['Year'] = df['Year'].str.replace('?','')
    
    df['Country'] = df['Country'].str.replace(' ', '')

    #df['Year'].str.contains('\?')

    print(df)