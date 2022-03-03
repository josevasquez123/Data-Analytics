from cv2 import merge
import pandas as pd

if __name__=="__main__":
    df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
    parent_theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')

    merged = df.merge(parent_theme, left_on='parent_theme', right_on='name')

    merged.drop(columns='name_y', inplace=True)

    #Obtener el % que tenga licencia y este sea el de Star Wars

    """ licensed = merged[merged['is_licensed']==True]

    licensed = licensed.dropna(subset=['set_num'])              #Aca solo mira los NaN en la columna indicada y elimina esas filas

    star_wars = licensed[licensed['parent_theme']=='Star Wars']

    the_force = int(star_wars.shape[0]/licensed.shape[0]*100)           #El porcentaje """

    #In which year was Star Wars not the most popular licensed theme?

    """ licensed_sorted = licensed.sort_values('year')

    licensed_sorted['count'] = 1

    summed_df = licensed_sorted.groupby(['year', 'parent_theme']).sum().reset_index()

    max_df = summed_df.sort_values('count', ascending=False).drop_duplicates(['year'])

    max_df.sort_values('year', inplace=True)

    new_era = 2017   """

    #print(max_df)

    #Break down number of sets by year

    clean_df = merged[~merged['set_num'].isnull()]

    clean_df['count'] = 1

    sets_per_year = clean_df.groupby('year').sum().reset_index()[['year','count']]

    print(sets_per_year)


    
