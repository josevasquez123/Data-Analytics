import pandas as pd

if __name__=="__main__":

    marvel_data = [
        ['Spider-Man', 'male', 1962],
        ['Captain America', 'male', 1941],
        ['Wolverine', 'male', 1974],
        ['Iron Man', 'male', 1963],
        ['Thor', 'male', 1963],
        ['Thing', 'male', 1961],
        ['Mister Fantastic', 'male', 1961],
        ['Hulk', 'male', 1962],
        ['Beast', 'male', 1963],
        ['Invisible Woman', 'female', 1961],
        ['Storm', 'female', 1975],
        ['Namor', 'male', 1939],
        ['Hawkeye', 'male', 1964],
        ['Daredevil', 'male', 1964],
        ['Doctor Strange', 'male', 1963],
        ['Hank Pym', 'male', 1962],
        ['Scarlet Witch', 'female', 1964],
        ['Wasp', 'female', 1963],
        ['Black Widow', 'female', 1964],
        ['Vision', 'male', 1968]
    ]

    """ #Create an empty pandas DataFrame
    x = pd.DataFrame(data=[None], index=[None], columns=[None])
    print(x) """

    """ #Create a marvel_df pandas DataFrame with the given marvel data

    marvel_df = pd.DataFrame(marvel_data)
    print(x) """

    marvel_df = pd.DataFrame(marvel_data)

    #Add column names to the marvel_df
    column_names = ['name', 'sex', 'first_appearance']

    marvel_df.columns = column_names

    #print(marvel_df)

    #Add index names to the marvel_df (use the character name as index)
    marvel_df.index = marvel_df['name']

    #print(marvel_df)

    #Drop the name column as it's now the index
    marvel_df = marvel_df.drop(['name'], axis=1)                                    #Axis 1 es para columnas
    #print(marvel_df)

    #Drop 'Namor' and 'Hank Pym' rows
    marvel_df = marvel_df.drop(['Namor', 'Hank Pym'], axis=0)                       #Axis 0 es para filas    
    #print(marvel_df)

    # Show the first 5 elements on marvel_df
    #print(marvel_df[:5])

    #Show the last 5 elements on marvel_df
    #print(marvel_df[-5:])

    #Show just the sex of the first 5 elements on marvel_df
    #print(marvel_df.iloc[:5,].sex.to_frame())

    #Show the first_appearance of all middle elements on marvel_df
    #print(marvel_df.iloc[1:-1]['first_appearance'].to_frame())

    #Show the first and last elements on marvel_df
    #print(marvel_df.iloc[[0, -1]])

    #Modify the first_appearance of 'Vision' to year 1964
    #marvel_df.loc['Vision','first_appearance'] = '1964'
    #print(marvel_df.loc['Vision'])

    #Add a new column to marvel_df called 'years_since' with the years since first_appearance
    marvel_df['years_since'] = 2021 - marvel_df['first_appearance']
    #print(marvel_df)

    #Given the marvel_df pandas DataFrame, make a mask showing the female characters
    #print(marvel_df[marvel_df['sex']=='female'])

    #Given the marvel_df pandas DataFrame, get the male characters
    #print(marvel_df[marvel_df['sex']=='male'])

    #Show basic statistics of marvel_df
    #print(marvel_df.describe())

    #Given the marvel_df pandas DataFrame, get the female characters with first_appearance after 1970
    print(marvel_df[(marvel_df['sex']=='female') & (marvel_df['first_appearance']>1970)])

    #Given the marvel_df pandas DataFrame, show the min value of first_appearance
    print(marvel_df.first_appearance.min())